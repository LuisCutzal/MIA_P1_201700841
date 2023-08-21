import ctypes
import struct
from utilities import coding_str

const = 'I 50s 2s 1s' #3 enteros sin signo, formato que se utilizara

class MKDISK(ctypes.Structure):
    __fields__ = [
        ('size', ctypes.c_int),
        ('path', ctypes.c_char * 50),
        ('fit', ctypes.c_char * 2 ),
        ('unit', ctypes.c_char * 1)
    ]
    
    def __init__(self):
        self.size = 0
        self.path = b'\0' * 50
        self.fit = b'\0' * 2
        self.unit = b'\0' * 1
      
    def set_size(self, size):
        self.size = size

    def set_path(self, path):
        self.path = coding_str(path, 50)

    def set_fit(self, fit):
        self.fit = coding_str(path, 2)
    
    def set_unit(self, unit):
        self.unit = coding_str(unit,1)

    def set_infomation(self, size, path, fit, unit):
        self.set_size(size)
        self.set_path(path)
        self.set_fit(fit)
        self.set_unit(unit)
    
    def display_info(self):
        print(f"size: {self.size}")
        print(f"path: {self.path.decode()}")
        print(f"fit: {self.fit.decode()}")
        print(f"unit: {self.unit.decode()}")

    def doSerialize(self):
        return struct.pack(
            const,
            self.size,
            self.path,
            self.fit,
            self.unit
        )

    def doDeserialize(self, data):
        self.size, self.path, self.fit, self.unit = struct.unpack(const, data)