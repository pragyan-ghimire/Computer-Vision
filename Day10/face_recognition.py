import numpy as np
import cv2 as cv
import os

harr_cascade = cv.CascadeClassifier("../Day9/harr_face.xml")

people = [] # ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
DIR = r"../Resources/faces/train"
for i in os.listdir(DIR):
    people.append(i)

features = np.load('../Day10/features.npy')
labels = np.load('../Day10/labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('../Day10/face_trained.yml')