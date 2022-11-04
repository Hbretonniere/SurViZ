import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys
from telescopes.main_info import info
# sys.path.append('../utils')
from utils.general_description import description


telescopes = st.sidebar.multiselect(
        "Select telescopes to display",
        list(info.keys()),
        default=["Euclid"]#, "HST"]
    )

for telescope in telescopes:
    fig = plt.figure()#figsize=(15, 15))
    fig.patch.set_facecolor('0E1116')
    plt.imshow(mpimg.imread(f"data/logos/{telescope}.jpeg"))
    plt.axis('off')
    st.pyplot(fig)
    st.markdown(description[telescope]['general_description'])
    st.markdown('### Instruments:')
    for instrument in list(description[telescope]['Instruments'].keys()):
        st.markdown("- " + description[telescope]['Instruments'][instrument])
    st.markdown('### Surveys:')
    for survey in list(description[telescope]['Surveys'].keys()):
        st.markdown("- " + description[telescope]['Surveys'][survey])