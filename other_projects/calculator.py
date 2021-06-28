class Operation: 

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def add(self):
        
        return self.num1 + self.num2
    
    def minus(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2

def checkIfIsDigit(input):
    try:
        int(input)
        return True
    except ValueError:
        return False

list = ['+', '-', '*', '/']

input1 = 0
input2 = 0
operator = None

while True:
    input1 = input("Number 1: ")
    if checkIfIsDigit(input1) == False:
        print("Please input a number.")
        continue

    while True:
        operator = input("Please operator (+, -, *, /):")
        if operator not in list:
            print("Please input valid operator.")
            continue
        break

    while True:
        input2 = input("Number 2: ")
        if checkIfIsDigit(input2) == False:
            print("Please input a number.")
            continue
        break

    op = Operation(int(input1), int(input2))

    if operator == list[0]:
        print(f"{input1} {operator} {input2} =", op.add())

    if operator == list[1]:
        print(f"{input1} {operator} {input2} =", op.minus())

    if operator == list[2]:
        print(f"{input1} {operator} {input2} =", op.multiply())

    if operator == list[3]:
        print(f"{input1} {operator} {input2} =", op.divide())

    ask = input("Do you want to add again? yes/no: ")
    if ask == 'yes':
        continue
    else:
        print("Thank you for using this calculator bye!")
        quit()


