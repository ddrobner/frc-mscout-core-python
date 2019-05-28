import cv2
import os
import pyzbar.pyzbar as pyzbar
from fileWriter import fileWriter

class decoder:
    def __init__(self):
        self.fw = fileWriter()

    def single(self, cameraIdx):
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

