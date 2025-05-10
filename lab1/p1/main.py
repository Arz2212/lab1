from PIL import Image
import numpy as np


img = Image.open("lunar02_raw.jpg").convert("L")
img_array = np.array(img)
min_val = img_array.min()
max_val = img_array.max()
if max_val == min_val:
    stretched = np.zeros_like(img_array)
else:
    stretched = ((img_array - min_val) / (max_val - min_val) * 255).astype(np.uint8)
result_img = Image.fromarray(stretched)
result_img.save("moon_enhanced4.png")




