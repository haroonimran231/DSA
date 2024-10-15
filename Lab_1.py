# celsius = 25
# fahrenheit = (celsius * 9/5) + 32
# print(f"{celsius}°C is {fahrenheit}°F")

# name = input("Enter your name: ") 
# age = input("Enter your age: ") 
# print(f"Hello {name}, you are {age} years old.")


# length = float(input("Enter the length: ")) 
# width = float(input("Enter the width: "))
# area = length * width
# print(f"The area of the rectangle is {area} square units.")

# 1. Write a program that performs all basic arithmetic operations between two numbers. 
# num_1=23
# num_2=2
# operators=input("Choose basic operator  `+`, `-`, `*`, `/`, `//`, `%`, `**`  ")
# if operators=="+":
#     print(num_1+num_2)
# elif operators=="-":
#     print(num_1-num_2)
# elif operators=="*":
#     print(num_1*num_2)
# elif operators=="/":
#     print(num_1/num_2)
# else:
#     print("choose correct operator")

# 2. Write a program that checks if a number is even or odd
# a = eval(input("Enter Any Number"))
# if a % 2 == 0 :
#     print("The Numnber is Even")
# else:
#     print("The Number is Odd")

# 3. Implement a simple calculator with addition, subtraction, multiplication, and division. 
# num_1=input("Enter a first no ")
# num_2=input("Enter a 2nd no ")
# operators=input("Choose basic operator  `+`, `-`, `*`, `/`, `//`, `%`, `**`  ")
# if operators=="+":
#     print(num_1+num_2)
# elif operators=="-":
#     print(num_1-num_2)
# elif operators=="*":
#     print(num_1*num_2)
# elif operators=="/":
#     print(num_1/num_2)
# else:
#     print("choose correct operator")

# a = int(input("Enter Any Integer"))

# if a>=0:
#     print("The Number is Positive")
# else:
#     print("The Number is Negative")

# 3. Write a program to determine the largest of three numbers. 
# a=int(input("Enter Any Integer"))
# b=int(input("Enter Any Integer"))
# c=int(input("Enter Any Integer"))
# if a>b and b>c:
#     print("a is greater")
# elif b>a and a>c:
#     print("b is greater")
# elif c>a and c>b:
#     print("c is greater")


# for i in range(1,11):
#     print(i)

# i=1
# sum=0
# n=int(input("enter ending number"))
# while(i<n):
#     sum=i+sum
#     print(sum)
#     i+=1

# n= int(input("Enter a number for table:"))
# for i in range(1,11):
#     print(n,"x",i,"=",i*10)


# n=int(input("enter a num for fibonacci:"))
# a=0
# b=1
# s=0
# for x in range(n):
#     print(s,end=" ")
#     s=a+b
#     b=a
#     a=s

# sum=0
# numbers=[1,2,3,4,5,6]
# for i in numbers:
#     sum=sum+i
#     print(sum)


# year =int(input("Enter a year"))
# if year%4==0 and (year%100!=0 or year%400==0):
#     print(year,"it is a leap year")
# else:
#     print(year,"it is not a leap year")


# n = 29  # Example number to check

# if n < 2:
#     print(f"{n} is not a prime number")
# else:
#     is_prime = True
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             is_prime = False
#             break
    
#     if is_prime:
#         print(f"{n} is a prime number")
#     else:
#         print(f"{n} is not a prime number")

# numbers = [10, 24, 36, 45, 12, 99, 54]  # Example list

# # Assume the first number is the largest
# largest = numbers[0]

# # Iterate through the list to find the largest number
# for num in numbers:
#     if num > largest:
#         largest = num

# print(f"The largest number in the list is: {largest}")


# Example list with duplicates
# numbers = [10, 24, 36, 45, 12, 99, 54, 24, 36, 99]

# # Convert the list to a set to remove duplicates
# unique_numbers = set(numbers)

# # Print the unique numbers
# print(unique_numbers)


# Example string
# text = "hello world"

# # Create an empty dictionary
# char_count = {}

# # Loop through each character in the string
# for char in text:
#     # Use the dictionary's get method to simplify incrementing
#     char_count[char] = char_count.get(char, 0) + 1

# # Print the dictionary containing character frequencies
# print(char_count)


# Specify the filename
# filename = 'example.txt'  # Change this to your file name

# # Open the file in read mode
# with open(filename, 'r') as file:
#     # Read the content of the file
#     content = file.read()

# # Display the content
# print(content)

# Specify the filename
# filename = 'user_input.txt'  # Change this to your desired file name

# # Open the file in write mode
# with open(filename, 'w') as file:
#     # Prompt the user for input
#     user_input = input("Please enter some text: ")
    
#     # Write the user input to the file
#     file.write(user_input)

# print(f"Your input has been written to {filename}.")

# filename = 'user_input.txt'  
# with open(filename, 'r') as file:
#     content = file.read()
# print(content)


# Specify the filename
# filename = 'user_input.txt'  # Change this to your file name

# # Open the file in read mode
# with open(filename, 'r') as file:
#     # Read all lines from the file
#     content = file.readlines()

# # Count lines
# line_count = len(content)

# # Count words and characters
# word_count = sum(len(line.split()) for line in content)
# char_count = sum(len(line) for line in content)

# # Display the counts
# print(f"Lines: {line_count}")
# print(f"Words: {word_count}")
# print(f"Characters: {char_count}")


# class Student:
#     def __init__(self, name, age):
#         self.name = name  # Attribute to store the student's name
#         self.age = age    # Attribute to store the student's age
#     def display(self):
#         # Method to print the student's information
#         print(f"Name: {self.name}, Age: {self.age}")
# # Example of creating a Student object and displaying its information
# student1 = Student("Alice", 20)
# student1.display()  # Output: Name: Alice, Age: 20


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2

#     def circumference(self):
#         return 2 * 3.14 * self.radius

# # Example usage
# circle = Circle(5)
# print("Area:", circle.area())           # Output: Area: 78.5
# print("Circumference:", circle.circumference())  # Output: Circumference: 31.4


# class BankAccount:
#     def __init__(self, account_number, balance=0):
#         self.account_number = account_number  # Store the account number
#         self.balance = balance                  # Initialize the balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount  # Add the amount to the balance
#             print(f"Deposited: ${amount:.2f}")
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount  # Subtract the amount from the balance
#             print(f"Withdrew: ${amount:.2f}")
#         else:
#             print("Insufficient funds or invalid amount.")

#     def get_balance(self):
#         return self.balance  # Return the current balance

# # Example usage
# account = BankAccount("12345678")
# account.deposit(100)                 # Deposit $100
# print("Current Balance:", account.get_balance())  # Output: Current Balance: 100
# account.withdraw(50)                 # Withdraw $50
# print("Current Balance:", account.get_balance())  # Output: Current Balance: 50
# account.withdraw(100)                # Attempt to withdraw more than the balance


# def calculator():
#     while True:
#         print("\nSimple Calculator")
#         print("1. Add")
#         print("2. Subtract")
#         print("3. Multiply")
#         print("4. Divide")
#         print("5. Exit")
        
#         choice = input("Select an operation (1-5): ")

#         if choice == '5':
#             print("Exiting the calculator. Goodbye!")
#             break
        
#         if choice in ['1', '2', '3', '4']:
#             num1 = float(input("Enter the first number: "))
#             num2 = float(input("Enter the second number: "))
        
#             if choice == '1':
#                 print(num1, num2)
#             elif choice == '2':
#                 print(num1, num2)
#             elif choice == '3':
#                 print(num1, num2)
#             elif choice == '4':
#                 print(num1, num2)
#         else:
#             print("Invalid input! Please select a valid option.")
# calculator()


# Open input file, process data, and write to output file
# with open('user_input.txt', 'r') as infile, open('user_input.txt', 'w') as outfile:
#     data = infile.read()               # Read data from input file
#     outfile.write(data.upper())        # Convert to uppercase and write to output file

# print("Data processed and written to output.txt.")
 


import random

def guess_number_game():
    number = random.randint(1, 100)  # Generate a random number between 1 and 100
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100.")
    
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

# Run the game
guess_number_game()
