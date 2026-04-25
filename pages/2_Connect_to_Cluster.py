#Connecting to cluster page 

import streamlit as st

# Background styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #C4C3D0;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.title("Connect to Cluster 💻")

st.write("Access Wake Forest's DEAC cluster:")

if st.button("Connect to Cluster"):
    st.markdown(
        "[Go to WFU DEAC NotebookLM --the supercomputer's very own AI chat bot!](https://notebooklm.google.com/notebook/7f5b7f16-36a1-4595-a4c1-bc3d3e7d04d0?addSource=true)"
        "[Go to DEAC Wiki -- DEACs expansive resource page] (https://deac-wiki.readthedocs.io/en/latest/index.html#)"
    )
