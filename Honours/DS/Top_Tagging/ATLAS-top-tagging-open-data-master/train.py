"""

######################### ATLAS Top Tagging Open Data ##########################

train.py - This is an example script for training constituent based taggers
on the ATLAS Top Tagging Open Data set.

For details of the data set and performance baselines, see (*CDS pub note link*).

Author: Kevin Greif
Last updated 8/1/2022
Written in python 3

################################################################################

"""

import sys

# Data I/O and numerical imports
import h5py
import numpy as np

# ML imports
import tensorflow as tf
from tensorflow.data import Dataset
from energyflow.archs import EFN, PFN
import sklearn.metrics as metrics
from sklearn.model_selection import train_test_split

# Plotting imports
import matplotlib.pyplot as plt

# Custom imports
import Honours.DS.Top_Tagging.preprocessing as preprocessing

################################# SETTINGS #####################################

# Settings used for data preparation and network training. For model hyper-
# parameters, see "Build Tagger and Datasets" section

# Paths to data files. Point these to local download of training / testing sets
train_path = '/home/WindowsDrive/Shared/Top_Tagging_Data/test.h5'
test_path = '/home/WindowsDrive/Shared/Top_Tagging_Data/test.h5'

# Set the amount of data to be used in training and testing. The full training
# set is very large (130 GB) and will not fit in memory all at once. Here, we
# take a subset  of the data. Using the full set will require piping.
n_train_jets = -1
n_test_jets = -1

# Set the fraction of the training data which will be reserved for validation
valid_fraction = 0.2

# Max constituents to consider in tagger training (must be <= 200)
max_constits = 80

# Tagger to train, supported options are 'hldnn', 'dnn', 'efn', 'pfn'.
tagger_type = 'hldnn'

# Training parameters
num_epochs = 20
batch_size = 256

########################### Data Preparation ###################################
print("Read data and prepare for tagger training")

# Load data from files using h5py
train = h5py.File(train_path, 'r')
test = h5py.File(test_path, 'r')

# Find names of appropriate names of numpy arrays from h5py file objects.
if tagger_type == 'hldnn':
    data_vector_names = train.attrs.get('hl')
else:
    data_vector_names = train.attrs.get('constit')

# Load data into a python dictionary for pass into pre-processing functions
train_dict = {key: train[key][:n_train_jets,...] for key in data_vector_names}
test_dict = {key: test[key][:n_test_jets,...] for key in data_vector_names}

# Pass dictionaries to preprocessing functions
if tagger_type == 'hldnn':
    # Data shapes: (n_jets, 15)
    print("Processing high level quantity information")
    train_data = preprocessing.high_level(train_dict)
    test_data = preprocessing.high_level(test_dict)
    num_data_features = train_data.shape[-1]
else:
    # Data shapes: (n_jets, max_constits, 7)
    print("Processing constituent information")
    train_data = preprocessing.constituent(train_dict, max_constits)
    test_data = preprocessing.constituent(test_dict, max_constits)
    num_data_features = train_data.shape[-1]

# Load labels and training weights
train_labels = train['labels'][:n_train_jets]
train_weights = train['weights'][:n_train_jets]
test_labels = test['labels'][:n_test_jets]
test_weights = test['labels'][:n_test_jets]

# Load testing set jet pT for plotting purposes
jet_pt = test['fjet_pt'][:n_test_jets]

####################### Build Tagger and Datasets  #############################
print("Building tagger and datasets")

# Due to EFN's data shape requirements, the EFN data set build is separate
# from the other models.

if tagger_type == 'efn':

    # Build and compile EFN
    model = EFN(
        input_dim=2,
        Phi_sizes=(350, 350, 350, 350, 350),
        F_sizes=(300, 300, 300, 300, 300),
        Phi_k_inits="glorot_normal",
        F_k_inits="glorot_normal",
        latent_dropout=0.084,
        F_dropouts=0.036,
        loss="binary_crossentropy",
        optimizer=tf.keras.optimizers.Adam(learning_rate=6.3e-5),
        output_dim=1,
        output_act='sigmoid',
        summary=False
    )

    # For EFN, take only eta, phi, and log(pT) quantities, and package into
    # a single dataset. We want each element of the data set to have shape:
    #   ((batch_size, max_constits, 1), (batch_size, max_constits, 2))
    # We can do this using tensorflow Dataset's "zip" function.
    # This code assumes quantities are ordered (eta, phi, pT, ...)
    train_angular = train_data[:,:,0:2]
    train_pt = train_data[:,:,2]

    test_angular = test_data[:,:,0:2]
    test_pt = test_data[:,:,2]

    # Make train / valid split using sklearn train_test_split function
    (train_angular, valid_angular, train_pt,
     valid_pt, train_labels, valid_labels,
     train_weights, valid_weights) = train_test_split(
        train_angular,
        train_pt,
        train_labels,
        train_weights,
        test_size=valid_fraction
    )

    # Build tensorflow data sets
    train_list = [train_pt, train_angular, train_labels, train_weights]
    train_sets = tuple([Dataset.from_tensor_slices(i).batch(batch_size)
                        for i in train_list])
    train_data = Dataset.zip(train_sets[:2])
    train_dataset = Dataset.zip((train_data,) + train_sets[2:])

    valid_list = [valid_pt, valid_angular, valid_labels, valid_weights]
    valid_sets = tuple([Dataset.from_tensor_slices(i).batch(batch_size)
                        for i in valid_list])
    valid_data = Dataset.zip(valid_sets[:2])
    valid_dataset = Dataset.zip((valid_data,) + valid_sets[2:])

    test_list = [test_pt, test_angular, test_labels, test_weights]
    test_sets = tuple([Dataset.from_tensor_slices(i).batch(batch_size)
                       for i in test_list])
    test_data = Dataset.zip(test_sets[:2])
    test_dataset = Dataset.zip((test_data,) + test_sets[2:])

# For all other models, data sets can be built using the same process, so
# these are handled together

else:

    if tagger_type == 'hldnn':

        # Build hlDNN
        model = tf.keras.Sequential()
        model.add(tf.keras.Input(shape=train_data.shape[1:]))

        # Hidden layers
        for _ in range(5):
            model.add(tf.keras.layers.Dense(
                180,
                activation='relu',
                kernel_initializer='glorot_uniform')
            )

        # Output layer
        model.add(tf.keras.layers.Dense(
            1,
            activation='sigmoid',
            kernel_initializer='glorot_uniform')
        )

        # Compile hlDNN
        model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=4e-5),
            # from_logits set to False for uniformity with energyflow settings
            loss=tf.keras.losses.BinaryCrossentropy(from_logits=False),
            metrics=[tf.keras.metrics.BinaryAccuracy(name='accuracy')]
        )

    elif tagger_type == 'dnn':

        # For DNN, we also need to flatten constituent data into shape:
        # (n_jets, max_constits * 7)
        train_data = train_data.reshape(-1, max_constits * num_data_features)
        test_data = test_data.reshape(-1, max_constits * num_data_features)

        # Build DNN
        model = tf.keras.Sequential()
        model.add(tf.keras.Input(shape=train_data.shape[1:]))

        # Hidden layers
        for i in range(5):
            model.add(tf.keras.layers.Dense(
                400,
                kernel_initializer='glorot_uniform',
                kernel_regularizer=tf.keras.regularizers.l1(l1=2e-4)
            ))
            model.add(tf.keras.layers.BatchNormalization(axis=1))
            model.add(tf.keras.layers.ReLU())


        # Output layer
        model.add(tf.keras.layers.Dense(
            1,
            activation='sigmoid',
            kernel_initializer='glorot_uniform',
            kernel_regularizer=tf.keras.regularizers.l1(l1=2e-4))
        )

        # Compile DNN
        model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=1.2e-5),
            # from_logits set to False for uniformity with energyflow settings
            loss=tf.keras.losses.BinaryCrossentropy(from_logits=False),
            metrics=[tf.keras.metrics.BinaryAccuracy(name='accuracy')]
        )

    elif tagger_type == 'pfn':

        # Build and compile PFN
        model = PFN(
            input_dim=7,
            Phi_sizes=(250, 250, 250, 250, 250),
            F_sizes=(500, 500, 500, 500, 500),
            Phi_k_inits="glorot_normal",
            F_k_inits="glorot_normal",
            latent_dropout=0.072,
            F_dropouts=0.022,
            loss="binary_crossentropy",
            optimizer=tf.keras.optimizers.Adam(learning_rate=7.9e-5),
            output_dim=1,
            output_act='sigmoid',
            summary=False
        )

    else:
        raise ValueError("Tagger type setting not recognized")

    # Make train / valid split using sklearn train_test_split function
    (train_data, valid_data, train_labels,
     valid_labels, train_weights, valid_weights) = train_test_split(
        train_data,
        train_labels,
        train_weights,
        test_size=valid_fraction
    )

    # Build tensorflow datasets.
    # In tf.keras' "fit" API, the first argument is the inputs, the second is
    # the labels, and the third is an optional "sample weight". This is where
    # the training weights should be applied.
    # See: https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit
    train_dataset = tf.data.Dataset.from_tensor_slices((
        train_data,
        train_labels,
        train_weights)
    ).batch(batch_size)

    valid_dataset = tf.data.Dataset.from_tensor_slices((
        valid_data,
        valid_labels,
        valid_weights)
    ).batch(batch_size)

    test_dataset = tf.data.Dataset.from_tensor_slices((
        test_data,
        test_labels,
        test_weights)
    ).batch(batch_size)

############################### Train Tagger ###################################
print("Starting tagger training")

# Train tagger with keras fit function. Use validation_split argument to
# partition the training data into train/validation sets.
train_history = model.fit(
    train_dataset,
    validation_data=valid_dataset,
    batch_size=batch_size,
    epochs=num_epochs,
    verbose=1
)

# Plot training and validation loss against training epochs
plt.plot(train_history.history['loss'], label='Training')
plt.plot(train_history.history['val_loss'], label='Validation')
plt.ylabel('Cross-entropy Loss')
plt.xlabel('Training Epoch')
plt.legend()
plt.savefig('./plots/loss.png', dpi=300)
plt.clf()

############################### Evaluate Tagger ################################
print("Run tagger evaluation")

# Run prediction on the testing set. Make cut on tagger output at 0.5 to
# evaluate accuracy metric
predictions = model.predict(test_dataset, batch_size=batch_size)[:,0]
discrete_predictions = (predictions > 0.5).astype(int)

# Evaluate metrics
auc = metrics.roc_auc_score(test_labels, predictions)
acc = metrics.accuracy_score(test_labels, discrete_predictions)

# Evaluate background rejection at fixed signal efficiency working points
fpr, tpr, thresholds = metrics.roc_curve(test_labels, predictions)
point5_index = np.argmax(tpr > 0.5)
br_point5 = 1 / fpr[point5_index]
point8_index = np.argmax(tpr > 0.8)
br_point8 = 1 / fpr[point8_index]

# Print metric results
print('\nPerformance metrics evaluated over testing set:')
print('AUC score:', auc)
print('ACC score:', acc)
print('Background rejection at 0.5 signal efficiency:', br_point5)
print('Background rejection at 0.8 signal efficiency:', br_point8)

# Plot ROC curve
plt.plot(tpr, 1 / fpr)
plt.yscale('log')
plt.ylabel('Background rejection')
plt.xlabel('Signal efficiency')
plt.savefig('./plots/roc.png', dpi=300)
plt.clf()

# Finally make a plot of the background rejection versus jet pT. Start by making
# a set of pT bins and empty vectors to accept B.R. values. Note pt bin array
# defines bin edges
pt_bins = np.linspace(350000, 3150000, 15)
br_point5_array = np.zeros(len(pt_bins) - 1)
br_point8_array = np.zeros(len(pt_bins) - 1)

# Loop through pT bins
for i in range(len(pt_bins) - 1):

    # Find the indeces of the jets that lie in this pT bin
    condition = np.logical_and(jet_pt > pt_bins[i], jet_pt < pt_bins[i+1])
    bin_indeces = condition.nonzero()[0]

    # Now take predictions and labels which fall in this pT bin
    bin_predictions = predictions[bin_indeces]
    bin_labels = test_labels[bin_indeces]

    # Calculate the background rejection at fixed signal efficiency
    fpr, tpr, thresholds = metrics.roc_curve(bin_labels, bin_predictions)
    bin_point5_index = np.argmax(tpr > 0.5)
    br_point5_array[i] = 1 / fpr[bin_point5_index]
    bin_point8_index = np.argmax(tpr > 0.8)
    br_point8_array[i] = 1 / fpr[bin_point8_index]

# Duplicate last entry in background rejection arrays
br_point5_array = np.concatenate((br_point5_array, br_point5_array[-1:]))
br_point8_array = np.concatenate((br_point8_array, br_point8_array[-1:]))

# Make a plot using matplotlib's step function
plot_bins = pt_bins / 1e6 # Set plot on TeV scale
plt.step(plot_bins, br_point5_array, '-', where='post', label=r'$\epsilon_{sig} = 0.5$')
plt.step(plot_bins, br_point8_array, '--', where='post', label=r'$\epsilon_{sig} = 0.8$')
plt.ylabel('Background rejection')
plt.xlabel('Jet pT (TeV)')
plt.legend()
plt.savefig('./plots/br_vs_pt.png', dpi=300)
