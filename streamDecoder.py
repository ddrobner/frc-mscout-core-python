class streamDecoder:
    dataArr = []
    codeArr = []
    qrHash = []

    # TODO Implement stream decoding

    def __init__(self):
        self.reset()

    def reset(self):
        self.dataArr = []
        self.codeArr = []
        self.qrHash = []
