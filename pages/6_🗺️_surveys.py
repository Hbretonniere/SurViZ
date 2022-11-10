import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from telescopes.main_info import info
from utils.plots import plot_surveys

st.markdown('# Surveys visualisation \n You can explore here the surveys footprints. The shapes and exact positions are not perfect, but estimated from public data.')
telescopes = st.sidebar.multiselect(
        "Select the telescopes",
        list(info.keys()),
        default=["Euclid"]#, "HST"]
    )

selected_surveys = {}
for telescope in telescopes:
    selected_surveys[telescope] = {}
     # SELECTION OF THE SURVEY
    st.sidebar.markdown(f'# {telescope}')
    telescope_survey = st.sidebar.multiselect(
                "Select the Surveys",
                list(info[telescope]['surveys'].keys()),
                default=list(info[telescope]['surveys'].keys())[0]
                )
    selected_surveys[telescope] = telescope_survey

fig = plot_surveys(telescopes, selected_surveys)
st.pyplot(fig)