def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def calculator():
    print("=== Calculator ===")
    print("Operations: +  -  *  /")

    while True:
        a = float(input("\nEnter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        b = float(input("Enter second number: "))

        if op == '+':
            result = add(a, b)
        elif op == '-':
            result = subtract(a, b)
        elif op == '*':
            result = multiply(a, b)
        elif op == '/':
            result = divide(a, b)
        else:
            print("Invalid operator! Use +, -, *, /")
            continue

        print(f"Result: {a} {op} {b} = {result}")

        again = input("\nCalculate again? (yes/no): ").lower()
        if again != 'yes':
            print("Goodbye!")
            break

calculator()
