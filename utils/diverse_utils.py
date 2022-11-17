import numpy as np
from astropy.coordinates import SkyCoord
import astropy.units as u
import galsim 
import glob 
import sys
import streamlit as st
from astropy.io import fits
from types import MethodType
import matplotlib.pyplot as plt
from astropy.coordinates import ICRS

def MagToFlux(zp, mag):
    Flux = np.power(10, ((zp - mag)*0.4))
    return Flux

ra_center = 120


def init_sky(projection='mollweide', ra_center=110,
             galactic_plane_color='red', ecliptic_plane_color='red',
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
    galactic_plane_color : color name, optional
        Draw a solid curve representing the galactic plane using the specified color, or do
        nothing when ``None``.
    ecliptic_plane_color : color name, optional
        Draw a dotted curve representing the ecliptic plane using the specified color, or do
        nothing when ``None``.
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
    if galactic_plane_color is not None:
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
    if ecliptic_plane_color is not None:
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



def projection_ra(self, ra):
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


def projection_dec(self, dec):
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
    
    return np.exp(-fac/ 2) / N #* np.exp(-fac2/ 2) / N2


def ecl2gal(lon_ecl, lat_ecl):
    '''
    # adapted from https://astronomy.stackexchange.com/questions/39404/how-to-plot-celestial-equator-in-galactic-coordinates-why-does-my-plot-appear

    Transforms ecliptic coordinates to galactic ones.
    Then prepares them for matplotlib aitoff projection.
    '''
    
    ecl = SkyCoord(lon_ecl, lat_ecl, unit=u.deg, frame='barycentricmeanecliptic')
    gal = ecl.transform_to('galactic')

    # Minus appears because of “mapping from the inside” issue
    l_gal, b_gal = -gal.l.wrap_at('180d').radian, gal.b.radian
    
    return l_gal, b_gal

def eq2gal(ra, dec):
    
    '''
    # adapted from https://astronomy.stackexchange.com/questions/39404/how-to-plot-celestial-equator-in-galactic-coordinates-why-does-my-plot-appear

    Transforms equatorial coordinates to galactic ones.
    Then prepares them for matplotlib aitoff projection. 
    '''
    
    eq = SkyCoord(ra, dec, unit=u.deg)
    gal = eq.galactic

    # Minus appears because of “mapping from the inside” issue
    l_gal, b_gal = -gal.l.wrap_at('180d').radian, gal.b.radian
    
    return l_gal, b_gal



def sim_field(cat, pxscale, fwhm, noise_level, zp):

    catName = glob.glob('../data/vis_0*')[0]
    cat = galsim.Catalog(catName) 
    ### NOISE LEVEL IN MICROJANSKY
    divideFor = 40
    NumGal = 314*1000/(divideFor**2)  # 314709 in the list
    image_size_x = int(25000/divideFor)
    image_size_y = int(25000/divideFor)
    full_image = galsim.ImageF(image_size_x, image_size_y)
    for i in range(int(NumGal)):
        if i == 184:
            continue
        stamp_size = 1000
        stamp_gal = galsim.ImageF(stamp_size, stamp_size, scale=pxscale)
        gal_idx = i
        float_ix = cat.getFloat(gal_idx, 1) / divideFor
        float_iy = cat.getFloat(gal_idx, 2) / divideFor
        radiusBulge = cat.getFloat(i, 5)
        radiusDisk = cat.getFloat(i, 8)*1.678
        bt = cat.getFloat(i, 4)
        ell_B = cat.getFloat(i, 6)
        ell_D = cat.getFloat(i, 9)
        q = bt*ell_B + (1-bt)*ell_D
        mag = cat.getFloat(i, 3)
        Flux = MagToFlux(zp, mag)
        PA = cat.getFloat(i, 7)
        ix = int(cat.getFloat(i, 1) / divideFor)
        iy = int(cat.getFloat(i, 2) / divideFor)
        dx = float_ix - ix
        dy = float_iy - iy
        offset = galsim.PositionD(dx, dy)
        bulge = galsim.Sersic(4, radiusBulge, flux=1.0)
        b_shear = galsim.Shear(q=ell_B, beta=galsim.Angle(PA, galsim.radians))
        bulge = bulge.shear(b_shear)
        
        disk = galsim.Sersic(1, radiusDisk, flux=1.0)
        d_shear = galsim.Shear(q=ell_D, beta=galsim.Angle(PA, galsim.radians))
        disk = disk.shear(d_shear)
        gal = bulge + disk
        psf = galsim.Gaussian(flux=1., fwhm=fwhm)
        gal = galsim.Convolve(psf, gal)
        gal = gal.withFlux(Flux)
        try:
            stamp = gal.drawImage(stamp_gal, method='no_pixel')
        except Exception:
            print(i, radiusBulge, radiusDisk)
            continue
        stamp.setCenter(ix, iy)
        bounds = stamp.bounds & full_image.bounds
        full_image[bounds] += stamp[bounds]
        full_image += np.random.normal(0, noise_level, (image_size_x, image_size_y))
    return full_image.array

def sim_and_save(cat, telescope, instrument, survey):
    "Example: sim_and_save('HST', 'ACS', 'HST-Cosmos')"

    sys.path.append('../')
    from telescopes.main_info import info
    instrument_info = info[telescope]['surveys'][survey]['instruments'][instrument]
    band = instrument_info['main_band']
    image = sim_field(cat, instrument_info['pix_scale'],
                instrument_info['bands'][band]['fwhm'],
                info[telescope]['surveys'][survey]['std_noise'],
                instrument_info['bands'][band]['zp'])
    
    fits.writeto(f'../data/fields/{telescope}_{instrument}_{survey}.fits', image, overwrite=True)

def create_and_save_gal(info, telescope, instrument, show=False):
    import cv2
    from scipy.signal import convolve2d

    survey = list(info[telescope]['surveys'].keys())[0]
    instrument_info = info[telescope]['surveys'][survey]['instruments'][instrument]
    pixel_scale = instrument_info['pix_scale']

    band = instrument_info['main_band']
    fwhm = instrument_info['bands'][band]['fwhm']
    print(pixel_scale, fwhm)
    img = np.load('../data/tng_gal.npy')[10:-1, 10:-10]
    s = int(237 * 0.03/pixel_scale)
    size = (s, s)
    psf = create_psf(fwhm, pixel_scale)
    psfed = convolve2d(img, psf, mode='same')
    res = cv2.resize(psfed, dsize=size, interpolation=cv2.INTER_CUBIC)
    np.save(f'../data/individual_gals/gal_{telescope}_{instrument}.npy', res)


def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://imgur.com/a/MjaKHak);
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 10px 20px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "SurViZ";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )