import pandas as pd
import random

# Sample data for student details
data = {
    'Name': ['Student 1', 'Student 2', 'Student 3', 'Student 4', 'Student 5'],
    'Age': [random.randint(18, 25) for _ in range(5)],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Female'],
    'Course': ['Mathematics', 'History', 'Physics', 'Chemistry', 'Biology'],
    'Roll Number': [random.randint(1001, 9999) for _ in range(5)]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Display the student details
print("Student Details:")
print(df)
