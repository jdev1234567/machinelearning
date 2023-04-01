
import numpy as np
import cv2

import tensorflow as tf



class Paint:



    def guess_image(self,path):
        model = tf.keras.models.load_model('model.h5')
        print(model.summary())
        img = cv2.imread(path)
        img_copy = img.copy()
        img_final = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
        img_final = cv2.resize(img_final, (28, 28))
        img_final = np.reshape(img_final, (1, 28, 28, 1))
        img_final = np.divide(img_final, 255.0)
        img_final = np.subtract(1, img_final)

        img_pred = chr(np.argmax(model.predict(img_final)) + 65)
        # print(model.predict(img_final))
        # plt.imshow(img_final[0], cmap="Greys")
        # plt.xlabel("Prediction: " + img_pred)
        # plt.show()

        return img_pred

