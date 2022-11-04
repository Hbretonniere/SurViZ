
import streamlit as st
import numpy as np
from telescopes.main_info import info

from utils.plots import plot_mirrors, plot_fovs


st.markdown('# 🪞 Mirrors and Filed of View visualisation \n Is shown the primary mirror size. Note that the particular shapes are not respected. \n ### Scroll for the FoV plot')
telescopes_mirrors = st.sidebar.multiselect(
        " Select telescopes",
        ["Euclid", "JWST", "HST", "Rubin"],
        default=["Euclid"]#, "HST"]
    )

fig_mirrors = plot_mirrors(info, telescopes_mirrors)
st.pyplot(fig_mirrors)

fig_fovs = plot_fovs(info, telescopes_mirrors)
st.pyplot(fig_fovs)