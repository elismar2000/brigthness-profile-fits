from astropy.io import fits
from astropy.stats import sigma_clipped_stats

import numpy as np

import sys

#=================================

image_file     = sys.argv[1]
mask_file      = sys.argv[2]
residual_file  = sys.argv[3]

image    = fits.getdata(image_file)
residual = fits.getdata(residual_file)

mean, median, stddev = sigma_clipped_stats(image)
mask_threshold = -stddev

#==================================
#making a mask
#==================================

for i in range(np.size(residual, axis=0)):
    for j in range(np.size(residual, axis=1)):
        print(i, j)

        if residual[i, j] < mask_threshold:
            image[i, j] = 1
        else:
            image[i, j] = 0

hdu = fits.PrimaryHDU(image)
hdu.writeto(mask_file)
