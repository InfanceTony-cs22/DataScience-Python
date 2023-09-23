# MOBILE DETAILS USING PANDA LIBRARY FUNCTION
import pandas as pd
import random

# Sample data for mobile phones in INR
data = {
    'Brand': ['Apple', 'Samsung', 'Google', 'OnePlus', 'Xiaomi'],
    'Model': ['iPhone X', 'Galaxy S21', 'Pixel 6', 'OnePlus 9 Pro', 'Mi 11'],
    'Price (INR)': [random.randint(20000, 100000) for _ in range(5)],
    'Specifications': [
        '6.1" OLED, 128GB storage, Dual-camera',
        '6.2" AMOLED, 256GB storage, Triple-camera',
        '6.0" OLED, 128GB storage, Dual-camera',
        '6.7" Fluid AMOLED, 256GB storage, Quad-camera',
        '6.81" AMOLED, 128GB storage, Triple-camera'
    ]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Display the mobile phone details
print("Mobile Phone Details:")
print(df)
