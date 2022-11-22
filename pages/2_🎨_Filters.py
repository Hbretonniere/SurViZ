"""
Visualisation of the filters
The user have to select the telescopes he want to display. For each selected telescope,
a new section will appear in the left panel, to chose the instrument corresponding to the 
telescope. 

The filters information are stored in the instruments file (/telescopes/instruments.py)
For each selection, the dictionary info from /telescopes/main_info is read.
The structure is as follow. To read Euclid's NIR's Y band, we read:
     - info['Euclid']["Instruments"]['Euclid_NIR']["bands"][Y]

By default, when selecting an instrument, all bands are displayed, but you can then remove some.
For some, you can also restrict to a survey, become some surveys do not use the whole range of the instrument's filters

The plotting is done by plot_bands in /utils/plot.py
"""


import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from telescopes.main_info import info
from utils.plots import plot_bands
from telescopes.references import filters_refs


# SurViZ logo
st.image('surviz_black_long.png')


# Description and README. The references are in filters_ref in /telescopes/references.py
st.markdown('# 🎨 Filters visualisation \n ')
description = st.expander("README")
description.markdown(filters_refs)
st.markdown('You can see here the filters of the different instruments. Note that for now, the shape and sensitivity are not correct: the y-axis is arbitrary, and the differences are just here for a better visualisation')

# Multi Select the telescopes. Default Euclid, Rubin/LSST
telescopes = st.sidebar.multiselect(
        "Select the telescopes",
        list(info.keys()),
        default=["Euclid", 'Rubin']
    )

# Warning and stop if no telescope selected
if len(telescopes) == 0:
    st.markdown('## Please select at least one telescope')

else:
    # Initialise the selected bands and instruments. THey will be dictionary to keep all the information necessary
    selected_bands = {}
    selected_instruments = {}
    selected_surveys = {}

    # Adding some option for the plot style, with two columns for better display of the buttons.
    col1, col2 = st.columns(2)
    with col1:
        fill = st.checkbox('Filled style') # the rectangle representing the filters will be filled with transparency
    with col2:
        log = st.checkbox('Logarithmic scale')  # will put the x-axis to log

    # Loop through selected telescopes
    for telescope in telescopes:
        selected_bands[telescope] = {}
        
        # Selection of the instruments. Default is the first instrument listed in the dictionary
        st.sidebar.markdown(f'# {telescope}') # Write the telescope name to separate clearly that we are selecting the instruments of this telescope
        telescope_instrument = st.sidebar.multiselect(
                    "Select the instruments",
                    list(info[telescope]['instruments'].keys()),
                    default=[list(info[telescope]['instruments'].keys())[0]])
        
        # Add the selected instruments to the dictionary of this the current telescope
        selected_instruments[telescope] = telescope_instrument

        # Add restriction to the survey for some missions (when necessary)
        restrict_to_survey = None
        selected_survey = None
        if telescope == 'JWST':
            restrict_to_survey = st.sidebar.checkbox('Restrict to a specific survey')
        
        # Loop through the selected instruments of the current telescope
        for instrument in selected_instruments[telescope]:

            # If we want to restrict ot a survey, the options of band selections are limited to the one listed in
            # info[telescope]['surveys'][survey]['filters']
            # else, all bands of the instruments
            if restrict_to_survey:
                selected_survey = st.sidebar.radio(
                'Select the survey',
                list(info[telescope]['surveys'].keys()),
                index=0)
                available_filters = info[telescope]['surveys'][selected_survey]['filters']
            else:
                available_filters = list(info[telescope]['instruments'][instrument]['bands'].keys())

            # Selection of all the available bands to display. Default are all.
            instrument_bands =  st.sidebar.multiselect(
                    f" Select the filters ({instrument})",
                    list(info[telescope]['instruments'][instrument]['bands'].keys()),
                    default=available_filters)
            selected_bands[telescope][instrument] = instrument_bands

    # Call the filters plotting routine
    fig = plot_bands(info, telescopes, selected_instruments, selected_bands, selected_survey, fill, log)

    # Plot the figure
    st.pyplot(fig)