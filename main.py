import pyzbar.pyzbar as pyzbar
import cv2
import os
from fileWriter import fileWriter

fw = fileWriter()
camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Scan Code', gray)

    cwd = os.getcwd()

    decodedCode = pyzbar.decode(frame)

    if decodedCode:
        fw.writeData(decodedCode)
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
