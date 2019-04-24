import zlib

class message:

    percentage = 0
    hashMessageLength = -1
    iterations = 0
    targetNumber = 0
    lastIt = ""
    targetHash = ""
    hashData = ""
    data = []
    codeHash = ""


    def message(self):
        self.clearMessage()

    def clearMessage(self):
        self.percentage = 0
        self.hashMessageLength = -1
        self.iterations = 0
        self.targetNumber = 0
        self.lastIt = ""
        self.targetHash = ""
        self.hashData = ""
        self.data = []
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
                    #TODO Placeholder need to implement inputData
                    print("placeholder inputData")
                else:
                    #TODO Placeholder need to implement inputHash
                    print("placeholder inputHash")

        if self.targetNumber != 0:
            #TODO need to implement complete
            print("Placeholder complete")
            print(f"Percentage: {self.percentage}")

        return (self.hashData() == self.targetHash) and (len(self.targetHash) == 8)

    def hashData(self):
        concatData = ""
        i = 0

        while i < len(self.data):
            concatData = concatData + self.data[i]
            i += 1
        return zlib.adler32(concatData)