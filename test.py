
# this is where i am importing dependencies to display image
from scipy import misc
import numpy as np

# this is how the image is displayed
image = misc.imread('ball.jpg', mode="L")

# this is where i add noise to the images
noisy1 = image + 3 * image.std() * np.random.random(image.shape)
alot = 2 * image.max() * np.random.random(image.shape)
noisy2 = image + alot

# this is how matplotlib plots the noisy image
import matplotlib.pyplot as plt
f, axarr = plt.subplots(2, 2)
axarr[0, 0].imshow(image,cmap = plt.get_cmap('gray'))
axarr[0, 0].set_title('Image gray')

axarr[0, 1].imshow(noisy1,cmap = plt.get_cmap('gray'))
axarr[0, 1].set_title('Image noise 1')

axarr[1, 0].imshow(noisy1,cmap = plt.get_cmap('gray'))
axarr[1, 0].set_title('Image noise 2')

axarr[1, 1].imshow(alot,cmap = plt.get_cmap('gray'))
axarr[1, 1].set_title('Added noise')

plt.show()
