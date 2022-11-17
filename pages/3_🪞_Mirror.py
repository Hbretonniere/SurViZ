
import streamlit as st
import numpy as np
from telescopes.main_info import info
from utils.plots import plot_mirrors, plot_fovs
from telescopes.references import mirrors_refs

"""
Visualisation of the mirrors and fields of view
The user have to select the telescopes he want to display. For each selected telescope,

The mirror information are stored in the instruments file (/telescopes/telescopes.py)
For each selection, the dictionary info from /telescopes/main_info is read.
The structure is as follow. To read Euclid's mirror, we read:
     - info['Euclid']["mirror"]
To read the FOV:
    -info['Euclid]['fov']

The plotting is done by plot_mirrors and plot_fov in /utils/plot.py
"""

# Display SurViZ logo
st.image('surviz_black_long.png')

# Description and README. The references are in mirrors_ref in /telescopes/references.py
st.markdown('# 🪞 Mirrors and Filed of View visualisation')
description = st.expander("README")
description.markdown(mirrors_refs)
st.markdown('Is shown the primary mirror size. Note that the particular shapes are not respected. \n ### Scroll for the FoV plot')

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
    # Call mirror plot routine
    fig_mirrors = plot_mirrors(info, telescopes)
    # Plot the mirrors
    st.pyplot(fig_mirrors)
    
    # Call FOV plot routine
    fig_fovs = plot_fovs(info, telescopes)
    # Plot the FOVs
    st.pyplot(fig_fovs)