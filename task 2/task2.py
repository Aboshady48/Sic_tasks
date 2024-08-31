import random
import math
#first type the range of the num
first_num=int(input("Guess the first number between 1 to 100: "))
Second_num=int(input("Guess the second number between 1 to 100: "))

#making the rondom value
user=random.randint(first_num,Second_num)
# Initializing the number of guesses.
count = 0
while count <= Second_num:
    count += 1
    #taling the guess number
    guess=int(input("Guess a number:- "))
    
    if user==guess:
        print("Congratulations total try = ",count)
        break
    elif user>guess:
        print("Lower!")
    elif user<guess:
        print("Higher!")
