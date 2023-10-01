import arithmetic_arranger
myList = []
print("Enter equation | Format: (num1 operator num2)\nPress (Enter) for exit")
while(True):
    myString = input("Enter Equation : ")
    if myString == "":
        break
    else:
        myList.append(myString)

arithmetic_arranger.arithmetic_arranger(myList)