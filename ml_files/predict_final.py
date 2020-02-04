from os import listdir
from os.path import join,isfile
from keras.preprocessing import image
from keras.models import load_model
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import cv2
import math
import imutils
from collections import Counter

model = load_model("model_new4.h5")

test_dir = '/home/ekta/hack/dataset/test/'

model.compile(loss="mean_squared_error",
            optimizer='rmsprop',
            metrics=['accuracy']
)

onlyfiles = [f for f in listdir(test_dir) if isfile(join(test_dir, f))]
print(onlyfiles)

for files in onlyfiles:
    img = image.load_img(test_dir+files,target_size=(150,150))
    x = image.img_to_array(img)
    x = np.expand_dims(x,axis=0)

    images = np.vstack([x])
    # plt.imshow(images)
    classes = model.predict_classes(images,batch_size=3)
    print(classes)
    # classes = classes[0]

''' using opencv to detect face .. '''


face_cascade=cv2.CascadeClassifier('harcascade_frontalface_default.xml')
print(face_cascade)



cap = cv2.VideoCapture(0)
i=0
ls=[]
while True:
    ret,test_img=cap.read()
    if not ret:
        continue
    gray_img=cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)
    # print(gray_img.shape)
    faces_detected = face_cascade.detectMultiScale(gray_img,1.32,5)
    for (x,y,w,h) in faces_detected:
        cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=7)

        roi_gray=gray_img[y:y+w,x:x+h]
        roi_gray = cv2.resize(roi_gray,(150,150))
        img_pixels = image.img_to_array(roi_gray)

        img_pixels = np.expand_dims(img_pixels,axis=0)

        img_pixels/=255
        # img_pixels.reshape(150,150,3)
        img_pixels = np.resize(img_pixels,(1,150,150,3))
        print(img_pixels.shape)
        predictions = model.predict(img_pixels)
        #
        max_index = np.argmax(predictions[0])
        #
        print(max_index)
        emotions = ('Ekta','sanjeev')
        #
        predicted_emotion = emotions[max_index]
        print('predicted emotion',predicted_emotion)
        if(i%5==0):
            ls.append(predicted_emotion)
        cv2.putText(test_img,predicted_emotion, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    resized_img = cv2.resize(test_img, (1000, 700))

    cv2.imshow('Facial emotion analysis ',resized_img)
    i=i+1

    if cv2.waitKey(10) == ord('q'):
        break

    # elif i==60:
    #     break


print(ls)
res = dict(Counter(ls))
print(res)
Keymax = max(res, key=res.get)
print('Person is  ',Keymax)

cap.release()
cv2.destroyAllWindows()
