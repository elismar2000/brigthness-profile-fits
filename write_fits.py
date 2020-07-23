from astropy.io import fits

import sys

#=================================
input = sys.argv[1]
output = sys.argv[2]

output = str(output)

hdu_list = fits.open(input)
print(hdu_list.info())

sci_data = hdu_list[1].data
dq_data = hdu_list[3].data

mask = dq_data == 0
sci_data *= mask

hdu = fits.PrimaryHDU(sci_data)
hdu.writeto(output)
