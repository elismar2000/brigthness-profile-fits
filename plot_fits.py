from astropy.io import fits

import numpy as np
import matplotlib.pyplot as plt

import sys

#=================================

image_file      = sys.argv[1]
model_file      = sys.argv[2]

min             = sys.argv[3]
max             = sys.argv[4]

image = fits.getdata(image_file)
model = fits.getdata(model_file)

residual = image - model

#==================================
#plot
#==================================

distance = 39e+3 #Kpc

px_scale_GMOS_S = 0.073 / (60*60)
px_scale_NIC3 = 0.2 / (60*60)

extent_x = np.size(image, axis=0) * np.deg2rad(px_scale_NIC3) * distance
extent_y = np.size(image, axis=1) * np.deg2rad(px_scale_NIC3) * distance


norm = plt.Normalize(min, max)

cmap = 'Spectral'

fig, axs = plt.subplots(1, 3, sharey=True, figsize=(40, 40))
image0 = axs[0].imshow(image, cmap=cmap, origin='lower', norm=norm, extent=[0, extent_y, 0, extent_x])
axs[0].set_title('Image')
axs[0].set_ylabel('Kpc')
axs[0].set_xlabel('Kpc')

image1 = axs[1].imshow(model, cmap=cmap, origin='lower', norm=norm, extent=[0, extent_y, 0, extent_x])
axs[1].set_title('Model')
axs[1].set_xlabel('Kpc')

image2 = axs[2].imshow(residual, cmap=cmap, origin='lower', norm=norm, extent=[0, extent_y, 0, extent_x])
axs[2].set_title('Residual')
axs[2].set_xlabel('Kpc')

cbar = plt.colorbar(image2, fraction=0.044, pad=0.04)
cbar.ax.tick_params(labelsize=7)
cbar.set_label('Counts')
plt.show()
