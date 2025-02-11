'''class Computer:
    def __init__(self):
        print("i am init method of computer class")

comp1=Computer()#calls the init method      
comp2=Computer()'''


class Computer:
    def __init__(self,brand,ram,rom):
        self.brand = brand
        self.ram = ram
        self.rom = rom
        
    def info(self):
        print(self.brand, self.ram, self.rom)

comp1 = Computer('dell', '15gb', '1tb')#calls the init method      
comp2 = Computer('hp', '16gb', '512tb')
comp1.brand='lenovo'

comp1.info()
comp2.info()
