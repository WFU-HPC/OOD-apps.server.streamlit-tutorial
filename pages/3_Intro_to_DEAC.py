#Intro to DEAC page

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

st.title("Intro to the DEAC")

st.markdown("""
Welcome to DEAC! Wake Forest's supercomputer, powering over 16 departments across campus.  
The system processed over 21 million core-hours and more than 650,000 tasks last year. Since 2020, 
the High Performance Computer (HPC) has had over 3 million tasks submitted to its system. 
It was initially developed in July 2002 to centralize computing environment for Wake Forest.

This resource enables staff, faculty, and students to accelerate their research and not let 
technology hold them back.  With over 500 accounts on the DEAC (a growing number!), the system 
has 90 compute nodes, 4,500 CPU cores, 38 TB of memory, and 280 TB of storage.  These numbers and 
variables may be unfamiliar, and that's ok! Think of a regular laptop as a bike and Wake's HPC 
system as an Airbus A380. Not only does the supercomputer have more power, and not only can it 
do tasks much faster, it's operating at a completely different level!

This is extremely important for present-day researchers. Being able to split data, run sets quickly
and efficiently, and have access to a resource with much more computing power that can be accessed simply
through a personal laptop is revolutionary. Students can also use this resource! Using the HPC system is a
great way to get more practice with Linux (the operating system used on the DEAC), understanding the power
and need for resources such as a supercomputer at institutions at Wake, and more. 

information gathered from Wake Forest's HPC news article: 
https://news.wfu.edu/2022/03/31/high-performance-computing-collaborations-power-research-learning/ 
""")