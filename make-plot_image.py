from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

import os
import subprocess
import sys

#==============================

image = sys.argv[1] #The original image
config = sys.argv[2] #Config file to generate the model

subprocess.run(['/home/elismar/Documentos/Fisica/IC/imfit-1.7.1/makeimage', config, '--refimage',
    image, '-o', 'modelimage.fits', '--psf', 'star.fits'], check=True)

model = os.path.join('modelimage.fits')

image = fits.getdata(image)
model = fits.getdata(model)
resid = image - model

hdu = fits.PrimaryHDU(resid)
hdu.writeto('residual.fits', overwrite=True)

#==============================

conf = np.genfromtxt(config)
I0 = conf[5, 1]
h = conf[6, 1]
Ie = conf[11, 1]
re = conf[12, 1]
I0_PS = conf[16, 1]

norm = plt.Normalize(-2, 5)
cmap = 'twilight'

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True, figsize=(40, 40))
ax1.imshow(image, cmap=cmap, origin='lower', norm=norm)
ax1.set_title('Image', fontsize=20)

ax2.imshow(model, cmap=cmap, origin='lower', norm=norm)
# axs[1].text(10, 50, 'I0: %1.2f' %I0)
# axs[1].text(10, 40, 'h: %1.2f' %h)
# axs[1].text(10, 30, 'Ie: %1.2f' %Ie)
# axs[1].text(10, 20, 're: %1.2f' %re)
# axs[1].text(10, 10, 'I0_PS: %1.2f' %I0_PS)
ax2.set_title('Model', fontsize=20)

resid_plot = ax3.imshow(resid, cmap='Spectral', origin='lower', norm=plt.Normalize(-5, 5))
ax3.set_title('Residual', fontsize=20)

for ax in [ax1, ax2, ax3]:
    ax.tick_params(axis='both', which='both', tickdir='in', labelsize=15, width=1.5)
    ax.set_xlabel('px', fontsize=15)
    ax.set_ylabel('px', fontsize=15)

plt.colorbar(resid_plot, cax=ax)
plt.show()
