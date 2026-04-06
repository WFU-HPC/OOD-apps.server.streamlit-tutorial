import streamlit as st
import subprocess

#Command to run the website:

#streamlit run app.py \
  #--server.address 0.0.0.0 \
  #--server.port 8501 \
  #--server.enableCORS false \
  #--server.enableXsrfProtection false

# Background color and header
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

st.title("Supercomputer Access Portal")
st.write("Welcome to DEAC Connect! Use this app to connect to and learn more about HPC resources.")

# Sidebar navigation
page = st.sidebar.radio(
    "Home page navigation",
    ["Linux basics", "Connect to cluster", "Intro to the DEAC", "Cheat sheet", "Bashcrawl (Coming soon!)"]
)

#Interactive portion

allowed_commands = ["ls", "pwd", "cat", "echo"]

# Expander acts like a button to reveal interactive portion
with st.expander("Click to try Linux commands!"):
    user_command = st.text_input("Enter a Linux command:")

    if user_command:
        cmd = user_command.split()[0]
        if cmd in allowed_commands:
            try:
                result = subprocess.run(
                    user_command, shell=True, capture_output=True, text=True
                )
                if result.stdout:
                    st.code(result.stdout, language="bash")
                if result.stderr:
                    st.error(result.stderr)
            except Exception as e:
                st.error(f"Error running command: {e}")
        else:
            st.error("Command not allowed! Try: " + ", ".join(allowed_commands))

# Button to connect to the cluster
if st.button("Connect to Cluster"):
    st.write("Connecting...")
    st.markdown(
        "[Go to WFU Deac dashboard](https://csc.deac.wfu.edu/pun/sys/dashboard)",
        unsafe_allow_html=True
    )

# Button to learn about the supercomputer
if st.button("Learn about Wake's supercomputer! #COMMENT: make this a readme file to keep outside of using internet?"):
    st.write("Opening supercomputer info...")
    st.markdown(
        "[Go to WFU Deac information website](https://news.wfu.edu/2022/03/31/high-performance-computing-collaborations-p)",
        unsafe_allow_html=True
    )
# Button to get to command cheat sheet
if st.button("Linux command cheat sheet #COMMENT: make this a readme file to keep outside of using internet?"):
    st.write("Accessing document...")
    st.markdown("[Command cheat sheet document](https://docs.google.com/document/d/1XdjdXbHq5_yH27qZmwNT5LrSORgitLDd9gy8GlADl_k/edit?usp=sharing)", unsafe_allow_html=True)

# Button to get to bashcrawl -- interactive portion
if st.button("Bashcrawl: learn how to use commands through a game!"):
    st.write("Accessing document...")
    st.markdown("[Bashcrawl game instructions document](https://docs.google.com/document/d/1wXQGkRkD1tvM2-y9DoZKudt-WQpaC6nz4qLeBAKMBlo/edit?usp=sharing)", unsafe_allow_html=True)