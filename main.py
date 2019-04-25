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

while True:
    ret, frame = camera.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)


    isScanning = False
    cwd = os.getcwd()

    if not multi:
        decodedCode = decode(frame)
    else:
       if not isScanning:
            isScanning = True
            isFinished = False
            abort = False
            output = ""

            while not isFinished and not abort:
                currentCode = decode(frame)
                if currentCode:
                    abortCountdown = 200
                    if ms.inputMessage(currentCode):
                        decodedCode = ms.data
                        ms.clearMessage()
                        isFinished = True
                else:
                    abortCountdown -= 1
                abort = abortCountdown <= 0
                if cv2.waitKey(1) == 27:
                    ms.clearMessage()
                if abort:
                    print("Scan Aborted!")





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
