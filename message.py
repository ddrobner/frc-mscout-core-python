class message:

    percentage = 0
    hashMessageLength = -1
    iterations = 0
    targetNumber = 0
    lastIt = ""
    targetHash = ""
    hashData = ""
    data = ""
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



