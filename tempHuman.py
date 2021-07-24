import os
import tkinter as tk
from tkinter import filedialog
import cv2
import time
import datetime

import face
import sendMail

# root = tk.Tk()
# root.withdraw()
#
# file_path = filedialog.askopenfilename()
def  mainFunction(file_path):
    person_cascade = cv2.CascadeClassifier(
        os.path.join('haarcascade_fullbody.xml'))
    cap = cv2.VideoCapture(file_path)
    fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
    out = cv2.VideoWriter("output.avi", fourcc, 5.0, (1280,720))
    while True:
        r, frame = cap.read()
        if r:
            start_time = time.time()
            frame = cv2.resize(frame, (640, 360))  # Downscale to improve frame rate
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)  # Haar-cascade classifier needs a grayscale image
            rects = person_cascade.detectMultiScale(gray_frame)

            end_time = time.time()
            #print("Elapsed Time:", end_time - start_time)

            for (x, y, w, h) in rects:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.imwrite(r"test2.jpg", frame[y:y + h, x:x + w])
                cv2.imwrite(r"encroacher.jpg", frame)

            cv2.imshow("preview", frame)


        k = cv2.waitKey(1)
        if k & 0xFF == ord("q"):  # Exit condition
            break

    ts = time.time()
    #st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d, %H:%M:%S')
    # x2=x1+width
    # y2=y1+height
    # screenshot=screenshot.crop((x1,y1,x2,y2))
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d, %H:%M:%S')
    # x2=x1+width
    # y2=y1+height
    # screenshot=screenshot.crop((x1,y1,x2,y2))
    obj = face.getCharacteristics()
    characterists = str(obj["age"]) + " years old ,"+obj["dominant_race"]+", "+obj["dominant_emotion"]+" ,"+ obj["gender"]
    mailFunctionResponse="NOT SENT"
    print("SENDING MAIL")
    mailFunctionResponse = sendMail.send("ENCROACHER DETECTED", st, characterists)
    print("Mail Response:")
    #os.save(screenshot)
    #im1=Image.open(screenshot)
    #im1.save("sample.jpg")
    #Image.save(screenshot, format=None, **params)
    print(mailFunctionResponse)
    cv2.destroyAllWindows()
    cap.release()
    out.release()
