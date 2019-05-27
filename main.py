import pyzbar.pyzbar as pyzbar
import cv2
import os
from fileWriter import fileWriter

fw = fileWriter()
camera = cv2.VideoCapture(0)

def decode(im) :
  # Find barcodes and QR codes
  decodedObjects = pyzbar.decode(im)

  # Print results
  for obj in decodedObjects:
    print('Type : ', obj.type)
    print('Data : ', obj.data,'\n')

  return decodedObjects

while True:
    ret, frame = camera.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Scan Code', gray)

    cwd = os.getcwd()

    decodedCode = decode(frame)

    if decodedCode:
        fw.writeData(decodedCode)
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
