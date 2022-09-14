import h5py
import numpy
import preprocessing
import tensorflow as tf
# import pickle

dataPath = '/home/WindowsDrive/Shared/Top_Tagging_Data/test.h5'
# trainDictFile = open('trainDict.pkl', 'w')
# testDictFile = open('testDict.pkl', 'w')
tagger_type = 'pfn'

def constituentProcessing(data_dict, max_constits):
    pt = data_dict['fjet_clus_pt'][:,:max_constits]
    eta = data_dict['fjet_clus_eta'][:,:max_constits]
    phi = data_dict['fjet_clus_phi'][:,:max_constits]
    energy = data_dict['fjet_clus_E'][:,:max_constits]

with h5py.File(dataPath, 'r') as data:

    dataKeys = data.keys()
    numJets = data.attrs.get('num_jets')
    halfNumJets = int(numJets / 2)

    trainDict = {key: data[key][:halfNumJets,...] for key in data.attrs.get('constit')}
    testDict = {key: data[key][halfNumJets:,...] for key in data.attrs.get('constit')}

    # pickle.dump(trainDict, trainDictFile)
    # pickle.dump(testDict, testDictFile)

    train_labels = data['labels'][:halfNumJets]
    train_weights = data['weights'][:halfNumJets]
    test_labels = data['labels'][halfNumJets:]
    test_weights = data['labels'][halfNumJets:]

    # processedData = preprocessing.constituent(trainDict, 80)

    # print(processedData[0])


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


# trainDictFile.close()
# testDictFile.close()
