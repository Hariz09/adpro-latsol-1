class Calculator:
    def add(self, add, b):
        return add + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a_new, b):
        return a_new * b
    
    def divide(self, a, b):
        return a / b
    
    def modulo(self, a, b):
        return a % b
    
    def power(self, a, b):
        return a ** b
    
if __name__ == "__main__":
    calc = Calculator()
    print("Addition: ", calc.add(10, 5))
    print("Subtraction: ", calc.subtract(10, 5))
    print("Multiplication: ", calc.multiply(10, 5))
    print("Division: ", calc.divide(10, 5))
    print("Modulo: ", calc.modulo(10, 5))
    print("Power: ", calc.power(10, 5))