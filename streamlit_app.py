import streamlit as st
import pandas as pd

st.title('Stock Market Prediction')

st.info('Stock Market Prediction using NN')

with st.expander('Data'):
  st.write('**Raw Data**')
  df  = pd.read_csv('https://raw.githubusercontent.com/RoyR02/Stock-pred1/master/AAPL.csv',nrows= 10)
  df
import streamlit as st
import subprocess
import os
import sys
import git

# Function to clone and install a library from a GitHub repository
def install_library(repo_url):
    try:
        # Clone the repository
        repo_name = repo_url.split('/')[-1].replace('.git', '')
        repo_path = os.path.join(os.getcwd(), repo_name)
        
        if os.path.exists(repo_path):
            st.warning(f"Repository '{repo_name}' already exists.")
        else:
            st.info(f"Cloning repository '{repo_name}'...")
            git.Repo.clone_from(repo_url, repo_name)
            st.success(f"Repository '{repo_name}' cloned successfully.")
        
        # Install the library using pip
        st.info(f"Installing library from '{repo_name}'...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", repo_path])
        st.success(f"Library '{repo_name}' installed successfully.")
        
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Streamlit app interface
st.title("Python Library Installer from GitHub")

repo_url = st.text_input("Enter GitHub Repository URL:")

if st.button("Install Library"):
    if repo_url:
        install_library(repo_url)
    else:
        st.warning("Please enter a valid GitHub repository URL.")


