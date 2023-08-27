class PARTICION():
    
    def __init__(self):
        self.part_status = "\0"
        self.part_type = "\0"
        self.part_fit = "\0"
        self.part_start = 0
        self.part_s = 0
        self.part_name = "\0" * 16
        self.constanteParticion = '3c 2I 16C'

    def set_valores(self,part_status,part_type,part_fit,part_start,part_s,part_name):
        self.part_status = part_status
        self.part_type = part_type
        self.part_fit = part_fit
        self.part_start = part_start
        self.part_s = part_s
        self.part_name = part_name
    
    def doSerialize(self):#esto es lo que escribire en el archivo binario
        nuevaParticion = struct.pack(
            self.constanteParticion,
            self.part_status,
            self.part_type,
            self.part_fit,
            self.part_start,
            self.part_s,
            self.part_name
        )
        return nuevaParticion
    
    def doDeserialize(self, data):
        partSize = struct.calcsize(self.constanteParticion)
        datoBinarioParticion = data[:partSize]
        self.part_status, self.part_type, self.part_fit, self.part_start, self.part_s, self.part_name = struct.unpack(self.constanteParticion, datoBinarioParticion)
        