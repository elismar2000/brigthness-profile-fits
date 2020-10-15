from __future__ import print_function
import argparse
import numpy as np

#=======================
#Parsing arguments
#=======================
parser = argparse.ArgumentParser()
parser.add_argument('--pixel_scale', metavar='ps', type=float, help='The image pixel scale in arcseconds')
parser.add_argument('--quantity', metavar='q', type=float, help='The physical quantity to be converted, in px')
parser.add_argument('--distance', metavar='d', type=float, help='Distance to the object in Mpc')

args = parser.parse_args()

ps = args.pixel_scale
q  = args.quantity
d  = args.distance

#========================
#Performing convertion
#========================
ps *= (1/3600) * np.pi/180 #from arcsecs to radians
d *= 1e+3 #from Mpc to Kpc

q *= ps * d

print('The size os this physical quantitity in Kpc is {:.3f}'.format(q))
