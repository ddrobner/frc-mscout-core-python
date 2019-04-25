import zlib


class messageQR:

    percentage = 0
    hashMessageLength = -1
    iterations = 0
    targetNumber = 0
    lastIt = ""
    targetHash = ""
    hashData = ""
    data = ""
    codeHash = ""

    def __init__(self):
        self.clearMessage()

    def clearMessage(self):
        self.percentage = 0
        self.hashMessageLength = -1
        self.iterations = 0
        self.targetNumber = 0
        self.lastIt = ""
        self.targetHash = ""
        self.hashData = ""
        self.data = ""
        self.codeHash = ""

    def inputMessage(self, msg):
        iterations = 0
        lastIt = msg

        if msg != lastIt:
            print("Inputting Message...")

            iterations += 1
            print(f"Iterations: {iterations}")

            if self.hashMessageLength < 0 or self.hashMessageLength > len(msg):
                self.hashMessageLength = len(msg)

            if iterations >= 3:
                print(f"Length: {self.hashMessageLength}")
                if len(msg) > self.hashMessageLength:
                    self.inputData(msg)
                else:
                    self.inputHash(msg)

        if self.targetNumber != 0:
            self.percentage = (float(self.complete())) / (float((self.targetNumber * 2)))
            print(f"Percentage: {self.percentage}")

        return (self.hashData == self.targetHash) and (len(self.targetHash) == 8)

    def inputData(self, msg):
        temp = zlib.adler32(msg)
        print(f"Data Input: {msg} with a hash of {temp}")

        for i in range(0, len(self.codeHash) + 1):
            if temp == self.codeHash[i]:
                while len(self.data) < i + 1:
                    self.data += ""
            self.data[i] = msg

    def inputHash(self, msg):
        if msg.find("|") != -1:
            index = int(msg[:msg.find["|"]])
            tmpHash = msg[:msg.find["|"] + 1]

            while len(self.codeHash) < index + 1:
                self.codeHash = self.codeHash + ""
            self.codeHash[index] = tmpHash
        elif msg.find("-") != -1:
            self.targetNumber = int(msg[:msg.find["-"]])
            self.targetHash = msg[:msg.find("-") + 1]

    def hashData(self):
        concatData = ""
        i = 0

        while i < len(self.data):
            concatData = concatData + self.data[i]
            i += 1
        return zlib.adler32(concatData)

    def complete(self):
        ret = 0
        for i in range(len(self.codeHash) + 1):
            if len(self.codeHash) > 0:
                ret += 1
        for i in range(len(self.data) + 1):
            if len(self.data[i]) > 0:
                ret += 1
        return ret
