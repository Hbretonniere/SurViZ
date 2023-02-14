import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
from astropy.io import fits
import streamlit as st
import seaborn as sns
from utils.plot_surveys import *
from astropy.visualization import ZScaleInterval

def plot_bands(info, telescopes, instruments, bands, surveys, fill=True, log=False):
    """
    Plot the selected filters of the selected telescopes and instruments
    The filters shape are simply defined as rectangles at the centered wavelength +/- FWHM/2
    The height is arbitrary, it does not contain any information about the sensitivity of the filter
    We just chose different heights for each mission and filter for a better display

    Parameters
    ----------
        - info:         dictionary,      the dictionary containing all the information of the telescopes
        - telescopes:   list of strings, the names of the selected telescopes
        - instruments:  list of strings, the name of the selected instruments
        - bands:        list of strings, the name of the selected bands
        - fill:         boolean,         if true, fill the filters' rectangles
        - log:          boolean,         if true, the x scale will be log

    Returns
    ----------
        - fig: the plt figure to plot

    """

    # Do not use seaborn style
    sns.reset_orig()
    plt.rcParams.update({"font.size": 22})

    # Create the figure
    fig, ax = plt.subplots(figsize=(15, 10))

    # Loop through the telescopes
    for i, telescope in enumerate(telescopes):
        j = i+1  # used to plot all telescope's bands at a different hight (for better visualisation)
        k = 0    # used to plot all band at a different hight (for better visualisation)

        # Loop trough the instruments
        for instrument in instruments[telescope]:
            
            # Empty plot for legend (to have a unique legend for the instrument)
            ax.plot([], [], ls=info[telescope]['instruments'][instrument]['ls'], color=info[telescope]['color'], label=f'{telescope} {instrument}')
            
            # Loop through the filters
            for i, band in enumerate(bands[telescope][instrument]):
                k += 1

                # Get bands info (min and max)
                band_info = info[telescope]['instruments'][instrument]['bands'][band]
                min_, max_ = band_info["min_max"]
                
                # Create the rectangle, with a height depending on the telescope and band number
                ax.hlines(10-j-k/10, min_, max_, color=info[telescope]['color'], ls=info[telescope]['instruments'][instrument]['ls'], alpha=0.7, lw=3)
                ax.vlines([min_, max_], ymin=0, ymax=[10-j-k/10, 10-j-k/10], color=info[telescope]['color'], ls=info[telescope]['instruments'][instrument]['ls'], alpha=0.7, lw=3)

                # If fill, fill the rectangle
                if fill:
                    ax.fill_between([min_, max_], 10-j-k/10, 0, color=info[telescope]['color'], alpha=0.5)

                # Add the name of the band above the rectangle
                plt.text((max_+min_)/2, 10-j-k/10+0.2, band, c=info[telescope]['color'], rotation=90, size=10)  #10-j+((10-j)/30)-k/30

    # Fix the limits of the y axis for better visualisation
    ax.set_ylim([-1, 10])
    
    # Remove the y ticks, as it is an arbitrary height
    ax.set_yticks([])    
    
    # Put the appropriate x-scale
    if log:
        ax.set_xscale('log')
    else:
        ax.set_xscale('linear')
    
    # x legend, depending on the number of instruments for better display
    ax.set_xlabel('Wavelength (nm)', fontsize=20)
    plt.legend(bbox_to_anchor = (1, 1.2), ncol=max(1, len(instruments)//2), fontsize=20)

    return fig

def plot_mirrors(info, telescopes):
    
    """
    Plot the mirrors of the selected telescopes.
    The mirrors are simply defined as a circle of the corresponding mirror radius.
    The complexity of the true real shape of the mirror is not taken into account.

    Parameters
    ----------
        - info:         dictionary,      the dictionary containing all the information of the telescopes
        - telescopes:   list of strings, the names of the selected telescopes
    
    Returns
    ----------
        - fig: the plt figure to plot

    """

    # Do not use seaborn style
    sns.reset_orig()

    # Create the figure
    fig, ax = plt.subplots(figsize=(10, 10))

    # Ensure that a circle appears as a circle
    ax.set_aspect("equal")

    # keep track of the diameters 
    ds = []

    # Loop through the telescopes
    for telescope in telescopes:
        if telescope == "Fermi":
            st.markdown('### Fermi has no mirror, the technology for gamma ray is different.')
            continue
        # get the miror's diameter
        d = info[telescope]["mirror"]

        # If a diameter is already present, change the line style
        # for beter visualisation
        if d in ds:
            ls = "--"
        else:
            ls = "-"
        ds.append(d)

        # Create the circle, with the telescope's defined color
        mirror = plt.Circle(
            (0, 0),
            d / 2,
            fill=False,
            lw=2,
            ec=info[telescope]["color"],
            label=telescope,
            alpha=0.8,
            ls=ls,
        )

        # add the artist to the plt
        ax.add_patch(mirror)
    
    # Defined the plot limits depending on the largest mirror,
    # and center on zero
    dmax = np.max(ds) + 1
    ax.set_xlim(-dmax / 2, dmax / 2)
    ax.set_ylim(-dmax / 2, dmax / 2)

    # Remove the axis ticks
    ax.set_xticks([])
    ax.set_yticks([])

    # Add a human stick figure (1.80)
    human_axes = ax.inset_axes(
        [-1.8 / 2, -1.8 / 2, 1.8, 1.8], transform=ax.transData, zorder=0
    )
    human_axes.imshow(mpimg.imread("./data/human.png"), alpha=0.3, aspect="auto")

    # Remove the human figure axes ant ticks
    human_axes.axis("off")
    human_axes.set_xticks([])
    human_axes.set_yticks([])
    plt.title("Primary Mirror Size")
    plt.legend()

    return fig


def plot_fovs(info, telescopes):

    """
    Plot the field of view (FOV) of the selected telescopes.
    The fovs are simply defined as a square of the corresponding FOVs radii.

    Parameters
    ----------
        - info:         dictionary,      the dictionary containing all the information of the telescopes
        - telescopes:   list of strings, the names of the selected telescopes
    
    Returns
    ----------
        - fig: the plt figure to plot

    """
    
    # Do not use seaborn style
    sns.reset_orig()

    # Create the figure
    fig, ax = plt.subplots(figsize=(8, 8))

    # Ensure that a square appears as a square
    ax.set_aspect("equal")
    
    # Hard code the x and y limits (Rubin is huge..., Fermi even more)
    if "Fermi" in telescopes:
        lims = 5500
    elif "Rubin" in telescopes:
        lims = 120
    else:
        lims = 30
    ax.set_xlim(-lims, lims)
    ax.set_ylim(-lims, lims)

    # Add a black background
    ax.add_patch(
        plt.Rectangle(
            (-lims, -lims), 2 * lims, 2 * lims, fc="black", ec="red", zorder=0
        )
    )

    # Loop through the selected telescopes
    for telescope in telescopes:

        # get the x and y sizes of the FOV
        x, y = info[telescope]["fov"]

        # Create the FOV rectangle
        fov = plt.Rectangle(
            (-x / 2, -y / 2),
            x,
            y,
            fc=info[telescope]["color"],
            ec="white",
            lw=2,
            label=telescope,
            alpha=0.3,
        )

        # Add the artist ot the plot
        ax.add_patch(fov)

    # Add an image of the moon at good scale
    moon_axes = ax.inset_axes(
        [-31 / 2, -31 / 2, 31, 31], transform=ax.transData, zorder=0
    )
    moon_axes.imshow(mpimg.imread("./data/moon.png"), aspect="auto")

    # Remove moon axes
    moon_axes.set_xticks([])
    moon_axes.set_yticks([])

    # Add an indication of the scale
    ax.errorbar([-31/2, 31/2], [0, 0], yerr=[2, 2], c='darkred')
    ax.text(-2.2, 1, "31'", color='darkred')
    ax.set_xlabel('arcmin')
    ax.set_ylabel('arcmin')
    plt.title("Field Of View")
    plt.legend()
    return fig


def plot_fields(telescopes, surveys, instruments, info, nb_to_plot, bands=None):
    """
    Plot the galaxy fields of the selected telescopes and instruments
    See sim_field() in utils/diverse_utils.py for extended information 
    about the fields simulations
    
    The images have all the same min max for a fair comparison, 
    defined with the min and max of all the ZScaleInterval.
    
    There is a second option to remove the image with the highest contrast for
    a better display of the others

    Parameters
    ----------
        - telescopes:   list of strings, the names of the selected telescopes
        - instruments:  list of strings, the name of the selected instruments
        - info:         dictionary,      the dictionary containing all the information of the telescopes
        - nb_to_plot:   int,             the number of subplots

    Returns
    ----------
        - fig: the plt figure to plot
    """

    # Do not use seaborn style
    sns.reset_orig()
    plt.rcParams.update({"font.size": 10})
    
    # We always want two columns: compute the number of lines corresponding
    nb_lines = int(np.ceil(nb_to_plot / 2))

    # Create the figure
    fig, ax  = plt.subplots(nb_lines, 2, figsize=(10, nb_lines * 5))

    # Flatten the subplots to be able to easily loop
    ax = ax.flatten()
    k = 0

    # Keep all images in memory to control global scale
    images = {}
    mins = []
    maxs = []

    # Loop through the telescopes a first time to load the images and compute the scales
    for telescope in telescopes:
        # Nicely organized dictionary for further plotting
        images[telescope] = {}

        # Loop trough the surveys
        for survey in surveys[telescope]:
            images[telescope][survey] = {}

            # Loop through the instruments
            for instrument in instruments[telescope][survey]:

                # If the image exist in the folders:
                try:
                    # load and keep the image
                    images[telescope][survey] = fits.open(f'./data/fields/{telescope}_{instrument}_{survey}.fits')[0].data

                    # find the min and max of the ZScaleInterval
                    interval = ZScaleInterval()
                    a = interval.get_limits(images[telescope][survey])
                    mins.append(a[0])
                    maxs.append(a[1])
                
                # If the image does not exist, plot a black image with white cross
                except OSError:
                    images[telescope][survey] = np.diag(np.ones(128))
                    images[telescope][survey] += np.fliplr(images[telescope][survey])

                    # Show an error message explaining that the image is not yet avaiable
                    st.write(f'Sorry, {telescope} {survey} {instrument} is not implemented yet! Stay Tuned !')
                    # st.write(f'Sorry, ./data/fields/{telescope}_{instrument}_{survey}.fits is not implemented yet!')

    # Find the global min and max of all the zscale intervals
    min_v, max_v = np.min(mins), np.max(maxs)
    
    # Compute a second min max for an alternative contrast
    if len(mins) >= 2:
        mins.remove(min_v)
        maxs.remove(max_v)
    min_2, max_2 = np.min(mins), np.max(maxs)

    # Define the button for the second contrast option
    contrast2 = st.checkbox('Other Contrast')

    # If second contrast, change the min_ max_ values
    if contrast2:
        min_v, max_v = min_2, max_2

    # Second loop through the telescopes to plot
    for telescope in telescopes:

        # Warnings for images I'm yet not sure of...
        if (telescope == 'HST') or (telescope == 'SDSS'):
            warning = 'Warning: The noise level is unsure (need to be checked)'
        else:
            warning = ""
        
        # Loop through surveys
        for survey in surveys[telescope]:

            # Loop through telescopes
            for instrument in instruments[telescope][survey]:
                
                # plot the image in the appropriate subplot, with the fixed min max
                ax[k].imshow(images[telescope][survey], cmap='bone', vmin=min_v, vmax=max_v)

                # Get the filters information and plot it in the subplot title
                filter = info[telescope]['surveys'][survey]['instruments'][instrument]['main_band']
                ax[k].set_title(f"{telescope}, {survey} {instrument} ({filter} filter), \n {warning}", fontsize=10)

                k += 1 # get the subplot number updated

    # If the number of image is odd, the last subplot is empty, remove the axis
    if nb_to_plot % 2 != 0:
        ax[-1].set_visible(False)

    return fig


def plot_galaxies(info, telescopes, instruments, nb_to_plot, change_gal, same_size, nbs=[2, 3, 4], nb=1, bands=None):
    """
    Plot the images of a galaxy as seen by the selected telescopes and instruments
    
    See create_and_save_gal in utils/diverse_utils.py for extended information about the simulation
    
    By default, all images are zoom in to have the same aspect.
    There is an option to show the same area of the sky in each plot (no zoom)

    Parameters
    ----------
        - info:         dictionary,      the dictionary containing all the information of the telescopes
        - telescopes:   list of strings, the names of the selected telescopes
        - instruments:  list of strings, the name of the selected instruments

    Returns
    ----------
        - fig: the plt figure to plot

    """

    # Do not use seaborn style
    sns.reset_orig()
    plt.rcParams.update({"font.size": 10})

    # Create the button for the same image size option
    # same_size = st.checkbox('Same size image')

    # We always want two columns: compute the number of lines corresponding
    nb_lines = int(np.ceil(nb_to_plot / 2))

    # Create the figure and  flatten the subplots to be able to easily loop
    fig, ax  = plt.subplots(nb_lines, 2, figsize=(10, nb_lines * 5))
    ax = ax.flatten()

    k = 0

    # keep trace of the image sizes (in arcsec) to be able to rescale them all to the same area
    sizes = []

    images = {}

    # if len(nbs) == 0:
        # nbs = [1, 2]
    if change_gal:
        if len(nbs) == 0:
            nbs = [1, 2, 3, 4]
        nb = np.random.choice(nbs)
        nbs.remove(nb)
        
    # First loop to load and find the maximum size
    for telescope in telescopes:

        # Nicely organized dictionary for further plotting        
        images[telescope] = {}

        # Loop through the instruments
        for instrument in instruments[telescope]:
            
                # file_name = f'./data/individual_galaxies/gal2_{telescope}_{instrument}.npy'
            # else:
            file_name = f'./data/individual_galaxies/gal{nb}_{telescope}_{instrument}.npy'
            # If the image exist in the folders:
            try:
                # load and keep the image
                images[telescope][instrument] = np.load(file_name, allow_pickle=True)
                
                # Compute the size of the stamp in arcsec
                sizes.append(237 * 0.03/info[telescope]['instruments'][instrument]['pix_scale'])
            
            # If the image does not exist, plot a black image with white cross
            except OSError:
                images[telescope][instrument] = np.diag(np.ones(128))
                images[telescope][instrument] += np.fliplr(images[telescope][instrument])

                st.write(f'Sorry, {telescope} {instrument} is not implemented yet!')
                # st.write(f'Sorry, ./data/individual_galaxies/gal_{telescope}_{instrument}.npy is not implemented yet!')

    # Find the max size            
    max_size = np.max(sizes)

    # Second loop for the actual plotting
    for telescope in telescopes:
        # Loop through teh instruments
            for instrument in instruments[telescope]:
                # Load the image from the dictionary
                img = images[telescope][instrument]
                
                # If we want the same area of the sky, padd the image with the appropriate numner of zeros
                # to match the largest image
                if same_size:
                    padding = int((max_size - np.shape(img)[0])/2)
                    img = np.pad(img, ((padding, padding), (padding, padding)), constant_values=0)

                # plot the image in the subplot
                ax[k].imshow(img, cmap='bone')
                ax[k].set_title(f'{telescope}, {instrument}', fontsize=10)

                k += 1 # update the subplot number

    # If the number of image is odd, the last subplot is empty, remove the axis
    if nb_to_plot % 2 != 0:
        ax[-1].set_visible(False)

    return fig


def plot_surveys(telescopes, surveys):
    """
    Plot the surveys footprint
    
    For now, the sky is plot with equatorial coordinates, centered in RA = 110deg,
    with a Mollweide projection.
    The areas and shapes are not perfect nor very automatized

    There are two options for now: you can zoom in certain surveys, 
    and you can write the name of the surveys above there footprint
    (for small ore non continuous surveys)
    
    See utils/plot_surveys.py to see how the footprints are created

    Parameters
    ----------
        - telescopes:   list of strings, the names of the selected telescopes
        - surveys:      list of strings, the name of the selected surveys

    Returns
    ----------
        - fig: the plt figure to plot
    """

    # Set seaborn ploting style
    sns.set()

    # Two columns for the two options
    col1, col2 = st.columns(2)

    # Button to display the name of the surveys or not
    with col1:
        show_name = st.checkbox('Show survey names', value=True)
    
    # initialise the sky map with the good shift and projection (plt as a strange way of plotting the sky)
    # also returns the ra and dec of the galactic and ecliptic plane with the
    # appropriate shift

    fig, ax, ecliptic, galactic = init_sky()

    # Ecliptic plane
    # Concatenate the two arrays of the ecliptic to deal with the discontinuty in 360/0
    # and have a single line not connected in the border of the map
    ecliptic_ra_deg = np.concatenate((ecliptic.ra.degree[160:], ecliptic.ra.degree[:160], ))
    ecliptic_dec_deg = np.concatenate(( ecliptic.dec.degree[160:], ecliptic.dec.degree[:160],))

    # Plot the ecliptic
    ax.plot(ax.projection_ra(ecliptic_ra_deg), ax.projection_dec(ecliptic_dec_deg), color='black', alpha=0.5, ls='--', lw=0.7)
    
    # Same for the galactic plane
    galactic_ra_deg = np.concatenate((galactic.ra.degree[14:], galactic.ra.degree[:14]))
    galactic_dec_deg = np.concatenate((galactic.dec.degree[14:], galactic.dec.degree[:14]))
    ax.plot(ax.projection_ra(galactic_ra_deg), ax.projection_dec(galactic_dec_deg), color='black', alpha=0.5, lw=0.7)

    # create a separate legend for the ecliptic and galactic plane
    lines = ax.get_lines()
    legend1 = plt.legend([lines[0]], ['Ecliptic'], fontsize=15, bbox_to_anchor = (0.14, 1.05))
    ax.add_artist(legend1)
    legend2 = plt.legend([lines[1]], ['Galactic'], fontsize=15, bbox_to_anchor = (1.02, 1.05))
    ax.add_artist(legend2)

    
    # Keep the patches in the cosmos regions in memory
    cosmos_patches = []

    # Loop through the telescopes
    for telescope in telescopes:

        # Loop through the surveys
        for survey in surveys[telescope]:
            # st.markdown(f'{telescope}-{survey}')
            # for each scenario, call the appropriate function defined
            # in utils/plot_surveys. This is a bit stupid, there must be a better way to do it...

            if f'{telescope}-{survey}' == 'Euclid-Deep-Survey':
                ax = plot_Euclid_Deep_Survey(fig, ax, show_name)

            elif f'{telescope}-{survey}' == 'Euclid-Wide-Survey':
                # Euclid wide needs the galactic and ecliptic way to be plotted
                ax = plot_Euclid_Wide_Survey(fig, ax, ecliptic_ra_deg, ecliptic_dec_deg, galactic_ra_deg, galactic_dec_deg)

            elif f'{telescope}-{survey}' == 'HST-HST-Cosmos':
                ax, cosmos_patch = plot_HST_cosmos_Survey(fig, ax, show_name)
                cosmos_patches.append(cosmos_patch)

            elif f'{telescope}-{survey}' == 'Rubin-LSST':
                ax = plot_Rubin_LSST_Survey(fig, ax)

            elif f'{telescope}-{survey}' == 'JWST-Cosmos-Web':
                ax, cosmos_patch = plot_cosmos_Web_Survey(fig, ax, show_name)
                cosmos_patches.append(cosmos_patch)

            elif f'{telescope}-{survey}' == 'JWST-CEERS':
                ax, cosmos_patch = plot_JWST_CEERS_Survey(fig, ax, show_name)
                cosmos_patches.append(cosmos_patch)

            elif f'{telescope}-{survey}' == 'HST-HST-CANDELS':
                ax = plot_HST_CANDELS_Survey(fig, ax, show_name)

            elif f'{telescope}-{survey}' == 'SDSS-SDSS-I':
                ax = plot_SDSS_I_Survey(fig, ax)
            
            elif  f'{telescope}-{survey}' == 'Chandra-Deep-North':
                ax = plot_Chandra_Deep_North_Survey(fig, ax, show_name)

            elif  f'{telescope}-{survey}' == 'Fermi-All_sky':
                ax = plot_Fermi_all_sky_Survey(fig, ax)

            # Warning if the survey is not yes defined
            else:
                st.markdown(f'Sorry, {telescope} {survey} is not yet available... Stay Tuned!')

    # possibility to zoom in cosmos regions if cosmos is plotted
    if any(('HST-Cosmos') in x for x in list(surveys.values())) or any(('Cosmos-Web') in x for x in list(surveys.values())):
        # Create the button to zoom in
        with col2:
            cosmos_zoom = st.checkbox('Zoom on Cosmos')
        
        if cosmos_zoom:
            # Add an inset plot above the sky plot
            zoom = ax.inset_axes([0.05, 1.15, 0.2, 0.4])

            # Define the area covered by the zoom (in degrees)
            sx = 1
            sy = 1

            # plot all the patches in the inset
            [zoom.add_patch(patch) for patch in cosmos_patches]

            # Set the lims and put the appropriate xticks
            zoom.set_xlim(rad(-40)-rad(sx), rad(-40)+rad(sx))
            zoom.set_ylim(rad(2)-rad(sy), rad(2)+rad(sy))
            xticks = list(zoom.get_xticks())
            yticks = list(zoom.get_yticks())
            zoom_xticks = [xticks[0], (xticks[-1] + xticks[0]) / 2, xticks[-1]]
            zoom_yticks = [yticks[0], (yticks[-1] + yticks[0]) / 2, yticks[-1]]
            zoom.set_xticks(zoom_xticks)
            zoom.set_yticks(zoom_yticks)
            zoom.set_xticklabels([np.round(150.12+sx, 2), np.round(150.12, 2), np.round(150.22-sx, 2)])
            zoom.set_yticklabels([np.round(2.20-sy, 2), np.round(2.20, 2), np.round(2.20+sy, 2)])
            zoom.set_xlabel('RA')
            zoom.set_ylabel('DEC')

            # Put an arrow directed to the actual cosmos field in the all sky map
            zoom.annotate('', xy=(0.6, 0), xycoords='axes fraction', xytext=(1.7, -1.55), arrowprops=dict(arrowstyle="<-", color='gray', alpha=0.9, lw=2))
    
    # Legend for the surveys
    plt.legend(bbox_to_anchor = (1, -0.1), ncol=2, fontsize=17)
    
    return fig