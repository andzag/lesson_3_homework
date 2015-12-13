from calculator import Calculator

calc = Calculator()

while True:
    print("Menu1:\n"
          "1. Simple operation\n"
          "2. Evaluate\n"
          "0. Exit\n")

    action1 = input("Select one option: ")

    if action1 == '0':
        break

    elif action1 == '2':
        expression = input("Enter the expression: ")
        try:
            result = calc.evaluate(expression)
        except SyntaxError:
            print("Error: Entered incorrect expression.\n")
            continue
        print("Result: ", result)

    elif action1 == '1':
        print("Menu2: \n"
        "1. Add\n"
        "2. Subtract\n"
        "3. Multiply\n"
        "4. Divide\n"
        "5. Go to the Menu1\n")

        action2 = input("Select one option: ")

        if action2 == '5':
            continue
        elif action2 in ('1', '2', '3', '4'):
            try:
                number1 = input("Enter first number: ")
                number1 = float(number1)
            except ValueError:
                print("Error: Entered incorrect first number")
                continue
            try:
                number2 = input("Enter second number: ")
                number2 = float(number2)
            except ValueError:
                print("Error: Entered incorrect second number")
                continue

            if action2 == '1':
                result = calc.add(number1, number2)
            if action2 == '2':
                result = calc.subtract(number1, number2)
            if action2 == '3':
                result = calc.multiply(number1, number2)
            if action2 == '4':
                try:
                    result = calc.divide(number1, number2)
                except ZeroDivisionError:
                    print("Error: Division by zero")
                    continue
        else:
            continue

        print("Result: ", result)
    else:
        continue