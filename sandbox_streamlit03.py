import streamlit as st
import pandas as pd
from PIL import Image

def my_widget(key):
    st.subheader('Hello there!')
    clicked = st.button("Click me " + key)
    if clicked and key=='first':
        image=Image.open('image01.jpg')
        st.image(image,use_column_width=True,caption="Uho")

# This works in the main area
clicked = my_widget("first")


# And within an expander
my_expander = st.beta_expander("Expand", expanded=True)
with my_expander:
    clicked = my_widget("second")

# AND in st.sidebar!
with st.sidebar:
    clicked = my_widget("third")

options = ["a", "b", "c", "d"]

col1, col2, col3 = st.beta_columns(3)

with col1:
    level_radio = st.radio(
        "Blah blah:", options, index=2
    )

with col2:
    section_filters = st.multiselect(
        "Blah:", sorted(list(options)), sorted(list(options))
    )

with col3:
    st.write('This is Column3')