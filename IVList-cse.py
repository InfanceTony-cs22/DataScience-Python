import pandas as pd
import random

# Function to generate random student data
def generate_student_data(n):
    data = {
        'StudentID': range(1, n + 1),
        'Name': ['Student' + str(i) for i in range(1, n + 1)],
        'Department': [random.choice(['CSE', 'MECH', 'CIVIL', 'EEE', 'ECE']) for _ in range(n)],
        'IV_Coming': [random.choice([True, False]) for _ in range(n)]
    }
    return data

# Number of students to generate
n = 50  # You can change this to generate data for any number of students

# Create a DataFrame with random student data
student_data = generate_student_data(n)
df = pd.DataFrame(student_data)

# Filter students who are coming for IV in the CSE department
cse_iv_students = df[(df['Department'] == 'CSE') & (df['IV_Coming'] == True)]

# Display the students coming for IV in the CSE department
print("Created by Infance Tony")
print("Students in CSE coming for IV:")
print(cse_iv_students[['StudentID', 'Name']])
