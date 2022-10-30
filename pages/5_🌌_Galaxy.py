import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from telescopes.main_info import info
from utils.plots import plot_galaxies

st.markdown('# 🌌 Galaxy visualisation \n')
telescopes = st.sidebar.multiselect(
        "Select telescopes to display",
        ["Euclid", "JWST", "HST", "Rubin"],
        default=["Euclid"]#, "HST"]
    )

nb_to_plot = 0
selected_surveys = {}
selected_instruments = {}
for telescope in telescopes:
    selected_instruments[telescope] = {}

    # SELECTION OF THE SURVEY
    st.sidebar.markdown(f'# {telescope}')
    telescope_survey = st.sidebar.multiselect(
                "Select the Surveys",
                list(info[telescope]['surveys'].keys()),
                default=list(info[telescope]['surveys'].keys())[0]
                )
    selected_surveys[telescope] = telescope_survey
    cols = st.sidebar.columns(len(selected_surveys[telescope]))

    for i, survey in enumerate(selected_surveys[telescope]):
        with cols[i]:
            survey_instrument =  st.multiselect(
                    f" {survey}",
                    list(info[telescope]['surveys'][survey]['instruments'].keys()),
                    default=list(info[telescope]['surveys'][survey]['instruments'].keys())[0])
            selected_instruments[telescope][survey] = survey_instrument
            nb_to_plot += len(survey_instrument)

fig = plot_galaxies(info, telescopes, selected_surveys, selected_instruments, nb_to_plot)
st.pyplot(fig)