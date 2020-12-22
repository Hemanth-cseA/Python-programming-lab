class Complex:
    def __init(self):
        self.real = 0
        self.imag = 0
    def setValue(self , real, imag):
        self.real = real
        self.imag = imag
    def __add__(self, C):
        Temp = Complex()
        Temp.real =  self.real + C.real
        Temp.imag =  self.imag + C.imag
        return Temp
    def display(self):
        print("(", self.real, " + " , self.imag, "i)")
C1 = Complex()
C1.setValue(1,2)
C2 = Complex()
C2.setValue(3,4)
C3 = Complex()
C3 = C1 + C2
print("RESULT = ")
C3.display()
