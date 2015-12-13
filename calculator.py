class Calculator:
    def __init__(self):
        self.base_numeral_system = 10

    def add(self, x, y):
        """This function adds two numbers"""
        return x + y

    def subtract(self, x, y):
        """This function subtracts two numbers"""
        return x - y

    def multiply(self, x, y):
        """This function multiplies two numbers"""
        if x == 1:
            return y
        elif y == 1:
            return x
        else:
            return x * y

    def divide(self, x, y):
        """This function divides two numbers"""
        if y == 1:
            return x
        elif y == 0:
            raise ZeroDivisionError
        else:
            return x / y

    def evaluate(self, expression):
        """This function evaluate expression"""
        try:
            result = eval(expression)
        except:
            raise SyntaxError
        return result
