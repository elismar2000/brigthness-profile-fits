from astropy.io import fits

import numpy as np
import matplotlib.pyplot as plt

import sys

#=================================

image_file      = '/home/elismar/Documentos/Fisica/IC/imfit-1.7.1/ngc2992-93/images/NICMOS/n4sb08040/n4sb08040_mos_final_cut.fits'

model1          = '/home/elismar/Documentos/Fisica/IC/imfit-1.7.1/ngc2992-93/images/NICMOS/n4sb08040/model1.fits'
residual1       = '/home/elismar/Documentos/Fisica/IC/imfit-1.7.1/ngc2992-93/images/NICMOS/n4sb08040/residual1.fits'

model2          = '/home/elismar/Documentos/Fisica/IC/imfit-1.7.1/ngc2992-93/images/NICMOS/n4sb08040/model2.fits'
residual2       = '/home/elismar/Documentos/Fisica/IC/imfit-1.7.1/ngc2992-93/images/NICMOS/n4sb08040/residual2.fits'

model2          = '/home/elismar/Documentos/Fisica/IC/imfit-1.7.1/ngc2992-93/images/NICMOS/n4sb08040/model3.fits'
residual2       = '/home/elismar/Documentos/Fisica/IC/imfit-1.7.1/ngc2992-93/images/NICMOS/n4sb08040/residual3.fits'

min             = -2
max             = 2

image = fits.getdata(image_file)
model1 = fits.getdata(model1)
residual1 = fits.getdata(residual1)
model2 = fits.getdata(model2)
residual2 = fits.getdata(residual2)
model3 = fits.getdata(model3)
residual3 = fits.getdata(residual3)

#==================================
#plot
#==================================

norm = plt.Normalize(min, max)

fig, axs = plt.subplots(3, 3, sharey=True, figsize=(40, 40))
axs[0, 0].imshow(image, cmap='magma', origin='lower', norm=norm)
axs[0, 0].set_title('Image')

axs[0, 1].imshow(model, cmap='magma', origin='lower', norm=norm)
axs[0, 1].set_title('Model')

axs[0, 2].imshow(residual, cmap='magma', origin='lower', norm=norm)
axs[0, 2].set_title('Residual')
#===========================
axs[0, 0].imshow(image, cmap='magma', origin='lower', norm=norm)

axs[0, 1].imshow(model, cmap='magma', origin='lower', norm=norm)

axs[0, 2].imshow(residual, cmap='magma', origin='lower', norm=norm)
#==========================
axs[0, 0].imshow(image, cmap='magma', origin='lower', norm=norm)

axs[0, 1].imshow(model, cmap='magma', origin='lower', norm=norm)

axs[0, 2].imshow(residual, cmap='magma', origin='lower', norm=norm)

plt.show()
