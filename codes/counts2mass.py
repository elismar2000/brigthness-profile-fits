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
    abs_mag = mag - (2.5 * np.log10((d/10)**2))
    #abs_mag = (2.5 * np.log10((d/10)**2)) - mag
    return abs_mag

def abs_mag2mass(image, magzp=20.4107, ps=1.0, distance=39, solar_abs_mag=3.3, gamma=1.0):
    '''
    Convert from source counts to absolute magnitude
    in the given passband, and then use a mass-to-light
    ratio to convert this magnitude to the relative
    stellar mass of the object in solar units

    Parameters
    ----------
    image : float or np.ndarray
        The object flux in units of source counts

    magzp : float
        The magnitude zero point for the given image

    ps : float
        The pixel scale for the given image

    distance : float
        The distance to the object in Mpc

    solar_abs_mag : float
        Solar absolute magnitude in the same filter band
        as the image

    gamma : float
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
    parser.add_argument('--distance', metavar='d', type=float, help='Distance to the object in Mpc')
    parser.add_argument('--solar_abs_mag', metavar='sam', type=float, help='Solar absolute magnitude in \
    the same filter band as the image')
    parser.add_argument('--gamma', metavar='gamma', type=float, help='The mass-to-light ratio')

    args = parser.parse_args()

    image = args.image
    magzp = args.magzp
    ps    = args.pixel_scale
    d     = args.distance
    sam   = args.solar_abs_mag
    gamma = args.gamma

    image = fits.getdata(image)

#============================================

    mag = counts2mag(image, magzp, ps)
    abs_mag = mag2abs_mag(mag, 38)

    plt.imshow(abs_mag, cmap='terrain', origin='lower')
    cbar = plt.colorbar()
    cbar.set_label(r'$mag/arcsec^2$')
    plt.show()

#============================================

    mass = abs_mag2mass(image, magzp, ps, d, sam, gamma)
    total_mass = np.sum(mass)

    print('The total stellar mass of this component in solar masses is {:e}'.format(total_mass))
