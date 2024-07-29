import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os

# Load the Lenna image
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(path)
lenna_filename = os.path.join(path, 'samples', 'lenna.bmp')
lenna_img = np.array(Image.open(lenna_filename))

# Load a national flag image (use a local file)
flag_filename = os.path.join(path, 'exercises', 'usa-flag.png')
flag_img = np.array(Image.open(flag_filename))

# Get Lenna image dimensions
lenna_height, lenna_width = lenna_img.shape[:2]

# Calculate new flag dimensions to fit in the top right corner
new_flag_width = lenna_width // 2  # Use half the width of Lenna image
new_flag_height = int(new_flag_width * flag_img.shape[0] / flag_img.shape[1])

# Ensure the new height doesn't exceed Lenna's height
if new_flag_height > lenna_height:
    new_flag_height = lenna_height
    new_flag_width = int(new_flag_height * flag_img.shape[1] / flag_img.shape[0])

# Resize flag image
flag_resized = np.array(Image.fromarray(flag_img).resize((new_flag_width, new_flag_height)))

# Create a copy of the Lenna image for modification
modified_lenna = lenna_img.copy()

# Replace the top right corner of Lenna image with the flag
modified_lenna[0:new_flag_height, -new_flag_width:] = flag_resized

# Display the modified Lenna image
plt.imshow(modified_lenna)
plt.axis('off')
plt.show()