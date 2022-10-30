import matplotlib.pyplot as plt
import streamlit as st
import matplotlib.image as mpimg

st.set_page_config(
    page_title="Home page",
    page_icon="👋",
    layout="centered")

st.write("## 👋 Welcome to SurViZ, your best tool to compare and explore galaxy SurVeys! \n ")

st.markdown(
    """
    ### Select on the left panel what you want to explore:

    - With 🎨 Bands, you will explore the bands of each telescopes' instruments.

    - With 🪞 Mirror , you will explore the size of the telescopes' primary mirror, and there field of view.

    - With ✨ Fields Of galaxies, you will explore the surveys and instruments' depths in a simulated galaxy field.

    - With 🌌 Galaxy, you will explore the the surveys and instruments'image quality (resolution and PSF) in a TNG galaxy.
    \n  """
)

fig = plt.figure(figsize=(27, 15))
plt.imshow(mpimg.imread("data/logos.jpg"), aspect="auto")
plt.axis('off')
st.pyplot(fig)