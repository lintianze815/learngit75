import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
img = Image.open('test.jpg')
img_array = np.array(img)
fig, axs = plt.subplots(5, 1, figsize=(8,12))
axs[0].imshow(img)
axs[0].set_title("Original Image")
axs[1].hist(img_array.flatten(), bins=256, color='c')
axs[1].set_title("Full image histogram")
axs[2].hist(img_array[...,0].flatten(), bins=256, color='r', density=True)
axs[2].set_title("Red channel histogram")
axs[3].hist(img_array[...,1].flatten(), bins=256, color='g', density=True)
axs[3].set_title("Green channel histogram")
axs[4].hist(img_array[...,2].flatten(), bins=256, color='b', density=True)
axs[4].set_title("Blue channel histogram")
plt.tight_layout()
plt.savefig('origin_img_info.png')
brightness = 0.5
contrast = 1.5
mean = np.mean(img_array)
if len(img_array.shape) == 2:
    img_array = np.uint8(img_array * brightness)
    img_array = (img_array - mean)*contrast + mean
    img_array = np.clip(img_array,0,255)
else:
    img_array = np.uint8(img_array * brightness)
    for i in range(img_array.shape[2]):
        img_array[:,:,i] = (img_array[:,:,i]-mean)*contrast + mean
    img_array = np.clip(img_array,0,255)
new_img = Image.fromarray(img_array.astype('uint8'))
new_img.save('adjust_img.jpg')
# 绘制修改后直方图
fig2, axs2 = plt.subplots(5,1,figsize=(8,12))
axs2[0].imshow(new_img)
axs2[0].set_title("Adjusted Image")
axs2[1].hist(img_array.flatten(), bins=256, color='c')
axs2[1].set_title("Adjusted Full image histogram")
axs2[2].hist(img_array[...,0].flatten(), bins=256, color='r', density=True)
axs2[2].set_title("Adjusted Red channel histogram")
axs2[3].hist(img_array[...,1].flatten(), bins=256, color='g', density=True)
axs2[3].set_title("Adjusted Green channel histogram")
axs2[4].hist(img_array[...,2].flatten(), bins=256, color='b', density=True)
axs2[4].set_title("Adjusted Blue channel histogram")
plt.tight_layout()
plt.savefig('adjust_img_info.png')
plt.show()