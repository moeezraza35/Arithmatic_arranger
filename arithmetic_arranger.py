def error(error_in):
    print(f"Syntax Error : \"{error_in}\"")

def is_oper_valid(oper):
    operators = ['+','-','*','/']
    if oper in operators:
        return True
    else:
        return False
    
def print_arrange(n1, op, n2, n3):
    max_len = 4
    myList = [str(n1), str(n2), str(n3)]
    for items in myList:
        if len(items) > max_len:
            max_len = len(items)
    
    for items in range(len(myList)):
        while len(myList[items]) <= max_len:
            myList[items] = ' ' + myList[items]
    
    myString = f"\n  {myList[0]}\n{op} {myList[1]}\n--"
    for x in range(max_len):
        myString += '-'
    myString += f"-\n  {myList[2]}\n"
    print(myString)

def arithmetic_arranger(myList):
    error_count = 0
    for equation in myList:
        if error_count == 5:
            print("Too many errors")
            break

        num1 = ""
        num2 = ""
        space=0
        oper = None
        error_out = 0
        for item in equation:
            if item != ' ' and space == 0:
                num1 += item
            elif item != ' ' and oper == None and space == 1:
                oper = item
            elif item != ' ' and space == 2:
                num2 += item
            elif space == 1 and num1 == "":
                error(equation)
                error_out = 1
                break
            elif space == 2 and oper == None:
                error(equation)
                error_out = 1
                break
            else:
                space += 1
        
        if error_out:
            error_count += 1
            continue
        
        try:
            num1 = int(num1)
        except ValueError:
            error(equation)
            error_count += 1
            continue
        
        try:
            num2 = int(num2)
        except ValueError:
            error(equation)
            error_count += 1
            continue

        if not is_oper_valid(oper):
            error(equation)
            error_count += 1
            continue
        else:
            if oper == '+':
                num3 = num1 + num2
            elif oper == '-':
                num3 = num1 - num2
            elif oper == '*':
                num3 = num1 * num2
            else:
                num3 = num1 / num2

        if len(str(num1)) < 5 or len(str(num2)) < 5 or len(str(num3)) < 5:
            print_arrange(num1, oper, num2, num3)
        else:
            print(f"Limit Error : in {equation}\nDigits of number can be 4 maximum")
            error_count += 1
