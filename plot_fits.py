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

distance = 39e+3 #Kpc

px_scale_GMOS_S = 0.073 / (60*60)
px_scale_NIC3 = 0.2 / (60*60)

extent_x = np.size(image, axis=0) * np.deg2rad(px_scale_NIC3) * distance
extent_y = np.size(image, axis=1) * np.deg2rad(px_scale_NIC3) * distance


norm = plt.Normalize(min, max)

fig, axs = plt.subplots(1, 3, sharey=True, figsize=(40, 40))
axs[0].imshow(image, cmap='magma', origin='lower', norm=norm, extent=[0, extent_y, 0, extent_x])
axs[0].set_title('Image')
axs[0].set_ylabel('Kpc')
axs[0].set_xlabel('Kpc')

axs[1].imshow(model, cmap='magma', origin='lower', norm=norm, extent=[0, extent_y, 0, extent_x])
axs[1].set_title('Model')
axs[1].set_xlabel('Kpc')

axs[2].imshow(residual, cmap='magma', origin='lower', norm=norm, extent=[0, extent_y, 0, extent_x])
axs[2].set_title('Residual')
axs[2].set_xlabel('Kpc')

plt.show()
