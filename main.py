# This is a simple calculator with functions to handle the math

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


while True:
    print("Simple Calculator - Enter a value")
    print("[1] add")
    print("[2] subtract")
    print("[3] multiply")
    print("[4] divide")
    print("[5] to quit")

    option = input("Enter option(1,2,3,4): ")

    if option in ('1', '2', '3', '4'):
        num1 = float(input("Enter the first value: "))
        num2 = float(input('Enter the second value:'))

    if option == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")

    if option == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")

    if option == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")

    if option == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")

    if option == '5':
        break
