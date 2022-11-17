import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys
from telescopes.main_info import info
from utils.general_description import description


"""
General information about the mission. 
By default, all telescopes are selected.
For each one, it charges the image with the logo, and then read the text written in the 
utils/general_description dictionary.
The dictionary is formatted with sub dictionary:
For each telescope name, you have a key for the Instruments and the Surveys. This way, we can
loop through the information, have a standardized format and an easier readability of the dictionary.

"""

telescopes = st.sidebar.multiselect(
        "Select telescopes to display",
        list(info.keys()),
        default=list(info.keys())
    )

for telescope in telescopes:
    # Display logo
    st.image(f'./data/logos/{telescope}.jpeg')
    st.markdown(description[telescope]['general_description'])

    # Euclid is for now the only mission that I have completed. Message elsewhere
    if telescope != 'Euclid':
        complete="(Non exhaustive list)"
    else:
        complete=""

    # Loop through the instruments
    # add warning if not complete
    st.markdown('### Instruments '+complete+':')
    for instrument in list(description[telescope]['Instruments'].keys()):
        st.markdown("- " + description[telescope]['Instruments'][instrument])
    
    # Loop through the instruments
    # add warning if not complete
    st.markdown('### Surveys '+complete+':')
    for survey in list(description[telescope]['Surveys'].keys()):
        st.markdown("- " + description[telescope]['Surveys'][survey])