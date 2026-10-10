print

def add():
    num1 = float(input("Enter a number: ").strip())
    num2 = float(input("Enter the other number: ").strip())
    result = num1 + num2
    print(f"{num1} + {num2} = {result} \n")

def subtract():
    num1 = float(input("Enter a number: ").strip())
    num2 = float(input("Enter another number: ").strip())
    result = num1 - num2
    print(f"{num1} - {num2} = {result} \n")

def multiply():
    num1 = float(input("Enter a number: ").strip())
    num2 = float(input("Enter another number: ").strip())
    result = num1 * num2
    print(f"{num1} * {num2} = {result} \n")

def divide():
    num1 = float(input("Enter a number: ").strip())
    num2 = float(input("Enter another number: ").strip())
    result = num1 / num2
    print(f"{num1} / {num2} = {result:.2f} \n")

def exponent():
    num1 = float(input("Enter a number: ").strip())
    num2 = float(input("Enter another number: ").strip())
    result = num1 ** num2
    print(f"{num1} raised to the power of {num2} = {result} \n")

print ("\t \t - - - - M E N U - - - - ")
print(" 1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide \n 5. Exponent \n 6. End \n ")
while True:
    try:
        action = int(input("Enter a command: "))
        match action:
            case 1:
                add()
            case 2:
                subtract()
            case 3:
                multiply()
            case 4:
                divide()
            case 5:
                exponent()
            case 6:
                print('Exitting. . .')
                break
            case _:
                print('Enter a valid integer for command \n')
    except ValueError:
        print("Enter a valid integer \n")
    except ZeroDivisionError:
        print("Undefined \n")
