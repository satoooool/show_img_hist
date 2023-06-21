import numpy as np
import pandas as pd
import streamlit as st
from skimage.io import imread


# download the image
img_url = 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjUF9l4BpMLj67ZckTKiASOPxsVpADYGZvV7wrNxUmE9nbgKOSieF9Kzzxqjm27IffqG0Te87P2Zdp7xo-0neAinwfG30KYS8W9-MtH2RjbcRwHlM_nKeTJNM7IY5J2WAEyvTlRS-nfXXLVrFrYrpvb7JrCp1BuRYvQyg8mvdfZNju-0A0QdS8jpAK2tw/s832/ai_dance_character.png'

im = imread(img_url)

st.image(im, caption='image from wikimedia commons',
         use_column_width=True)


# show histgram of all colors
hist_red, _ = np.histogram(im[:, :, 0], bins=64)
hist_green, _ = np.histogram(im[:, :, 1], bins=64)
hist_blue, _ = np.histogram(im[:, :, 2], bins=64)
hist = np.stack((hist_red, hist_green, hist_blue), axis=1)

df_hist = pd.DataFrame(hist, columns=['R', 'G', 'B'])
st.bar_chart(df_hist)


# choose one color
color = st.radio(
    "choose R, G, or B",
    ('R', 'G', 'B'))
if color == 'R':
    df_hist = pd.DataFrame(hist_red)
    st.bar_chart(df_hist)
if color == 'G':
    df_hist = pd.DataFrame(hist_green)
    st.bar_chart(df_hist)
if color == 'B':
    df_hist = pd.DataFrame(hist_blue)
    st.bar_chart(df_hist)
