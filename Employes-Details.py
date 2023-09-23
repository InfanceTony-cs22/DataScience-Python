#employe details
import pandas as pd

# Sample data for employee details
data = {
    'Employee ID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [30, 28, 35, 25, 32],
    'Department': ['HR', 'IT', 'Sales', 'Finance', 'Marketing'],
    'Salary': [55000, 60000, 48000, 75000, 52000],
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Display the employee details
print("Employee Details:")
print(df)
