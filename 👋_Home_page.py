"""

This is the main page, that you have to run with "streamlit run" to launch the app locally.
Streamlit automatically create the tabs in the left sidebar from the .py files located in /pages
Here we just have the home page, with a short description of the tabs, and some images

"""


import matplotlib.pyplot as plt
import streamlit as st
import matplotlib.image as mpimg

st.set_page_config(
    page_title="Home page",
    page_icon="👋",
    layout="centered")


# SurViZ logo
st.image('surviz_black_long.png')

# Main Description
st.markdown("## 👋 Welcome to SurViZ, your best tool to compare and explore galaxy SurVeys!")
st.markdown("Developed by __Hubert Bretonnière__: https://github.com/Hbretonniere/SurViZ")
st.markdown("The app is still under development. Please reach me in the github repo if you have any comments or suggestions.")
st.markdown("For a more quantitative comparison of some of the surveys, you can visit and use galcheat (https://github.com/aboucaud/galcheat)")

# Description of the features. 
st.markdown(
    """
    ### Select on the left panel what you want to explore:

    - With 🔭 General info, you will have a short description of the telescopes, their scientific goals, instruments and surveys.
    
    - With 🎨 Filters, you will explore the spectral bands of each telescopes' instruments.

    - With 👁️ FOV, you will be able to explore the Filed of View of each telescope.

    - With 📈characteristics, you will explore the capacity of the missions regarding filters, resolution and depth.
    
    - With 🌌 Galaxy, you will explore the surveys and instruments' image quality (resolution and PSF) in a TNG galaxy.

    - With ✨ Galaxy fields, you will explore the surveys and instruments' depths in a simulated galaxy field.

    - With 🗺️ Survey footprint, you will visualise the sizes and positions of the various surveys.

    - With 🪞 Mirror , you will explore the size of the telescopes' primary mirror.
    \n  
    
    More information can be found by clicking in the READMEs of each tab.
    """
)

# Mission logos
st.image('data/logos/logos.jpeg')