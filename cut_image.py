from astropy.io import fits

import numpy as np

import sys

#============================

image_file = sys.argv[1]

image = fits.getdata(image_file)

#============================

def cut_image(image, x0, x1, y0, y1, output):
    '''
    Make a square cut on a fits image.
    Coordinates of the corners of the square
    are given by x0, x1, y0, y1
    '''
    image = image[x0:x1, y0:y1]
    hdu = fits.PrimaryHDU(image)
    hdu.writeto(output)

x0 = sys.argv[2]
x1 = sys.argv[3]
y0 = sys.argv[4]
y1 = sys.argv[5]
output = sys.argv[6]

x0 = int(x0)
x1 = int(x1)
y0 = int(y0)
y1 = int(y1)
output = str(output)

cut_image(image, x0, x1, y0, y1, output)

#==============================
