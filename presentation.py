import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

#st.sidebar.success("Select a demo above.")

title_container = st.container()
col1,mid, col2 = st.columns([1,1,20])
image = Image.open('NWG_Logo.png')
with title_container:
    with col1:
        st.image(image, width=64)
    with col2:
        st.markdown('<h1 style="color: purple;">Natwest Intelligence Agent</h1>',
                    unsafe_allow_html=True)

# Subtitle
st.markdown("# Our Solution")

# Paragraph
st.write("""Relationship managers spend hours making individual personalised reports for every customer based on their 
            business needs, financial account and credit worthiness . Our interactive intelligence agent aims at making
            things easier for the branch relationship managers by generating these reports for them and reducing 
            repetitive work. Not only would this free relationship managers from hours spent on processing information 
            manually but would also enable them to focus on more creative and innovative space to add further value to 
            tangible business outcomes by making deeper customer relations.""")

workflow_sketch = Image.open('WorkFlow.jpg')
st.image(workflow_sketch)

# Bulleted points
st.write("- Summerise financial accounts in seconds")
st.write("- Faster turnaround time for customers")
st.write("- Reduces repetitive tasks, freeing up Relationship Managers to have higher quality conversations with customers")
st.write("- Time and Cost Savings")
st.write("- Minimises human business risk")

# Subtitle
st.markdown("# Implemetation and Design #")
# Paragraph
st.write("")

# Add a title
image_solution = Image.open('solutions.jpg')
st.image(image_solution)
