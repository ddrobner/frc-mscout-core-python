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

def writeData(code):
    data = code[0].data.decode("utf-8").split(";")

    # Creates directory and returns false if it fails
    try:
        os.mkdir(f"{cwd}/data/{data[1]}")
        print(f"Created Folder: {data[1]}")
    except OSError:
        print("Creating Directory Failed!")
        return False
    # Creates a filename substituting the appropriate variables with f-strings
    filename = f"{data[3]}{data[4]}_{data[1]}_{data[2]}"

    # Tries to write the data. If it is successful it will return true,
    # otherwise false

    try:
        f = open(f"{cwd}/data/{data[1]}/{filename}.fmt", "+w")
        f.write(';'.join(data))
        f.close()
        print(f"Created File {filename}")
        return True
    except OSError:
        print("Creating File Failed!")
        return False

while True:
    ret, frame = camera.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Scan Code', gray)

    cwd = os.getcwd()

    decodedCode = decode(frame)

    if decodedCode:
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
