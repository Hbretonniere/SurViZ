import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from telescopes.main_info import info
from utils.plots import plot_galaxies
from telescopes.references import image_quality_refs

st.markdown('# 🌌 Galaxy visualisation \n')
description = st.expander("README")
description.markdown('For each survey, the galaxy is simulated from an Illustris-TNG galaxy, and rescaled to the pixel-scale of the instrument, then convolved by the aproximate PSF. \n We do not add noise, considering that the galaxy is very near by. To see the impact of the depth in the different surveys, see the Galaxy Field tab. \n ' + image_quality_refs)
telescopes = st.sidebar.multiselect(
        "Select telescopes to display",
        list(info.keys()),
        default=["Euclid", 'JWST', 'SDSS']#, "HST"]
    )

nb_to_plot = 0
selected_surveys = {}
selected_instruments = {}
for telescope in telescopes:
    selected_instruments[telescope] = {}

    # SELECTION OF THE SURVEY
    st.sidebar.markdown(f'## {telescope}')

    telescope_instrument =  st.sidebar.multiselect(
            f"Select instruments",
            list(info[telescope]['instruments'].keys()),
            default=list(info[telescope]['instruments'].keys())[0])
    selected_instruments[telescope] = telescope_instrument
    nb_to_plot += len(telescope_instrument)

fig = plot_galaxies(info, telescopes, selected_instruments, nb_to_plot)
st.pyplot(fig)