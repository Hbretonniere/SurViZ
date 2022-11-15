import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from telescopes.main_info import info
from utils.plots import plot_fields
from telescopes.references import image_depth_refs

st.markdown('# ✨ Galaxy field  \n ')
description = st.expander("README")

description.markdown('For each survey, you can see the same galaxy field, simulated with galsim. Each galaxy is simulated with the appropriate pixel scale and PSF. The flux is computed with the appropriate zero-point of the instrument, and we then add a Gaussian noise centered on zero, with an std estimated for each survey. \n The routine used to generate the fields can be found in utils/diverse_utils. It is not executed live for computing time reasons.' + image_depth_refs)

telescopes = st.sidebar.multiselect(
        "Select the telescopes",
        list(info.keys()),
        default=["Euclid", 'JWST']#, "HST"]
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
    # st.sidebar.markdown('Select the instruments for each survey')

    cols = st.sidebar.columns(len(selected_surveys[telescope]))
    for i, survey in enumerate(selected_surveys[telescope]):
        with cols[i]:
            st.markdown(f'{survey}')
            survey_instrument =  st.multiselect(
                    f" Select the instruments {i*' '} ",
                    list(info[telescope]['surveys'][survey]['instruments'].keys()),
                    default=list(info[telescope]['surveys'][survey]['instruments'].keys())[0])
            selected_instruments[telescope][survey] = survey_instrument
            nb_to_plot += len(survey_instrument)

fig = plot_fields(telescopes, selected_surveys, selected_instruments, info, nb_to_plot)
st.pyplot(fig)