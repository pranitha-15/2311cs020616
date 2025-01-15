def sum_of_even_numbers(n):
    # Initialize the sum to 0
    total = 0
    
    # Loop through all numbers from 1 to n
    for i in range(2, n+1, 2):
        total += i
    
    return total

# Input: a positive integer n
n = int(input("Enter a positive integer: "))

# Call the function and print the result
result = sum_of_even_numbers(n)
print(f"The sum of all even numbers between 1 and {n} is: {result}")
