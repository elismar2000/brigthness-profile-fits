from astropy.io import fits

import numpy as np
import matplotlib.pyplot as plt

import sys

#=================================

image_file      = sys.argv[1]
model_file      = sys.argv[2]
residual_file   = sys.argv[3]
min             = sys.argv[4]
max             = sys.argv[5]

image = fits.getdata(image_file)
model = fits.getdata(model_file)
residual = fits.getdata(residual_file)

#==================================
#plot
#==================================

norm = plt.Normalize(min, max)

fig, axs = plt.subplots(1, 3, sharey=True, figsize=(40, 40))
axs[0].imshow(image, cmap='magma', origin='lower', norm=norm)
axs[0].set_title('image')

axs[1].imshow(model, cmap='magma', origin='lower', norm=norm)
axs[1].set_title('model')

axs[2].imshow(residual, cmap='magma', origin='lower', norm=norm)
axs[2].set_title('residual')

plt.show()
