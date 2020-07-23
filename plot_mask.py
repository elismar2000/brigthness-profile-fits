from astropy.io import fits

import numpy as np
import matplotlib.pyplot as plt

import sys

#=================================

image_file = sys.argv[1]
mask_file  = sys.argv[2]

min        = sys.argv[3]
max        = sys.argv[4]

image = fits.getdata(image_file)
mask = fits.getdata(mask_file)

image *= mask

#==================================
#plot
#==================================

norm = plt.Normalize(min, max)

plt.imshow(image, cmap='magma', origin='lower', norm=norm)
plt.colorbar()
plt.show()
