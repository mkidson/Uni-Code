import h5py
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense  
from keras import backend as K
from sklearn.model_selection import train_test_split
import pandas as pd
import tables
import matplotlib.pyplot as plt
import tensorflow as tf

gpu_devices = tf.config.experimental.list_physical_devices('GPU')
for device in gpu_devices:
    tf.config.experimental.set_memory_growth(device, True)
    
dataPath = '/home/WindowsDrive/Shared/Top_Tagging_Data/test.h5'

with h5py.File(dataPath, 'r') as data:

    npDataLabels = np.array(data['labels'])

    npDataWeights = np.array(data['weights'])
    
    hlDataArr = {key: data[key][...] for key in data.attrs.get('hl')}

    df = pd.DataFrame(hlDataArr)

data_train, data_test, labels_train, labels_test, weights_train, weights_test = train_test_split(df, npDataLabels, npDataWeights, test_size=0.33, random_state=69, shuffle=True)

model = Sequential()
model.add(keras.Input(shape=15))
model.add(Dense(20, activation='relu', kernel_regularizer=None))
model.add(Dense(20, activation='relu', kernel_regularizer=None))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam')   
model.fit(data_train, labels_train, sample_weight=weights_train, epochs=8, batch_size=100, verbose=1)