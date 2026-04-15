#Linux basics page

import streamlit as st
import subprocess

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



st.title("Linux Basics 💻")

st.write("Try basic Linux commands safely:")

allowed_commands = ["ls", "pwd", "cat", "echo", "cd"]

with st.expander("Click to try Linux commands"):
    user_command = st.text_input("Enter a Linux command:")

    if user_command:
        cmd = user_command.split()[0]

        if cmd in allowed_commands:
            try:
                result = subprocess.run(
                    user_command,
                    shell=True,
                    capture_output=True,
                    text=True
                )

                if result.stdout:
                    st.code(result.stdout, language="bash")

                if result.stderr:
                    st.error(result.stderr)

            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.error(f"Command not allowed. Try: {', '.join(allowed_commands)}")