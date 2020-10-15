#stdlib
from __future__ import print_function
import argparse

import numpy as np
#third part
from astropy.io import fits

#=======================
#Parsing arguments
#=======================
parser = argparse.ArgumentParser()
parser.add_argument('--image', metavar='i', type=str, help='The image fits file')
parser.add_argument('--magzp', metavar='magzp', type=float, help='The magnitude zero point')

args = parser.parse_args()

image = args.image
magzp = args.magzp

#========================
#Performing conversion
#========================
image = fits.getdata(image)

flux = np.sum(image)
mag = magzp - (2.5 * np.log10(flux))

print("This image total magnitude on its filter is: ", mag)
