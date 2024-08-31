x=int(input("Enter first number : "))
y=int(input("Enter second number : "))


for num in range (x,y+1):
    if num % 7==0 and num % 5==0:
        print(num," is divisible by 7 and 5 ")
    else:
        print("is't divisible by 7 and 5 ")
