"""
Visualisation of the surveys footprint
The user have to select the telescopes he want to display. For each selected telescope,
a new section will appear in the left panel, to chose the surveys corresponding to the 
telescope. 

For now, we have a plotting routine for each survey, as it is hard to automatize.
Each footprint is computed in /utils/plot_surveys.py
The plotting is done by plot_surveys in /utils/plot.py
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from telescopes.main_info import info
from utils.plots import plot_surveys
from telescopes.references import footprint_refs


# SurViZ logo
st.image('surviz_black_long.png')

# Description and README. The references are in footprint_refs in /telescopes/references.py
description = st.expander("README")
description.markdown(footprint_refs)
st.markdown('# Surveys visualisation \n You can explore here the surveys footprints. The shapes and exact positions are not perfect, but estimated from public data.')

# Multi Select the telescopes. Default Euclid (Wide)
all = st.sidebar.checkbox('Plot all telescopes and surveys available')

if all:
    default_tel = list(info.keys())
else:
    default_tel = ["Euclid"]


telescopes = st.sidebar.multiselect(
            "Select the telescopes",
            list(info.keys()),
            default=default_tel
        )

# Initialise the selected surveys. THey will be dictionary to keep all the information necessary
selected_surveys = {}

# Loop through selected telescopes
for telescope in telescopes:
    selected_surveys[telescope] = {}

    # Selection of the survey. Default is the first survey listed in the dictionary
    st.sidebar.markdown(f'# {telescope}') # Write the telescope name to separate clearly that we are selecting the surveys of this telescope
    if all:
        default_surveys = list(info[telescope]['surveys'].keys())
    else:
        default_surveys = list(info[telescope]['surveys'].keys())[0]
    telescope_survey = st.sidebar.multiselect(
                "Select the Surveys",
                list(info[telescope]['surveys'].keys()),
                default=default_surveys
                )

    # Add the selected surveys to the dictionary of this the current telescope
    selected_surveys[telescope] = telescope_survey

# Call the plotting routine
fig = plot_surveys(telescopes, selected_surveys)

# Plot the figure
st.plotly_chart(fig)