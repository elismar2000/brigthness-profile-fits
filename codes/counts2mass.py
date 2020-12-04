#stdlib
import argparse

import matplotlib.pyplot as plt
import numpy as np
#third part
from astropy.io import fits


def counts2mag(image, magzp, ps):
    mag = magzp - (2.5 * np.log10(image))
    mag += 2.5 * np.log10(ps**2)
    return mag

def mag2abs_mag(mag, distance):
    d = distance * 1e+6
    abs_mag = mag - (2.5 * np.log10((d/10)**2)
    return abs_mag

def abs_mag2mass(image, magzp, ps, distance, solar_abs_mag, gama):
    '''
    Convert from source counts to absolute magnitude
    in the given passband, and then use a mass-to-light
    ratio to convert this magnitude to the relative
    stellar mass of the object

    Parameters
    ----------
    image : float or np.ndarray
        The object flux in units of source counts

    magzp : float
        The magnitude zero point for the given image

    ps : float
        The pixel scale for the give image

    distance : float
        The distance to the object. Needed to convert
        from apparent to absolute magnitude

    solar_abs_mag : float
        Solar absolute magnitude in the same filter band
        as the image

    gama : float
        The mass-to-light ratio, normalized to solar units
    '''
    mag = counts2mag(image, magzp, ps)
    abs_mag = mag2abs_mag(mag, distance)
    lum = 10**(-0.4*(abs_mag - solar_abs_mag))
    mass = gamma * lum
    return mass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', metavar='i', type=str, help='The image fits file')
    parser.add_argument('--magzp', metavar='magzp', type=float, help='The magnitude zero point')
    parser.add_argument('--pixel_scale', metavar='ps', type=float, help='The image pixel scale in arcsec/pixel')

    args = parser.parse_args()

    image = args.image
    magzp = args.magzp
    ps    = args.pixel_scale

    image = fits.getdata(image)

    mag = counts2mag(image, magzp, ps)
    abs_mag = mag2abs_mag(mag, 38)

    plt.imshow(abs_mag, cmap='terrain', origin='lower')
    cbar = plt.colorbar()
    cbar.set_label(r'$mag/arcsec^2$')
    plt.show()
