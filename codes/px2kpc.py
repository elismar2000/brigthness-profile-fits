from __future__ import print_function
import argparse
import numpy as np


def px2kpc(q, ps=1.0, distance=39):
    ps *= (1/3600) * np.pi/180 #from arcsecs to radians
    distance *= 1e+3 #distance from Mpc to Kpc
    q *= ps * distance
    return q


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--pixel_scale', metavar='ps', type=float, help='The image pixel scale in arcseconds')
    parser.add_argument('--quantity', metavar='q', type=float, help='The physical quantity to be converted, in px')
    parser.add_argument('--distance', metavar='d', type=float, help='Distance to the object in Mpc')

    args = parser.parse_args()

    ps = args.pixel_scale
    q  = args.quantity
    d  = args.distance

    q = px2kpc(q, ps, d)

    print('The size os this physical quantitity in Kpc is {:.3f}'.format(q))
