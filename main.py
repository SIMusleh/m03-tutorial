#oop subtraction

class Calculator:
  def __init__(self, num1, num2):
    self.num1 = num1
    self.num2 = num2
    
  def subtract(self):
      return self.num1 - self.num2

calc = Calculator(5, 2)
result = calc.subtract()
print(result) 

#functional paradigm subtraction

def subtract(num1, num2):
    return num1 - num2

result = subtract(5, 2)
print(result)

#oop division

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def divide(self):
        return self.num1 / self.num2

calc = Calculator(10, 2)
result = calc.divide()
print(result)

#functional paradigm division

def divide(num1, num2):
    return num1 / num2

result = divide(10, 2)
print(result)