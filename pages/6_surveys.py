import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from telescopes.main_info import info
from utils.plots import plot_surveys

st.markdown('# Surveys visualisation \n You can see here the filters of the different instruments. Note that for now, the shape and sensitivity are not correct: the y-axis is arbitrary, and the differences are just here for a better visualisation ')
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