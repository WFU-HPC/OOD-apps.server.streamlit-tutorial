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


st.title("Connect to Cluster")

st.write("Access Wake Forest's DEAC cluster:")

if st.button("Connect to Cluster"):
    st.markdown(
        "[Go to WFU DEAC Dashboard](https://csc.deac.wfu.edu/pun/sys/dashboard)"
    )
