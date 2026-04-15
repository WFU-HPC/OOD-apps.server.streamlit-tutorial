#Bashcrawl page

import streamlit as st
import subprocess
import os

# 1. Page Config
st.set_page_config(page_title="BashCrawl")
st.markdown("<style>.stApp {background-color: #C4C3D0;}</style>", unsafe_allow_html=True)

st.title("⚔️ BashCrawl Adventure ⚔️ ")
st.markdown("Do not stress if you get confused, you can always restart!")
st.markdown("When stuck, remember to check your location, read the outputs, and try different commands (pwd, ls, cat, cd). Check out the command cheat sheet if you need some direction!")

# 2. Robust Path Finding
# This finds the 'bashcrawl' folder sitting next to your 'pages' folder
CURRENT_SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__)) # inside 'pages'
BASE_APP_DIR = os.path.dirname(CURRENT_SCRIPT_PATH)             # 'my_streamlit_app'
GAME_DIR = os.path.join(BASE_APP_DIR, "bashcrawl")

# 3. Initialize Game State
if 'current_path' not in st.session_state or not os.path.exists(st.session_state.current_path):
    st.session_state.current_path = os.path.join(GAME_DIR, "entrance")

# 4. Terminal Interface
with st.expander("Terminal Console", expanded=True):
    # Display current location relative to the game folder
    try:
        display_path = os.path.relpath(st.session_state.current_path, GAME_DIR)
    except:
        display_path = "entrance"
        st.session_state.current_path = os.path.join(GAME_DIR, "entrance")
        
    st.info(f"📍 **Location:** `bashcrawl/{display_path}`")

    user_input = st.text_input("Enter command:", key="bash_input").strip()

    if user_input:
        parts = user_input.split()
        if not parts:
            st.rerun()
        
        cmd = parts[0].lower()
        allowed = ["ls", "pwd", "cat", "cd", "help", "clear"]

        if cmd in allowed:
            # Handle 'cd' (Change Directory)
            if cmd == "cd":
                target = parts[1] if len(parts) > 1 else ".."
                new_path = os.path.normpath(os.path.join(st.session_state.current_path, target))
                
                if new_path.startswith(GAME_DIR) and os.path.isdir(new_path):
                    st.session_state.current_path = new_path
                    st.rerun()
                else:
                    st.error("You can't go that way!")
            
            # Handle other commands
            else:
                result = subprocess.run(
                    user_input, shell=True, cwd=st.session_state.current_path,
                    capture_output=True, text=True
                )
                if result.stdout: st.code(result.stdout, language="bash")
                if result.stderr: st.error(result.stderr)
        else:
            st.error(f"Command '{cmd}' not allowed. Try: ls, cd, cat, pwd")

if st.button("Reset to Entrance"):
    st.session_state.current_path = os.path.join(GAME_DIR, "entrance")
    st.rerun()