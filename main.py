def calculator():
    print("Simple CLI Calculator")
    while True:
        try:
            a = float(input("Enter first number: "))
            op = input("Enter operator (+, -, *, /): ")
            b = float(input("Enter second number: "))

            if op == '+':
                print("Result:", a + b)
            elif op == '-':
                print("Result:", a - b)
            elif op == '*':
                print("Result:", a * b)
            elif op == '/':
                print("Result:", a / b)
            else:
                print("Invalid operator")
        except Exception as e:
            print("Error:", e)

        cont = input("Continue? (y/n): ")
        if cont.lower() != 'y':
            break

calculator()
