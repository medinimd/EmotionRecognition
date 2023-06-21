import tensorflow as tf
import matplotlib.pyplot as plt
import cv2
import os
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from fer import FER




train = ImageDataGenerator(rescale=1/255)
validation = ImageDataGenerator(rescale=1/255)


train_dataset = train.flow_from_directory("dataset/train/",
                                            target_size= (200,200),
                                            batch_size = 32,
                                            class_mode = 'binary')
validation_dataset = train.flow_from_directory("dataset/validation/", 
                                            target_size= (200,200),
                                            batch_size = 32,
                                            class_mode = 'binary')


print(train_dataset.class_indices)

model = tf.keras.models.Sequential([tf.keras.layers.Conv2D(16,(3,3),activation= 'relu', input_shape=(200,200,3)),
                                    tf.keras.layers.MaxPool2D(2,2),

                                    tf.keras.layers.Conv2D(32,(3,3),activation= 'relu'),
                                    tf.keras.layers.MaxPool2D(2,2),

                                    tf.keras.layers.Conv2D(64,(3,3),activation= 'relu'),
                                    tf.keras.layers.MaxPool2D(2,2),

                                    tf.keras.layers.Flatten(),

                                    tf.keras.layers.Dense(512,activation='relu'),

                                    tf.keras.layers.Dense(1,activation='sigmoid')
          
])

from tensorflow.keras.optimizers import RMSprop
model.compile(loss= 'binary_crossentropy',
                optimizer = RMSprop(learning_rate=0.001),
                metrics =['accuracy'])



model_fit = model.fit(train_dataset,
                        steps_per_epoch = 1,
                        epochs = 200,
                        validation_data= validation_dataset)


tf.keras.models.save_model(model,'my_model2.hdf5')   


    




