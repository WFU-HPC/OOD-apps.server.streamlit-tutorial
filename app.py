import streamlit as st

# Background styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #788c9f;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#Beginning of website
st.title("Supercomputer Access Portal")

st.write("""
Welcome to DEAC Connect! A resource for students to better understand Wake Forest's most advanced 
technology. Use the sidebar (arrows in top left) to navigate:

- Learn Linux basics
- Connect to the cluster
- Explore DEAC resources
- Use cheat sheets
- Try DeacQuest
""")