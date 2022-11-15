import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from telescopes.main_info import info
from utils.plots import plot_bands
from telescopes.references import filters_refs
from utils.diverse_utils import add_logo

# add_logo()
st.image('surviz_black_long.png')


st.markdown('# 🎨 Filters visualisation \n ')
description = st.expander("README")
description.markdown(filters_refs)
st.markdown('You can see here the filters of the different instruments. Note that for now, the shape and sensitivity are not correct: the y-axis is arbitrary, and the differences are just here for a better visualisation')
telescopes = st.sidebar.multiselect(
        "Select the telescopes",
        ["Euclid", "JWST", "HST", "Rubin", "SDSS"],
        default=["Euclid", 'Rubin']#, "HST"]
    )

selected_bands = {}
selected_instruments = {}
col1, col2 = st.columns(2)
with col1:
    fill = st.checkbox('Filled style')
with col2:
    log = st.checkbox('Logarithmic scale')

for telescope in telescopes:
    selected_bands[telescope] = {}
    # SELECTION OF THE INSTRUMENT
    st.sidebar.markdown(f'# {telescope}')
    telescope_instrument = st.sidebar.multiselect(
                "Select the instruments",
                list(info[telescope]['instruments'].keys()),
                default=[list(info[telescope]['instruments'].keys())[0]])
    selected_instruments[telescope] = telescope_instrument

    for instrument in selected_instruments[telescope]:
        instrument_bands =  st.sidebar.multiselect(
                f" Select the filters ({instrument})",
                list(info[telescope]['instruments'][instrument]['bands'].keys()),
                default=list(info[telescope]['instruments'][instrument]['bands'].keys()))
        selected_bands[telescope][instrument] = instrument_bands

fig = plot_bands(info, telescopes, selected_instruments, selected_bands, fill, log)
st.pyplot(fig)