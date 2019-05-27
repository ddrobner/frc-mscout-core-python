class fileWriter:
    def __init__(self):
        pass

    def writeData(self, code):
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


