import os
import numpy as np
import cv2 as cv

people = [] # ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
DIR = r"../Resources/faces/train"
for i in os.listdir(DIR):
    people.append(i)

harr_cascade = cv.CascadeClassifier("../Day9/harr_face.xml")
features = []
labels = []

def create_train():
    for person in people:
        # Get the path to the person's directory
        path = os.path.join(DIR, person)
        label = people.index(person)

        # Loop through each image in the person's directory
        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = harr_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in faces_rect:

                # faces region of interest
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
# print(f"Total faces: {len(features)}")
# print(f"Labels: {len(labels)}")

print("----------------Training done!----------------")

features = np.array(features, dtype='object')
labels = np.array(labels)
face_recognizer = cv.face.LBPHFaceRecognizer_create()

# train the recognizer on the features and labels
face_recognizer.train(features, labels)

face_recognizer.save('../Day10/face_trained.yml')

np.save('../Day10/features.npy', features)
np.save('../Day10/labels.npy', labels)