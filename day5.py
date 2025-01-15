#program 1:
# Task 1: Asking the user to input a positive integer
n = int(input("Enter a positive integer: "))

# Task 2: Printing numbers from 1 to n using a for loop
print("Numbers from 1 to", n)
for i in range(1, n + 1):
    print(i)

# Task 3: Calculating the sum of all numbers from 1 to n using a while loop
sum_of_numbers = 0
i = 1
while i <= n:
    sum_of_numbers += i
    i += 1

# Printing the sum of numbers from 1 to n
print("The sum of all numbers from 1 to", n, "is:", sum_of_numbers)


#program 2:

# Task 1: Defining the function to calculate square of a number
def calculate_square(n):
    return n ** 2

# Task 2: Main program to take user input and call the function
number = int(input("Enter a positive integer: "))

# Task 3: Calling the function and displaying the result
square = calculate_square(number)
print(f"The square of {number} is: {square}")
