class ComplexNumber:

    real = 0 
    imaginary = 0
    
    # Define constructor here
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary


    def add(self, x: "ComplexNumber"):
        # Complete the function
        m = self.real+x.real
        n = self.imaginary + x.imaginary
        return ComplexNumber(m,n)
    
    # x: "ComplexNumber" type of x
    #->"ComplexNumber" return type
    def subtract(self, x: "ComplexNumber")->"ComplexNumber":
        # Complete the function
        #(a+ib)-(c+id) = (a-c) + i(b-d)
        m = self.real - x.real
        n = self.imaginary - x.imaginary
        return ComplexNumber(m,n)
        
        
    def multiply(self, x: "ComplexNumber")->"ComplexNumber":
        # Complete the function
        #(a+ib)*(c+id) = (a*c-b*d)+i(b*c+a*d)
        m = (self.real*x.real)-(self.imaginary*x.imaginary)
        n = (self.imaginary*x.real)+(self.real*x.imaginary)
        return ComplexNumber(m,n)
    
    def divide(self, x: "ComplexNumber")->"ComplexNumber":
        # Complete the function
        #(a+ib)*(c+id) = ((a*c + b*d) + i(bc-ad) / (c**2 + d**2))
        denominator = (x.real*x.real) + (x.imaginary*x.imaginary)
        m = ((self.real*x.real) + (self.imaginary*x.imaginary))/denominator
        n = ((self.imaginary*x.real) - (self.real*x.imaginary))/denominator
        
        return ComplexNumber(m,n)
        

    
        
a =  ComplexNumber(10, 5)
b =  ComplexNumber(2, 3)
c1 = a.add(b) 
# c2 = a.subtract(b)
# c3 = a.multiply(b)
c4 = a.divide(b)
print(c1)