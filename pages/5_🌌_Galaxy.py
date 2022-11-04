import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from telescopes.main_info import info
from utils.plots import plot_galaxies

st.markdown('# 🌌 Galaxy visualisation \n')
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