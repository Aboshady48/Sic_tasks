def add_calc (num1=0,num2=0):
    num1=float(input("enter your frst num: "))
    num2=float(input("enter your second num: "))
    result=(num1+num2)
    return print(result)

def mult_calc(num1=0,num2=0):
    num1=float(input("enter your frst num: "))
    num2=float(input("enter your second num: "))
    result=(num1*num2)
    return print(result)
    

def div_calc(num1=0,num2=0):
    num1=float(input("enter your frst num: "))
    num2=float(input("enter your second num: "))
    try:
        div=num1/num2
    except:
        print("wrong")
    
#this was an recursion functions and it's works
'''
def multi_calc (num1,num2):#recursion
    
    if num1 ==0 or num2 ==0:
        return 0
    return num1 + mult_calc(num1,num2-1)

def divdi_calc(num1,num2):#recursion
    base=0
    if num1<num2:
        return base
    else:
        base+=1
        return divd_calc(num1-num2,num2)
    return base

def rec (a,b):
    a=input()
    b=input()
    multi_calc(a,b)
'''
    
def calc (user=0):
    print("addtion two num press 1: ")
    print("Multiply two num press 2: ")
    print("divided two num press 3: ")
    user=int(input(" press 1 , 2 or 3:  "))
    if user == 1:
        add_calc()
        return add_calc()
    elif user == 2:
        return mult_calc()
    elif user == 3:
        return div_calc()
    else:
        print("you had chosse the wrong opration :) ")
        
calc()
#rec()
