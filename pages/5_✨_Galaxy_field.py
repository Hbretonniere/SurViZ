import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from telescopes.main_info import info
from utils.plots import plot_fields
from telescopes.references import image_depth_refs


"""
Visualisation of the survey depth

The fields are simulated using galsim, from a catalogue created with EGG.

For each galaxy, we convert the magnitude to the flux corresponding to the zero point magnitude of the instrument.
The galaxy (good pixel scale) is then convolved with the appropriate PSF
A background noise is added, corresponding to the exposure time of the survey

Note that for now, we do not simulate the fields on the fly, 
but just read the images previously simulated. Nevertheless, 
the simulation is automatized in the same way than the other 
features of the app, but takes too much time to be done on the fly.

The user have to select the telescopes he want to display. For each selected telescope,
a new section will appear in the left panel, to chose the survey corresponding to the 
telescope. 
Note that for now, the band is fixed, selected with the "main_band" info ot the instrument

The pixel scale information is stored in the instruments file (/telescopes/instruments.py)
The PSF and pixel scale information are stored in the instrument's band file (/telescopes/instruments.py)
The noise level is stored in the surveys file (/telescopes/surveys.py)

For each selection, the dictionary info from /telescopes/main_info is read.
The structure is as follow. To read Euclid's NIR's zero point:
     - info['Euclid']["Instruments"]['Euclid_NIR']["bands"][main_band]['zp']

The galaxy simulation procedure are done in sim_field(...) and sim_and_save_fields(...) in /utils/diverse_utils
The plotting is done by plot_fields in /utils/plot_galaxies.py
"""

# SurViZ logo
st.image('surviz_black_long.png')

# Description and README. The references are in image_depth_refs /telescopes/references.py
st.markdown('# ✨ Galaxy field  \n ')
description = st.expander("README")
description.markdown('For each survey, you can see the same galaxy field, simulated with galsim. Each galaxy is simulated with the appropriate pixel scale and PSF. The flux is computed with the appropriate zero-point of the instrument, and we then add a Gaussian noise centered on zero, with an std estimated for each survey. \n The routine used to generate the fields can be found in utils/diverse_utils. It is not executed live for computing time reasons. \n For Cosmos-Web, which have different exposure time depending on the area, we took the depth of two exposures.' + image_depth_refs)

# Multi Select the telescopes. Default Euclid, JWST
telescopes = st.sidebar.multiselect(
        "Select the telescopes",
        list(info.keys()),
        default=["Euclid", 'JWST']
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
        st.sidebar.markdown(f'# {telescope}') # Write the telescope name to separate clearly that we are selecting the instruments of this telescope
        telescope_survey = st.sidebar.multiselect(
                    "Select the Surveys",
                    list(info[telescope]['surveys'].keys()),
                    default=list(info[telescope]['surveys'].keys())[0]
                    )
        
        # Add the selected survey to the dictionary of this the current telescope
        selected_surveys[telescope] = telescope_survey

        # Add the selection of the instrument, with as many columns as the number of surveys for better display
        cols = st.sidebar.columns(len(selected_surveys[telescope]))

        # Loop through the surveys
        for i, survey in enumerate(selected_surveys[telescope]):
            with cols[i]:
                st.markdown(f'{survey}') # Write the Survey name to separate clearly that we are selecting the instruments of this telescope's survey

                # Selection of the instruments. Default is the first instrument listed in the dictionary
                survey_instrument =  st.multiselect(
                        f" Select the instruments {i*' '} ",
                        list(info[telescope]['surveys'][survey]['instruments'].keys()),
                        default=list(info[telescope]['surveys'][survey]['instruments'].keys())[0])

                # Add the selected instruments to the dictionary of this the current telescope's survey
                selected_instruments[telescope][survey] = survey_instrument
                nb_to_plot += len(survey_instrument)
    
    # Call the plotting routine
    fig = plot_fields(telescopes, selected_surveys, selected_instruments, info, nb_to_plot)

    # Plot the figure
    st.pyplot(fig)