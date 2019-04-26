import ctypes

class adler32hash:

    MOD_ADLER = ctypes.c_uint32(0)

    def __init__(self):
        self.MOD_ADLER = ctypes.c_uint32(65521)

    def hashInput(self, input):
        self.MOD_ADLER = ctypes.c_uint32(65521)

        a, b = ctypes.c_uint32(1), ctypes.c_uint32(0)

        for x in input:
            a = (a + x) % self.MOD_ADLER
            b = (b + a) % self.MOD_ADLER

        ret = ctypes.c_uint32((b << 16) or a)
        return hex(ret)


