import pyzbar.pyzbar as pyzbar
import cv2
import os
import sys
from messageQR import messageQR

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

camera = cv2.VideoCapture(0)
decodedCode = ""
abortCountdown = 0
ms = messageQR()

def decode(im) :
  # Find barcodes and QR codes
  decodedObjects = pyzbar.decode(im)

  # Print results
  for obj in decodedObjects:
    print('Type : ', obj.type)
    print('Data : ', obj.data,'\n')

  return decodedObjects

if sys.argv[1] == "single":
    multi = False
else:
    multi = True

def writeData(input):
    formatted = ""
    for i in range(len(input) + 1):
        formatted += input[i]
    return formatted

isScanning = False
cwd = os.getcwd()

while True:

    if not multi:
        while True:
            ret, frame = camera.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame', gray)
            decodedCode = decode(frame)
            if decodedCode:
                decodedCode = decode(frame)
    elif multi:
        if not isScanning:
            abortCountdown = 200
            isScanning = True
            isFinished = False
            abort = False
            output = ""

            while not isFinished:
                ret, frame = camera.read()
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                cv2.imshow('frame', gray)
                currentCode = decode(frame)
                if currentCode:
                    if ms.inputMessage(currentCode[0].data.decode("utf-8")):
                        decodedCode = ms.data
                        ms.clearMessage()
                        isFinished = True
                        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA###############################")
                        break
                else:
                    abortCountdown -= 1

                abort = True if abortCountdown <= 0 else False
                if cv2.waitKey(1) == 27:
                    ms.clearMessage()
                if abort:
                    print("Scan Aborted!")

    else:
        print(f"Invalid Argument {sys.argv[1]}!")
        sys.exit(1)
    if decodedCode:
        dataStr = decodedCode[0].data.decode("utf-8")
        #Splits it at the first semicolon, getting the team number
        team = dataStr.split(";")

        #Creates a directory for the team
        try:
            os.mkdir(f"{cwd}/data/{team[1]}")
        except OSError:
            print("Creating directory failed!")

        #Uses f-string to generate filename
        filename = f"{team[3]}{team[4]}_{team[1]}_{team[2]}"

        #Writes the actual data to a file
        try:
            f = open(f"{cwd}/data/{team[1]}/{filename}.fmt", "w+")
            f.write(dataStr)
            f.close()
        except OSError:
            print("Writing data failed!")

        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
