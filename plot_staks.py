from astropy.io import fits
import matplotlib.pyplot as plt

import sys

#=================================
image_file = sys.argv[1]

hdu_list = fits.open(image_file)

sci_data = hdu_list[1].data
dq_data = hdu_list[3].data

mask = dq_data == 0
sci_data *= mask

norm = plt.Normalize(0.0, 10000.0)

plt.imshow(sci_data, cmap='magma', origin='lower', norm=norm)
plt.colorbar()
plt.show()
