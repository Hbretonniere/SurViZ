import numpy as np
from astropy.coordinates import SkyCoord
import astropy.units as u
# import galsim 
import glob 
import sys
import streamlit as st
from astropy.io import fits
from types import MethodType
import matplotlib.pyplot as plt
from astropy.coordinates import ICRS
import cv2
from scipy.signal import convolve2d


def MagToFlux(zp, mag):
    """
    Convert a magnitude to the corresponding total flux, depending on 
    the AB zero-point magntiude of the instrument
    
    Parameters
    ----------
        - zp : float, the zero-point magnitude of the instrument
        - mag : float: the magnitude of the object
    
    Returns
    ----------
    
        - Flux: the corresponding flux

    """

    Flux = np.power(10, ((zp - mag)*0.4))
    return Flux


def init_sky(projection='mollweide', ra_center=110,
             ax=None):
    """
    Adapted from https://desiutil.readthedocs.io/en/latest/_modules/desiutil/plots.html

    Initialize matplotlib axes with a projection of the full sky.

    Parameters
    ----------
    projection : :class:`str`, optional
        Projection to use. Defaults to 'mollweide'.  To show the available projections,
        call :func:`matplotlib.projections.get_projection_names`.
    ra_center : :class:`float`, optional
        Projection is centered at this RA in degrees. Default is +120°, which avoids splitting
        the DESI northern and southern regions.
    ax : :class:`~matplotlib.axes.Axes`, optional
        Axes to use for drawing this map, or create new axes if ``None``.

    Returns
    -------
    :class:`~matplotlib.axes.Axes`
        A matplotlib Axes object.  Helper methods ``projection_ra()`` and ``projection_dec()``
        are added to the object to facilitate conversion to projection coordinates.

    Notes
    -----
    If requested, the ecliptic and galactic planes are plotted with ``zorder`` set to 20.
    This keeps them above most other plotted objects, but legends should be set to
    a ``zorder`` higher than this value, for example::

        leg = ax.legend(ncol=2, loc=1)
        leg.set_zorder(25)
    """
    #
    # Internal functions.
    #
    def projection_ra(self, ra):
        r"""Shift `ra` to the origin of the Axes object and convert to radians.

        Parameters
        ----------
        ra : array-like
            Right Ascension in degrees.

        Returns
        -------
        array-like
            `ra` converted to plot coordinates.

        Notes
        -----
        In matplotlib, map projections expect longitude (RA), latitude (Dec)
        in radians with limits :math:`[-\pi, \pi]`, :math:`[-\pi/2, \pi/2]`,
        respectively.
        """
        #
        # Shift RA values.
        #
        r = np.remainder(ra + 360 - ra_center, 360)
        #
        # Scale conversion to [-180, 180].
        #
        r[r > 180] -= 360
        #
        # Reverse the scale: East to the left.
        #
        r = -r
        return np.radians(r)

    def projection_dec(self, dec):
        """Shift `dec` to the origin of the Axes object and convert to radians.

        Parameters
        ----------
        dec : array-like
            Declination in degrees.

        Returns
        -------
        array-like
            `dec` converted to plot coordinates.
        """
        return np.radians(dec)
    #
    # Create ax.
    #
    if ax is None:
        fig = plt.figure(figsize=(10.0, 5.0), dpi=100)
        ax = plt.subplot(111, projection=projection)
    #
    # Prepare labels.
    #
    base_tick_labels = np.array([150, 120, 90, 60, 30, 0, 330, 300, 270, 240, 210])
    base_tick_labels = np.remainder(base_tick_labels+360+ra_center, 360)
    tick_labels = np.array(['{0}°'.format(l) for l in base_tick_labels])
    #
    # Galactic plane.
    #
    galactic_l = np.linspace(0, 2 * np.pi, 100)
    galactic = SkyCoord(l=galactic_l*u.radian, b=np.zeros_like(galactic_l)*u.radian,
                            frame='galactic').transform_to(ICRS)
        #
        # Project to map coordinates and display.  Use a scatter plot to
        # avoid wrap-around complications.
        #

        # Make sure the galactic plane stays above other displayed objects.
    #
    # Ecliptic plane.
    #
    ecliptic_l = np.linspace(0, 2 * np.pi, 200)
    ecliptic = SkyCoord(lon=ecliptic_l*u.radian, lat=np.zeros_like(ecliptic_l)*u.radian, distance=1 * u.Mpc,
                            frame='heliocentrictrueecliptic').transform_to(ICRS)
    #
    # Set RA labels.
    #
    labels = ax.get_xticklabels()
    for l, item in enumerate(labels):
        item.set_text(tick_labels[l])
    ax.set_xticklabels(labels)
    #
    # Set axis labels.
    #
    ax.set_xlabel('R.A. [deg]')
    ax.set_ylabel('Dec. [deg]')
    ax.grid(True)
    #
    # Attach helper methods.
    #
    ax._ra_center = ra_center
    ax.projection_ra = MethodType(projection_ra, ax)
    ax.projection_dec = MethodType(projection_dec, ax)
    return fig, ax, ecliptic, galactic



def projection_ra(self, ra, ra_center=110):
    r"""
    From https://desiutil.readthedocs.io/en/latest/_modules/desiutil/plots.html

    Shift `ra` to the origin of the Axes object and convert to radians.

    Parameters
    ----------
    ra : array-like
        Right Ascension in degrees.

    Returns
    -------
    array-like
        `ra` converted to plot coordinates.

    Notes
    -----
    In matplotlib, map projections expect longitude (RA), latitude (Dec)
    in radians with limits :math:`[-\pi, \pi]`, :math:`[-\pi/2, \pi/2]`,
    respectively.
    """
    #
    # Shift RA values.
    #
    r = np.remainder(ra + 360 - ra_center, 360)
    #
    # Scale conversion to [-180, 180].
    #
    r[r > 180] -= 360
    #
    # Reverse the scale: East to the left.
    #
    r = -r
    return np.radians(r)


def projection_dec(self, dec, ra_center=110):
    """
    From https://desiutil.readthedocs.io/en/latest/_modules/desiutil/plots.html

    Shift `dec` to the origin of the Axes object and convert to radians.

    Parameters
    ----------
    dec : array-like
        Declination in degrees.

    Returns
    -------
    array-like
        `dec` converted to plot coordinates.
    """
    return np.radians(dec)



def create_psf(fwhm, pxscale):
    """
    Create the image of a PSF, based on a FWHM

    Parameters
    ----------
        fwhm: float, the full width half maximum of the PSF
        pxscale: float, the pixel scale of the instrument

    Returns
    ----------
        PSF: (256, 256) numpy array, the 2d image of the PSF
    """

    N = 256
    X = np.linspace(-127, 127, N)
    Y = np.linspace(-127, 127, N)
    X, Y = np.meshgrid(X, Y)

    # Mean vector and covariance matrix
    mu = np.array([0, 0.])
    Sigma = np.array([[ fwhm/pxscale , 0], [0,  fwhm/pxscale]])

    # Pack X and Y into a single 3-dimensional array
    pos = np.empty(X.shape + (2,))
    pos[:, :, 0] = X
    pos[:, :, 1] = Y
    n = mu.shape[0]
    Sigma_det = np.linalg.det(Sigma)
    Sigma_inv = np.linalg.inv(Sigma)
    N = np.sqrt((2*np.pi)**n * Sigma_det)
    # This einsum call calculates (x-mu)T.Sigma-1.(x-mu) in a vectorized
    # way across all the input variables.
    fac = np.einsum('...k,kl,...l->...', pos-mu, Sigma_inv, pos-mu)
    PSF = np.exp(-fac/ 2) / N
    return PSF


def sim_field(pxscale, fwhm, noise_level, zp):

    """
    Simulate a field of galaxies with Galsim

    Parameters
    ----------
        - cat:         
        - pxscale:     float, the pixel scale of the instrument
        - fwhm:        float, the full width half maximum of the PSF
        - noise level: float, the standard deviation of the background sky noise
        - zp:          float, the AB zero-point magnitude of the instrument
    
    Returns
    ----------
        - full_image:  numpy array, the galaxy flux field

    """
    
    # Charge the catalogue name of galaxy parameters (double Sérsic catalog)
    catName = glob.glob('../data/vis_0*')[0]

    # Transform to galsim like catalog
    cat = galsim.Catalog(catName) 

    # The catalog contains a field of 314000 galaxies, which is to large for what we want
    # To reduce it, we divide the size of the field by 40^2, and thus also the density of sources and positions
    divideFor = 40
    NumGal = 314000/(divideFor**2)  # 314709 in the list
    image_size_x = int(25000/divideFor)
    image_size_y = int(25000/divideFor)

    # Create the blank image of the full field
    full_image = galsim.ImageF(image_size_x, image_size_y)

    # Loop through the galaxies
    for gal_idx in range(int(NumGal)):

        # There's a too big galaxy (too long to simualte)
        if gal_idx == 184:
            continue
        
        # Create the stamp for the individual galaxy
        stamp_size = 1000
        stamp_gal = galsim.ImageF(stamp_size, stamp_size, scale=pxscale)

        # Extract all the necessary parameters (parameter shapes, position and fluxes)
        float_ix = cat.getFloat(gal_idx, 1) / divideFor
        float_iy = cat.getFloat(gal_idx, 2) / divideFor
        radiusBulge = cat.getFloat(gal_idx, 5)
        radiusDisk = cat.getFloat(gal_idx, 8)*1.678
        bt = cat.getFloat(gal_idx, 4)
        ell_B = cat.getFloat(gal_idx, 6)
        ell_D = cat.getFloat(gal_idx, 9)
        q = bt*ell_B + (1-bt)*ell_D
        mag = cat.getFloat(gal_idx, 3)
        Flux = MagToFlux(zp, mag)
        PA = cat.getFloat(gal_idx, 7)
        ix = int(cat.getFloat(gal_idx, 1) / divideFor)
        iy = int(cat.getFloat(gal_idx, 2) / divideFor)
        
        # Simulate the bulge component
        bulge = galsim.Sersic(4, radiusBulge, flux=1.0)

        # Shear to the wanted ellipticity
        b_shear = galsim.Shear(q=ell_B, beta=galsim.Angle(PA, galsim.radians))
        bulge = bulge.shear(b_shear)
        
        # Simulate the disk component
        disk = galsim.Sersic(1, radiusDisk, flux=1.0)
        
        # Shear it to the wanted ellipticity
        d_shear = galsim.Shear(q=ell_D, beta=galsim.Angle(PA, galsim.radians))
        disk = disk.shear(d_shear)

        # SUm the two components
        gal = bulge + disk

        # Create the PSF
        psf = galsim.Gaussian(flux=1., fwhm=fwhm)

        # Convolve the galaxy and the PSF
        gal = galsim.Convolve(psf, gal)

        # Calibrate the flux of the galaxy
        gal = gal.withFlux(Flux)

        # Draw the profile on the stamp
        try:
            stamp = gal.drawImage(stamp_gal, method='no_pixel')
        except Exception:
            print(gal_idx, radiusBulge, radiusDisk)
            continue
        
        # Place the stamp in the corresponding place of the full image 
        stamp.setCenter(ix, iy)
        bounds = stamp.bounds & full_image.bounds
        full_image[bounds] += stamp[bounds]

        # Add the gaussian background noise
        full_image += np.random.normal(0, noise_level, (image_size_x, image_size_y))

    return full_image.array

def sim_and_save_field(info, telescope, instrument, survey):
    """ 
    Simulate and save a galaxy field
    Note that for now, the band is fixed, selected with the "main_band" info ot the instrument

    Parameters
    ----------
        - info:       dictionary, the dictionary containing all the information of the telescopes
        - telescope:  string, the name of the telescope
        - instrument: string, the name of the instrument
        - survey:     string, the name of the survey
    
    Returns
    -------
        None, just save the image with the appropriate name
    
    """

    # Get the dictionary of the telescope's survey's instrument
    instrument_info = info[telescope]['surveys'][survey]['instruments'][instrument]

    # Because for now we simulate only one band, select the "main_band" name
    band = instrument_info['main_band']

    # Simulate the field with the appropriate image quality and depth
    image = sim_field(instrument_info['pix_scale'],
                instrument_info['bands'][band]['fwhm'],
                info[telescope]['surveys'][survey]['std_noise'],
                instrument_info['bands'][band]['zp'])
    
    # write the fits image with the appropriate name
    fits.writeto(f'../data/fields/{telescope}_{instrument}_{survey}.fits', image, overwrite=True)


def create_and_save_gal(info, telescope, instrument, show=False):

    """ 
    Simulate and save a galaxy from a TNG image
    Note that for now, the band is fixed, selected with the "main_band" info ot the instrument
    The image is noiseless, and thus does not depend of the survey, just the instrument

    The native pixel scale is defined as 0.03 arcsec per pixel. This is arbitrary,
    we just need to have this value to be the smallest of all our surveys.
    This way, all the image will be degraded at the good scale, relative to the original one

    Parameters
    ----------
        - info:       dictionary, the dictionary containing all the information of the telescopes
        - telescope:  string, the name of the telescope
        - instrument: string, the name of the instrument
        - show:       bool, if true, imshow the galaxy
    
    Returns
    -------
        None, just save the image with the appropriate name
    """

    # We do not need a specific survey. the first is ok
    survey = list(info[telescope]['surveys'].keys())[0]

    # Get the dictionary of the telescope's survey's instrument
    instrument_info = info[telescope]['surveys'][survey]['instruments'][instrument]
    
    # Get the pixels scale
    pixel_scale = instrument_info['pix_scale']

    # Because for now we simulate only one band, select the "main_band" name
    band = instrument_info['main_band']
    
    # Get the fwhm
    fwhm = instrument_info['bands'][band]['fwhm']

    # Load the file with the Illustris-TNG profile
    img = np.load('../data/tng4_gal.npy')[10:-10, 10:-10]

    # Define the resolution of the image
    # by multiplying the size of the original image (in pixel)
    # by the ratio of the original and telescope pixel scale

    s = int(237 * 0.03/pixel_scale)
    size = (s, s)
    
    # Create the PSF
    psf = create_psf(fwhm, pixel_scale)

    # Convolve the image by the PSF
    psfed = convolve2d(img, psf, mode='same')

    # resize the image
    res = cv2.resize(psfed, dsize=size, interpolation=cv2.INTER_CUBIC)

    if show:
        plt.figure()
        plt.imshow(res, cmap='bone')
    
    # Save the image with the appropriate name
    np.save(f'../data/individual_galaxies/gal4_{telescope}_{instrument}.npy', res)
