from astropy.io import fits

import numpy as np
import matplotlib.pyplot as plt

import sys

#=================================

image_file      = sys.argv[1]
min             = sys.argv[2]
max             = sys.argv[3]

image = fits.getdata(image_file)

#==================================
#plot
#==================================

norm = plt.Normalize(min, max)

plt.imshow(image, cmap='magma', origin='lower', norm=norm)
plt.colorbar()
plt.title('image')

plt.show()
