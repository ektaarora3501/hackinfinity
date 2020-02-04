import os
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Conv2D,MaxPooling2D,Dropout,Flatten,Activation,Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from keras.losses import binary_crossentropy


train_dir = '/home/ekta/hack/train1/'
# test_dir = '/home/ekta/hack/dataset/test'

# setting hyperparametes

HEIGHT = 150
WIDHT = 150
SAMPLES = 48
EPOCHS = 3
BATCH_SIZE = 1
INPUT_SHAPE = (HEIGHT,WIDHT,3)

model = Sequential()
# creating the first layer
model.add(Conv2D(32,(3,3),input_shape=INPUT_SHAPE))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(32,(3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(64,(3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))


model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.2))


model.add(Dense(2))
model.add(Activation('sigmoid'))

# model.add(Dropout(0.5))

model.compile(loss = "mean_squared_error",
               optimizer = Adam(),
               metrics=['accuracy'],)

train_data_gen = ImageDataGenerator(
        rescale = 1./255,
        shear_range =0.2,
        zoom_range =0.2,
        horizontal_flip= True,
)

training_generator = train_data_gen.flow_from_directory(
              train_dir,
              target_size = (WIDHT,HEIGHT),
              batch_size= BATCH_SIZE,
               class_mode = "categorical",
)

print(training_generator.class_indices)

model.fit(training_generator,
          epochs=EPOCHS,
          steps_per_epoch=SAMPLES//BATCH_SIZE,
          verbose =1,
          # epochs=EPOCHS
          )


model.save('model_new4.h5')
