from astropy.io import fits

import numpy as np
import matplotlib.pyplot as plt

import sys

#=================================

image1_file     = sys.argv[1]
image2_file     = sys.argv[2]
diff_image_file = sys.argv[3]

image1 = fits.getdata(image1_file)
image2 = fits.getdata(image2_file)

diff_image = image1 - image2

hdu = fits.PrimaryHDU(diff_image)
hdu.writeto(diff_image_file)
