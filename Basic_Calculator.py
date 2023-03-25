""" Basic Calulator
By Stuarrt Boekelman 3/23/2023
This is a console program that will take input for two numbers and ask the
user if they want to add, subtract, multiply, divide, square or raise thier
numbers then proform said calulation and output the result."""

# Error 01 is an unexpected error, that shouldn't occur but acts as a placeholder 

def addNums(numOne, numTwo):
   answer = numOne+numTwo
   print(f"Your numbers added and rounded 5 decimal places are {answer:.5f}")

def subNums(numOne, numTwo):
    answer = numOne - numTwo
    print(f"Your numbers subtracted and rounded 5 decimal places are {answer:.5f}")

def multNums(numOne, numTwo):
    answer = numOne*numTwo
    print(f"Your numbers multiplied and rounded 5 decimal places are {answer:.5f}")

def divNums(numOne, numTwo):
    if numTwo == 0:
        print("Can't divide by zero")
    else:
        answer = numOne/numTwo
        print(f"Your numbers divided and rounded 5 decimal places are {answer:.5f}")

def main():
    endProgram = ""
    while endProgram != "q":
        firstNum = input("Please enter the first number for your calulation: ")
        secondNum = input("Please enter the second number for your calculation: ")
        if firstNum.isnumeric() and secondNum.isnumeric():
            firstNum  = float(firstNum)
            secondNum = float(secondNum)
            editNumOne = input("Is the first number raised to a power? Type (y) or (n): ")
            editNumOne = editNumOne.lower()
            if editNumOne == "y":
                power = input("What power is your number raised to: ")
                firstNum = firstNum ** float(power)
            elif editNumOne == "n":
                if firstNum <= 0:
                    pass
                else:
                    squareRoot = input("Do you want to use the square root of your number? Type (y) or (n): ")
                    squareRoot = squareRoot.lower()
                    if squareRoot == "y":
                        firstNum = firstNum**.5
                    elif squareRoot == "n":
                        pass
                    else:
                        print("Did you type (y) or (n)?")
            else:
                print("Did you type (y) or (n)?")
            editNumTwo = input("Is the second number raised to a power? Type (y) or (n): ")
            editNumTwo = editNumTwo.lower()
            if editNumTwo == "y":
                power = input("What power is your number raised to: ")
                secondNum = secondNum ** float(power)
            elif editNumTwo == "n":
                if secondNum <= 0:
                    pass
                else:
                    squareRoot = input("Do you want to use the square root of your number? Type (y) or (n): ")
                    squareRoot = squareRoot.lower()
                    if squareRoot == "y":
                        secondNum = secondNum**.5
                    elif squareRoot == "n":
                        pass
                    else:
                        print("Did you type (y) or (n)?")
            else:
                print("Did you type (y) or (n)?")
            print("Please make a choice from the follwing:\n")
            print("1 - Add\n")
            print("2 - Subtract\n")
            print("3 - Multiply\n")
            print("4 - Divide\n")
            calcChoice = input("Please enter your choice here: ")
            while not calcChoice.isnumeric() or not (1 <= int(calcChoice) <= 4):
                print("Your entry was non-numeric or not within range of the choices.\n")
                calcChoice = input("Please enter your choice here: ")
            calcChoice = int(calcChoice)
            if calcChoice == 1:
                addNums(firstNum, secondNum)
            elif calcChoice == 2:
                subNums(firstNum, secondNum)
            elif calcChoice == 3:
                multNums(firstNum, secondNum)
            elif calcChoice == 4:
                divNums(firstNum, secondNum)
            else:
                print("Error: 01")
        else:
            print("Sorry one or more of your inputs is non numeric, try again.")
        endProgram = input("Do you want to preform another calculation? Type (q) to quit: ")
        endProgram = endProgram.lower()

main()