import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)

#Load known faces 
divyanshi_image = face_recognition.load_image_file("divyanshi.jpg")
divyanshi_encoding = face_recognition.face_encodings(divyanshi_image)[0]

known_face_encoding = [divyanshi_encoding]
known_face_names = ["Divyanshi"]

#list of expected students
students = known_face_names.copy()

face_locations = []
face_encodings = []

#Get the current date and time
now = datetime.now()
current_date = now.strftime("%d/%m/%Y, %H:%M:%S")
f = open(f"{current_date}.csv" , "w+" , newline="")
lnwrite = csv.writer(f)

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame , (0,0) , fx=0.25 , fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame , cv2.COLOR_BGR2RGB)
    #Recognition of faces
    matches = face_recognition.compare_faces(known_face_encoding , face_encodings)
    face_distance = face_recognition.face_distance(known_face_encoding , face_encodings)
    best_match_index = np.argmin(face_distance)

    if(matches[best_match_index]):
        name = known_face_names[best_match_index]
    
    # Add the text if a person is present
    if name in known_face_names:
        font = cv2.FONT_HERSHEY_TRIPLEX
        bottomLeftCornerOfText = (10 ,100)
        fontScale = 1.5
        fontColor = (255 ,0 ,0)
        thickness = 3
        linetype = 2
        cv2.putText(frame , name + "Present")
    cv2.imshow("Attendence" , frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
video_capture.release()
cv2.destroyAllWindows()
f.close()
