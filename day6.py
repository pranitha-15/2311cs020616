import pandas as pd

# Task 1: Creating the DataFrame
data = {
    'Name': ['John', 'Alice', 'Bob', 'Diana'],
    'Age': [28, 34, 23, 29],
    'Department': ['HR', 'IT', 'Marketing', 'Finance'],
    'Salary': [45000, 60000, 35000, 50000]
}

# Create the DataFrame
df = pd.DataFrame(data)

# Task 2: Display the first 2 rows of the DataFrame
print("First 2 rows of the DataFrame:")
print(df.head(2))  # Display the first 2 rows

# Add a new column 'Bonus' where the bonus is 10% of the salary
df['Bonus'] = df['Salary'] * 0.10

# Display the DataFrame with the new 'Bonus' column
print("\nDataFrame with the 'Bonus' column:")
print(df)

# Calculate the average salary of employees
average_salary = df['Salary'].mean()
print(f"\nThe average salary of employees is: {average_salary}")

# Filter and display employees who are older than 25
employees_over_25 = df[df['Age'] > 25]
print("\nEmployees older than 25:")
print(employees_over_25)
