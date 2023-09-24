import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Load an image
image = Image.open('sample.jpg')

# Convert the image to a NumPy array
img_array = np.array(image)

# Convert the image to grayscale
grayscale_array = np.mean(img_array, axis=2).astype(np.uint8)

# Display the grayscale image
plt.imshow(grayscale_array, cmap='gray')
plt.axis('off')
plt.show()
