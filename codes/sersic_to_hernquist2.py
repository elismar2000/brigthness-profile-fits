import abel
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

from photutils.isophote import EllipseGeometry, Ellipse

#=======================
#Performing the inverse Abel transformation over the bulge 2D image
#=======================

#This must be a 2D model image of the bulge to be transformed
image = 'image'
image = fits.getdata(image)

#The center pixel coordinates of the bulge
x0 = 15
y0 = 16
bulge_3D = abel.Transform(image, direction='inverse', method='three_point', center=(y0, x0)).transform

#=======================
#Fitting ellipses to the 3D image in order to get its brigthness profile
#=======================

geometry = EllipseGeometry(x0=14, y0=14, sma=2, eps=0.07, pa=0)

ellipse = Ellipse(bulge_3D, geometry)
isolist = ellipse.fit_image()

#========================
#Plot results
#========================

fig, (ax1, ax2) = plt.subplots(figsize=(14, 5), nrows=1, ncols=2)
norm = plt.Normalize(-2, 2)
ax1.imshow(bulge_3D, origin='lower', norm=norm)
ax1.set_title('Data')

smas = np.linspace(1, 10, 5)
for sma in smas:
    iso = isolist.get_closest(sma)
    x, y, = iso.sampled_coordinates()
    ax1.plot(x, y, color='white')

ax2.plot(isolist.sma, isolist.intens, color='purple', marker='x')
ax2.set_xlabel(r'$sma\ [pixel]$')
ax2.set_ylabel(r'$countrate\ [DN\ sec^{-1}]$')
ax2.set_title('Brigthness Profile')

plt.show()
