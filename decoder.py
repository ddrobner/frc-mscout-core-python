import cv2
import os
import pyzbar.pyzbar as pyzbar
from fileWriter import fileWriter

class decoder:
    # Creates a filewriter object
    def __init__(self):
        self.fw = fileWriter()

    def single(self, cameraIdx):
        # Creates camera (needs to be in here so I can pass the camera id as an
        # argument)
        self.camera = cv2.VideoCapture(cameraIdx)
        while True:
            ret, frame = self.camera.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('Scan Code', gray)

            cwd = os.getcwd()

            decodedCode = pyzbar.decode(frame)

            if decodedCode:
                self.fw.writeData(decodedCode)
                self.camera.release()
                cv2.destroyAllWindows()
                break
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.camera.release()
                cv2.destroyAllWindows()
                break

