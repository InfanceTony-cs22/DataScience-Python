#CALCULATING STUDENTS JOINED IN MY COLLEGE USING PANDAS IN PYTHON
import pandas as pd

# Sample student data with 'Department' column
data = {
    'StudentID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Student1', 'Student2', 'Student3', 'Student4', 'Student5', 'Student6', 'Student7', 'Student8', 'Student9', 'Student10'],
    'Department': ['CSE', 'MECH', 'CIVIL', 'EEE', 'CSE', 'ECE', 'CSE', 'MECH', 'EEE', 'CIVIL']
}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Calculate the number of students in each department
department_counts = df['Department'].value_counts()

# Display the results
print("STELLA MARYS COLLEGE OF ENGINEERING")
print("Number of students joined each department:")
print(department_counts)
