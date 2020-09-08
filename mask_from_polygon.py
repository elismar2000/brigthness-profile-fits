from astropy.io import fits

import numpy as np

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

import sys

#=================================

image_file = sys.argv[1]
mask_file  = sys.argv[2]

image = fits.getdata(image_file)

#==================================
#making a mask
#==================================

polygon = Polygon([(93, 45), (93, 50), (89, 50), (89, 45)])

for i in range(np.size(image, axis=0)):
    for j in range(np.size(image, axis=1)):
        print(i, j)
        point = Point(i, j)

        if polygon.contains(point):
            image[i, j] = 1
        else:
            image[i, j] = 0

hdu = fits.PrimaryHDU(image)
hdu.writeto(mask_file)
