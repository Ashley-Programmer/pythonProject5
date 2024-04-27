
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def quotient(x, y):
    if y == 0:
        return "Syntax Error!"
    else:
        return x / y

print("Do you either want to:")

print("")

print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')
print('5. Exit')

print("")

choice = input("Enter choice (1/2/3/4/5): ")

num1 = int(input('Enter num1: '))
num2 = int(input('Enter num2: '))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))

if choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))

if choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))

if choice == '4':
    print(num1, "/", num2, "=", quotient(num1, num2))

# else:
#     print('Invalid input!')