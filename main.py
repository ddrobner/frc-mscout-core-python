import pyzbar.pyzbar as pyzbar
import cv2
import os

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
