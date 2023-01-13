
"""
Visualisation of the mirrors and fields of view
The user have to select the telescopes he want to display. For each selected telescope,

The mirror information are stored in the instruments file (/telescopes/telescopes.py)
For each selection, the dictionary info from /telescopes/main_info is read.
The structure is as follow. To read Euclid's FOV we read: 
    -info['Euclid]['fov']

The plotting is done by plot_mirrors and plot_fov in /utils/plot.py
"""


import streamlit as st
import numpy as np
from telescopes.main_info import info
from utils.plots import plot_mirrors, plot_fovs
from telescopes.references import mirrors_refs


# Display SurViZ logo
st.image('surviz_black_long.png')

# Description and README. The references are in mirrors_ref in /telescopes/references.py
st.markdown('# 👁️ Filed of View visualisation')
description = st.expander("README")
description.markdown(mirrors_refs)
st.markdown('Field of View plot, The precise shapes are not respected')

# Multi Select the telescopes. Default Euclid, Rubin/LSST
telescopes = st.sidebar.multiselect(
        " Select telescopes",
        list(info.keys()),
        default=["Euclid", 'Rubin']
    )

# Warning and stop if no telescope selected
if len(telescopes) == 0:
    st.markdown('## Please select at least one telescope')

else:
    # Call FOV plot routine
    fig_fovs = plot_fovs(info, telescopes)
    # Plot the FOVs
    st.pyplot(fig_fovs)