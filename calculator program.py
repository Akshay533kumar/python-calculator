operator = input("enter your opprater(+,-,*,/): ")
num1 = int(input("enter your number: "))
num2 = int(input("enter your number: "))
if operator == "+" :
    result = num1+num2
    print(result)
elif operator == "-" :
    result = num1-num2
    print(result)
elif operator == "*" :
    result = num1*num2
    print(result)
elif operator == "/" :
    result = num1/num2
    print(result)
else :
    print(f"{operator}is not valid")
