import pandas as pd

# Load data from a CSV file into a DataFrame
data = pd.read_csv('sample_data.csv')  # Replace 'sample_data.csv' with your CSV file

# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(data.head())

# Display basic statistics of numeric columns
print("\nSummary statistics:")
print(data.describe())

# Filter data based on a condition
young_employees = data[data['Age'] < 30]
print("\nYoung employees:")
print(young_employees)

# Group and aggregate data
average_salary_by_age = data.groupby('Age')['Salary'].mean()
print("\nAverage salary by age:")
print(average_salary_by_age)
