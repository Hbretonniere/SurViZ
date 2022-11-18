"""
Visualisation of the image qualities on a galaxy.

The galaxy is an Illustris-TNG galaxy (https://www.tng-project.org/data/)

We first degrade the resolution to the expected pixel scale
The galaxy is then convolved with a PSF modelled as a gaussian with the expected instrument's FWHM

Note that for now, we do not simulate the galaxies on the fly, 
but just read the images previously simulated. Nevertheless, 
the galaxy simulation is automatized in the same way than the other 
features of the app, but takes too much time to be done on the fly.

The user have to select the telescopes he want to display. For each selected telescope,
a new section will appear in the left panel, to chose the survey corresponding to the 
telescope. 
Note that for now, the band is fixed, selected with the "main_band" info ot the instrument

The pixel scale information is stored in the instruments file (/telescopes/instruments.py)
The PSF information is stored in the instrument's band file (/telescopes/instruments.py)

For each selection, the dictionary info from /telescopes/main_info is read.
The structure is as follow. To read Euclid's NIR's pixel scale
     - info['Euclid']["Instruments"]['Euclid_NIR']["pix_scale"]

The galaxy simulation procedure is done in create_and_save_gal(...) in /utils/diverse_utils
The plotting is done by plot_galaxies in /utils/plot_galaxies.py
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from telescopes.main_info import info
from utils.plots import plot_galaxies
from telescopes.references import image_quality_refs


# SurViZ logo
st.image('surviz_black_long.png')

# Description and README. The references are in image_quality_refs /telescopes/references.py
st.markdown('# 🌌 Galaxy visualisation \n')
description = st.expander("README")
description.markdown('For each survey, the galaxy is simulated from an Illustris-TNG galaxy, and rescaled to the pixel-scale of the instrument, then convolved by the aproximate PSF. \n We do not add noise, considering that the galaxy is very near by. To see the impact of the depth in the different surveys, see the Galaxy Field tab. \n The routine used to generate the galaxies can be found in utils/diverse_utils. It is not executed live for computing time reasons. ' + image_quality_refs)

# Multi Select the telescopes. Default Euclid, Rubin/LSST
telescopes = st.sidebar.multiselect(
        "Select telescopes to display",
        list(info.keys()),
        default=["Euclid", 'JWST', 'SDSS']
    )

# Warning and stop if no telescope selected
if len(telescopes) == 0:
    st.markdown('## Please select at least one telescope')

else:
    # Initialise the selected surveys and instruments. THey will be dictionary to keep all the information necessary
    selected_surveys = {}
    selected_instruments = {}

    # keep info of the number of galaxies to plot, for a better display in the plot routine
    nb_to_plot = 0

    # Loop through selected telescopes
    for telescope in telescopes:
        selected_instruments[telescope] = {}

        # Selection of the surveys. Default is the first listed in the dictionary
        st.sidebar.markdown(f'## {telescope}')

        telescope_instrument =  st.sidebar.multiselect(
                f"Select instruments",
                list(info[telescope]['instruments'].keys()),
                default=list(info[telescope]['instruments'].keys())[0])
        
        # Add the selected survey to the dictionary of this the current telescope
        selected_instruments[telescope] = telescope_instrument
        nb_to_plot += len(telescope_instrument)

    # Call the plot routine
    fig = plot_galaxies(info, telescopes, selected_instruments, nb_to_plot)

    # Plot the figure
    st.pyplot(fig)