import os
from skimage import io
import numpy as np
from matplotlib import pyplot as plt

# Loading JPG file mask image for inspection
test_mask_pic = io.imread("Pic_7.JPG")
plt.imshow(test_mask_pic, cmap="gray")
# plt.show()
# print(np.unique(test_mask_pic))

# Let us load a numoy array saved from Label Studio
#  task-1-annotation-14-by-1-tag-road-0

# Lets up load a numpy array saved from Label Studio
test_mask_np = np.load("task-1-annotation-14-by-1-tag-road-0.npy")
plt.imshow(test_mask_np, cmap="gray")
# plt.show()
# print(np.unique(test_mask_np))

# Need to binarize the image. Simple thresholing for values above 0.
# Conver all values above 0 to 1 to assign a pixel value of 1 for the Houses class.
# Similary convert other values for other classes to 2, 3 ,etc.

my_mask = np.where(test_mask_pic > 0, 1, test_mask_pic)

plt.imshow(my_mask, cmap="gray")

# Now let us read images from all classes and change pixel values to 1, 2, 3, ...
# You can also combine them into a single image (numpy array) for simple handling in fut...
# (Chaning pixel values is optional if you do not intend to combine them into a single
# It is better to keep them separate, especially for multilabel segmentation
# where classes can overlap


# label_folder = "labels_as_jpg/ - наименование папки
road_masks = []
water_masks = []
all_mask = []

for filename in os.listdir("annotation image"): # - Получить список файлов в директории/каталоге
    if "road" in filename:
        print(filename)
        road_mask = io.imread(filename)
        road_mask = np.where(road_mask > 0, 1, road_mask)
        road_masks.append(road_mask)
    elif "water" in filename:
        print(filename)
        water_mask = io.imread(filename)
        water_mask = np.where(water_mask > 0, 2, water_mask)
        water_masks.append(water_mask)

for i in road_masks:
    print(i)




