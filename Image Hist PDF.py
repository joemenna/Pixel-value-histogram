import skimage.color
from PIL import Image, ImageFilter
import skimage.io
import skimage.viewer
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
import scipy




image = skimage.io.imread('lana.png')
data = np.ravel(image)
img = mpimg.imread('lana.png')
histogram, bin_edges = np.histogram(image, bins=256, range=(0, 255))

mean = round(np.mean(data), 1)
med = round(np.median(data),1)
mode = scipy.stats.mode(data)

ran = np.ptp(data)
variance = round(np.var(data), 1)
stddev = round(np.std(data), 1)

fig = plt.figure()
fig.add_subplot(221)
plt.imshow(image)
fig.add_subplot(222)
plt.title("Pixel Histogram")
plt.xlabel(f"Pixel value\n\nThe modal value is {mode.mode[0]} with a count of {mode.count[0]}\nThe mean is {mean}. The median is {med}\nVariance ={variance} Standard Deviation ={stddev}")
plt.ylabel('pixels')
plt.xlim([0.0, 255.0])
plt.plot(bin_edges[0:-1], histogram)


print(f"The modal value is {mode.mode[0]} with a count of {mode.count[0]}\nThe mean is {mean}. The median is {med}\nVariance ={variance} Standard Deviation ={stddev}")
plt.show()





