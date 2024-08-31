def is_num_prime(num):#deremin the number is a prime number
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):#check if the num divisible by ant num from 2 up to the suqare root of the num
        if num % i == 0:
            return False
    return True

def is_num_pronic(num):#determin if the num is a pronic num
    for i in range(1, int(num**0.5) + 1):#start from 1 and chack if the product equal the given number
        if i * (i + 1) == num:
            return True
    return False

def main_choice(choice):
    if choice == '1':
        num = int(input("Enter a number to check if it's prime: "))
        print(f"{num} is {'a prime' if is_num_prime(num) else 'not a prime'} number.")
    elif choice == '2':
        num = int(input("Enter a number to check if it's pronic: "))
        print(f"{num} is {'a pronic' if is_num_pronic(num) else 'not a pronic'} number.")
    elif choice == '3':
        print("Exiting the program.")
        return False
    else:
        print("Invalid choice. Please try again.")
    return True

def show_menu():#1 check if num is prime #2 check if the num is pronic #2 exit the program
    while True:
        print("\nMenu:")
        print("1. Check if a number is prime")
        print("2. Check if a number is pronic")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if not main_choice(choice):
            break

show_menu()
