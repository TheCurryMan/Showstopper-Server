import numpy as np
# import pyrebase
# from PIL import Image
# # import cv2
# import requests
# from io import BytesIO
# import matplotlib.pyplot as plt
# import keras
from resizeimage import resizeimage
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Dropout, Flatten
# from keras.utils import to_categorical
from keras.utils import np_utils
from keras.models import load_model
import PIL.ImageOps    

#Clothing dataset
from keras.datasets import fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
train_images = train_images[:30000]
train_labels = train_labels[:30000]
test_images = train_images[:30000]
test_labels = train_labels[:30000]


#Change to float and resize
num_classes = len(np.unique(train_labels))
train_images = train_images.astype('float32')
test_images = test_images.astype('float32')
# cv2.imwrite('prefx_training.png', train_images[0,:,:])
train_images /= 255
# cv2.imwrite('postfx_training.png', train_images[0,:,:])
test_images /= 255
rows, cols = train_images.shape[1:]
train_data = train_images.reshape(train_images.shape[0], 1, rows, cols)
test_data = test_images.reshape(test_images.shape[0], 1, rows, cols)
input_shape = (1, rows, cols)
train_labels_one_hot = np_utils.to_categorical(train_labels, 10)
test_labels_one_hot = np_utils.to_categorical(test_labels, 10)

def createModel():
    model = Sequential()
    model.add(Conv2D(28, (3, 3), padding='same', activation='relu', input_shape=input_shape, data_format = 'channels_first'))
    model.add(Conv2D(28, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=2))
    model.add(Dropout(0.25))

    model.add(Conv2D(56, (3, 3), padding='same', activation='relu'))
    model.add(Conv2D(56, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=2))
    model.add(Dropout(0.5))

    model.add(Conv2D(56, (3, 3), padding='same', activation='relu'))
    model.add(Conv2D(56, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=2))
    model.add(Dropout(0.5))

    model.add(Flatten())
    model.add(Dense(512, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes, activation='softmax'))
    
    return model

# model1 = createModel()
# batch_size = 256
# epochs = 50
# model1.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
# model1.summary()
# history = model1.fit(train_data, train_labels_one_hot, batch_size=batch_size, epochs=epochs, verbose=1,
#                     validation_data=(test_data, test_labels_one_hot))
# model1.save('30000samp.h5')

def predict(img):
    test_model = load_model('10000samp.h5')
    test_model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
    img = img.convert('L')
    img = resizeimage.resize_cover(img, [28,28])
    inverted_image = PIL.ImageOps.invert(img)
    img = np.array(inverted_image)
    img = img.astype('float32')
    img /= 255
    final_img = np.reshape(img, [1, 1, 28, 28])
    predictions = test_model.predict_classes(final_img, batch_size=128, verbose=1)
    return predictions[0]