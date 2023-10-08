You can convert an Excel file into a JSON file using the Pandas library in Python. Here's a step-by-step guide to do this:

Install Pandas and Openpyxl (if not already installed):
If you haven't already installed Pandas and the Openpyxl library, you can do so using pip:


pip install pandas openpyxl



Read the Excel File:
Use Pandas to read the Excel file and load it into a DataFrame. Make sure to specify the sheet name if your Excel file has multiple sheets.


import pandas as pd

# Replace 'your_excel_file.xlsx' with the path to your Excel file
df = pd.read_excel('your_excel_file.xlsx', sheet_name='Sheet1')



Convert DataFrame to JSON:
Use the to_json method of the DataFrame to convert it into a JSON string. You can customize the format and orientation of the JSON as needed.


# Convert DataFrame to JSON (orient 'records' for a list of dictionaries)
json_data = df.to_json(orient='records', indent=4)



Save JSON to a File:
Finally, you can save the JSON data to a file using Python's built-in file handling methods.

# Save JSON to a file (replace 'output.json' with your desired filename)
with open('output.json', 'w') as json_file:
    json_file.write(json_data)




Here's the complete code:
---------------------------




import pandas as pd

# Read the Excel file into a DataFrame
df = pd.read_excel('your_excel_file.xlsx', sheet_name='Sheet1')

# Convert the DataFrame to JSON
json_data = df.to_json(orient='records', indent=4)

# Save the JSON to a file
with open('output.json', 'w') as json_file:
    json_file.write(json_data)
