class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def addition(self):
        return self.num1 + self.num2
    
    def substract(self):
        return self.num1 - self.num2
    
    def product(self):
        return self.num1*self.num2
    
    def divide(self):
        return self.num1/self.num2

class Calculator2:
    def add(self, num1, num2):
        return num1 + num2
    
    def sub(self, x,y):
        return x - y
    
    def prod(self, x, y):
        return x*y
    
    def div(self, x, y):
        if y != 0 :
            return x/y
        else:
            return "Invalid"
calc = Calculator2()
print(calc.add(1,2))
print(calc.div(2,0))