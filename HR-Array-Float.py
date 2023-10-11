import numpy as np
np.set_printoptions(legacy='1.13')

# Read input values
n, m = map(int, input().split())

# Create the desired N X M array with 's on the main diagonal
x_array = np.eye(n, m)

# Print the N X M array
print(x_array)
