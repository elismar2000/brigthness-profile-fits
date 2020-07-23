import matplotlib.pyplot as plt
import numpy as np
from astropy import wcs
from astropy.io import fits
from mpl_toolkits.axes_grid1 import make_axes_locatable
from numpy import ma

image = '/home/elismar/Documentos/Fisica/IC/imfit-1.7.1/ngc2992-93/images/GMOS/ngc2992/S20180216S0095_final_cut.fits'
model = '/home/elismar/Documentos/Fisica/IC/imfit-1.7.1/ngc2992-93/images/GMOS/ngc2992/ngc2992_model4.fits'
residual = '/home/elismar/Documentos/Fisica/IC/imfit-1.7.1/ngc2992-93/images/GMOS/ngc2992/ngc2992_residual4.fits'

def get_stmag(data, photflam):
    data[data <= 0] = np.nan
    return -2.5 * np.log10(data * photflam) - 21.10


def plot_ruler(ax, color):
    ax.annotate('2 kpc', (-7, -9.5), ha='center', va='bottom', color=color)
    ax.plot([-9, -9 + 2000.0 / 496.0], [-10, -10], color=color, lw=2)


def paper_plot():
    with fits.open(residual) as hdu:
        w = wcs.WCS(image)
        original_header = fits.getheader(image)
        y, x = np.indices(hdu[0].data.shape)
        ra, dec = w.wcs_pix2world(x, y, 1)

    ra0 = 121.9209810
    dec0 = 39.0042138

    fig, axes = plt.subplots(nrows=1, ncols=3, sharey='row', num=1, figsize=(9, 3))

    photflam = original_header['photflam']

    d_original = get_stmag(fits.getdata(image), photflam)
    model = get_stmag(fits.getdata(model), photflam)

    # a = ma.array(d, mask=np.isnan(d))
    a = d_original - model
    b = ma.array(d_original, mask=False)
    c = ma.array(model, mask=False)

    titles = ['Data', 'Model', 'Residuals']

    def makeplot(data, i):
        ax = axes[i]

        dra = -(ra - ra0) * np.cos(np.deg2rad(dec)) * 3600.
        ddec = (dec - dec0) * 3600.

        if i == 2:
            vmin = -1.
            vmax = +1.
            cmap = 'Spectral_r'
        else:
            vmin, vmax = (22, 28)
            cmap = 'plasma_r'

        im = ax.pcolormesh(dra, ddec, data, vmin=vmin, vmax=vmax, cmap=cmap, rasterized=True)

        div = make_axes_locatable(ax)
        cax = div.append_axes('right', size=.1, pad=0.05)
        cbar = plt.colorbar(im, cax)
        cax.locator_params(nbins=5)

        if i == 2:
            cbar.set_label(r'$\Delta$ STMAG (F105W)')
            plot_ruler(ax, 'black')
        else:
            cbar.set_label('STMAG (F105W)')
            plot_ruler(ax, 'white')

        ax.set_title(titles[i])

        ax.set_aspect('equal', 'box')

        ax.set_xlabel(r'$\Delta \,\, {\rm RA}$ (arcsec)')

        if i == 0:
            ax.set_ylabel(r'$\Delta \,\, {\rm DEC}$ (arcsec)')

        l = 12
        ax.set_xlim(-l, l)
        ax.set_ylim(-l, l)

        ax.locator_params(nbins=5)

        ax.minorticks_on()

    for data, i in zip([b, c, a], range(3)):
        makeplot(data, i)

    fig.tight_layout()
    plt.savefig('imfit_results.pdf', bbox_inches='tight', format='pdf')
    plt.show()


if __name__ == '__main__':
    paper_plot()
