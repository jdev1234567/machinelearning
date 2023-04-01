import os
import cv2
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from PIL import Image

class Digit:
    def model(self):

        train_new_model = False

        if train_new_model:
            mnist = tf.keras.datasets.mnist
            (X_train, y_train), (X_test, y_test) = mnist.load_data()

            X_train = tf.keras.utils.normalize(X_train, axis=1)
            X_test = tf.keras.utils.normalize(X_test, axis=1)

            #
            model = tf.keras.models.Sequential()
            model.add(tf.keras.layers.Flatten())
            model.add(tf.keras.layers.Dense(units=128, activation=tf.nn.relu))
            model.add(tf.keras.layers.Dense(units=128, activation=tf.nn.relu))
            model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.softmax))


            model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])


            model.fit(X_train, y_train, epochs=3)


            val_loss, val_acc = model.evaluate(X_test, y_test)
            print(val_loss)
            print(val_acc)


            model.save('handwritten_digits.model')
        else:
            # Load the model
            model = tf.keras.models.load_model('handwritten_digits.model')


        try:
                img = Image.open('myphoto.png')
                a = img.convert("P", palette=Image.ADAPTIVE, colors=24)
                a.save('myphoto.png')
                img = cv2.imread('myphoto.png')[:, :, 0]

                img = np.invert(np.array([img]))
                prediction = model.predict(img)
                print("The number is probably a {}".format(np.argmax(prediction)))
                #plt.imshow(img[0])
                #plt.show()

                return "The number is probably a {}".format(np.argmax(prediction))
        except Exception as e:
                pass