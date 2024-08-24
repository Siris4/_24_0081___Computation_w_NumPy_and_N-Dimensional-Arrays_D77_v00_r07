import numpy as np
import matplotlib.pyplot as plt

# Create an image with different color channels
height, width = 100, 100
image_array = np.zeros((height, width, 3), dtype=np.uint8)

# Set the red channel to 255 in the top half
image_array[:height//2, :, 0] = 255  # Red

# Set the green channel to 255 in the bottom left quarter
image_array[height//2:, :width//2, 1] = 255  # Green

# Set the blue channel to 255 in the bottom right quarter
image_array[height//2:, width//2:, 2] = 255  # Blue

# Check if image_array is a NumPy ndarray
print("Type of image_array:", type(image_array))

# Display the shape and datatype
print("Shape of image_array:", image_array.shape)
print("Datatype of image_array:", image_array.dtype)

# Display the image
plt.imshow(image_array)
plt.axis('off')  # Turn off axis labels
plt.show()



# Type of image_array: <class 'numpy.ndarray'>
# Shape of image_array: (100, 100, 3)
# Datatype of image_array: uint8

