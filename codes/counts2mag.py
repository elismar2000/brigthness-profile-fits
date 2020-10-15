#stdlib
import argparse

import matplotlib.pyplot as plt
import numpy as np
#third part
from astropy.io import fits

#=======================
#Parsing arguments
#=======================
parser = argparse.ArgumentParser()
parser.add_argument('--image', metavar='i', type=str, help='The image fits file')
parser.add_argument('--magzp', metavar='magzp', type=float, help='The magnitude zero point')
parser.add_argument('--pixel_scale', metavar='ps', type=float, help='The image pixel scale in arcsec/pixel')

args = parser.parse_args()

image = args.image
magzp = args.magzp
ps    = args.pixel_scale

#========================
#Performing conversion
#========================
image = fits.getdata(image)

mag = magzp - (2.5 * np.log10(image))
mag /= ps**2

# #só um improviso pra mudar de H pra Ks:
# mag -= 1.1275

plt.imshow(mag, cmap='terrain', origin='lower')
cbar = plt.colorbar()
cbar.set_label(r'$mag/arcsec^2$')
plt.show()
