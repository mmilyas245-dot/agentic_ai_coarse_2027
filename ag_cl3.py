def calculator(num1,op,num2):
    
    if op=="/":
        print(num1/num2)
    elif op=="*":
        print(num1*num2)
    elif op=="+":
        print(num1+num2)
    elif op=="-":
        print(num1-num2)
    else:
        pass
num1=int(input("enter num1:"))
op=input("enter operation : /*+-")
num2=int(input("enter num2:"))
calculator(num1,op,num2)
