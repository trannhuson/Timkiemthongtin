import face_recognition
import os
import cv2
from collections import Counter
import tkinter
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image,ImageTk
import pymysql.cursors
from datetime import datetime

KNOWN_FACES_FOLDER = 'know'
UNKNOWN_FACES_FOLDER = 'unkno'
DIFFERENCE = 0.4
MODEL = 'cnn'



known_faces = []
known_names = []

def changeSize(path):
    img = cv2.imread(path)
    return cv2.resize(img, (200, 300))


for name in os.listdir(KNOWN_FACES_FOLDER):

    for filename in os.listdir(f'{KNOWN_FACES_FOLDER}/{name}'):

        image = face_recognition.load_image_file(f'{KNOWN_FACES_FOLDER}/{name}/{filename}')

        #return list found face
        encoding = face_recognition.face_encodings(image)[0]

        known_faces.append(encoding)
        known_names.append(name)


print('Processing unknown faces...')
print(known_names)

for filename in os.listdir(UNKNOWN_FACES_FOLDER):
    print("fileName: "+ filename)
    print(" os.listDir: ",os.listdir(UNKNOWN_FACES_FOLDER))

    print(f'Filename {filename}')
    image = face_recognition.load_image_file(f'{UNKNOWN_FACES_FOLDER}/{filename}')

    locations = face_recognition.face_locations(image, model=MODEL)

    encodings = face_recognition.face_encodings(image, locations)

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    print(f', found {len(encodings)} face(s)')
    for face_encoding, face_location in zip(encodings, locations):

        results = face_recognition.compare_faces(known_faces, face_encoding, DIFFERENCE)

        name = "unknow"
        #print(name)

        if True not in results:

            top_left = (face_location[3], face_location[0])
            bottom_right = (face_location[1], face_location[2])

            cv2.rectangle(image, top_left, bottom_right, (0,0,255), 2)

            #pain text
            top_left = (face_location[3], face_location[2])
            bottom_right = (face_location[1], face_location[2] + 22)

            cv2.rectangle(image, top_left, bottom_right, (0,255,0), cv2.FILLED)

            cv2.putText(image, name, (face_location[3] + 10, face_location[2] + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 3)
        else :
            arr = []
            for i in range(len(known_names)):
                if results[i] == True:
                    if known_names[i] not in arr:
                        arr.append(known_names[i])
                    else :
                        arr.append(known_names[i])

            #print(arr)
            dem = Counter(arr)
            sl=[]

            pt = []
            if len(arr) != 0:
                sl.append(dem[arr[0]])
                pt.append(arr[0])
            for i in range(len(arr)-1):
                if arr[i] != arr[i+1] :
                    sl.append(dem[arr[i+1]])
                    pt.append(arr[i+1])
            # print(sl)
            # print(pt)

            if len(sl) != 0:
                max1 = max(sl)

            # print(max1)


            arrName = []
            for i in range(len(pt)):
                if sl[i] == max1:
                    arrName.append(pt[i])

            #print(arrName)

            for i in arrName:

                name = i

                print(f' - {name} from {results}')

                top_left = (face_location[3], face_location[0])
                bottom_right = (face_location[1], face_location[2])

                cv2.rectangle(image, top_left, bottom_right, (0,0,255), 2)

                top_left = (face_location[3], face_location[2])
                bottom_right = (face_location[1], face_location[2] + 22)

                cv2.rectangle(image, top_left, bottom_right, (0,0,255), cv2.FILLED)

                cv2.putText(image, name, (face_location[3] + 10, face_location[2] + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 2)

    cv2.imshow(filename, image)
    cv2.waitKey(0)
    cv2.destroyWindow(filename)
