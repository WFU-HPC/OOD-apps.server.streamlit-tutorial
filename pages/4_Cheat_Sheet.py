import streamlit as st

# Background styling
st.markdown("""
<style>
.stApp {
    background-color: #C4C3D0;
}
</style>
""", unsafe_allow_html=True)

st.title("Linux Command Cheat Sheet")

st.write("Quick reference for common Linux commands:")

st.markdown("""
**What is Linux?**  
Linux is the operating system that the DEAC runs on. This means it runs programs, manages files, software, and hardware, allocates resources, transfers data between the hard drive and memory, and much more!

--- Common Linux commands ---  
- mkdir -- creates a directory where files can be stored. Must have a different name than other directories (can use the command "mkdir -p" to always create a parent directory). Ex: mkdir /home/$USERNAME/activities  
- mkdir -p -- safer option when creating directories; will not throw error if directory already exists  
- cat -- view file contents, ex: `cat project1.txt`  
- ls -- list files in current directory  
- pwd -- print working directory  
- echo -- display text or variables  
- cd -- change directory  
- export -- create new environment variables  
- man -- read the manual for commands, ex: `man mkdir` or `man pwd`
""")

st.markdown("""
--- Slurm Commands ---  
- squeue -- shows current jobs submitted to the cluster  
- sbatch -- submit a job to the scheduler  
- sacct -- show job history and status  
- nano -- edit .slurm files
""")

st.markdown("""
--- Module system commands ---  
- module avail -- show installed software packages  
- module show -- show info about a software package  
- module load -- load a software package  
- module purge -- reset loaded modules
""")