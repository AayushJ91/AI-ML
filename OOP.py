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

class Shape:
    def area():
        pass
    def perimeter():
        pass
    def display():
        pass

class circle(Shape):
    def __init__(self, r):
        self.r = r
    
    def area(self):
        return 3.14*self.r**2
    def perimeter(self):
        return 6.28*self.r
    def display(self):
        print(f"the are is: {self.area()}")
        print(f"the perimeter is: {self.perimeter()}")
    
class Triangle(Shape):
    def __init__(self, h, b):
        self.h = h
        self.b = b
     
    def area(self):
        return 0.5*self.h*self.b
    def display(self):
        print(f"The area of triangle is: {self.area()}")

class Stack:
    def __init__(self):
        self.x = []
        
    def push(self,a):
        self.x.append(a)
    
    def pop(self):
        self.x.pop(len(self.x) - 1)
    
    def display(self):
        for i in range(len(self.x)):
            if i == len(self.x) - 1:
                print(f"{self.x[i]} <- top")
            else:
                print(self.x[i], end=" ")

st = Stack()
st.push(9)
st.push(8)
st.push(10)
st.push(78)
st.push(68)
st.display()
st.pop()
st.display()