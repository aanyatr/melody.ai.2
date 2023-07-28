import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie  
import pandas as pd
import numpy as np
from pygame import mixer
st.set_page_config(page_title='Melody.AI', page_icon=":musical_note:",layout='wide')

# animation additions1 : THE SOUNDWAVE 
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
    
lottie_coding = load_lottiefile("soundwave.json")  # replace link to local lottie file

st_lottie(
    lottie_coding,
    speed=1,
    reverse=False,
    loop=True,
    quality="high", # medium ; high
    height=None,
    width=None,
    key=
    None,
)
# --- 
col1, col2 = st.columns([1,5])
with st.container():
 lottie_note = load_lottiefile("hii.json")
with col1:
 st_lottie(
    lottie_note,
    speed=0.5,
    reverse=False,
    loop=True,
    quality="high", # medium ; high
    height=200,
    width=200,
    key=None,
)

# BELOW HEADER TEXT:
with col2:
 st.markdown("# :violet[I'm Melody.AI] :musical_note:")
 st.subheader(':blue[**An AI model used to help you generate customized playlists of your choice**]')
 st.write("I'm eager to assist in coming up with remarkable music for melodies! :musical_score:")
 st.write("[Learn More>](https://www.spotify.com)")

#-- setting a divider:
with st.container():
 st.write("---")

# ---- hamster animation addition 
 lottie_note = load_lottiefile("question.json")
# setting columns for the animation and text
 col3, col4= st.columns([1,2])
 with col3: # calling the animation question
  st_lottie(
    lottie_note,
    speed=0.5,
    reverse=False,
    loop=True,
    quality="high", # medium ; high
    height=500,
    width=400,
    key=None, )
  
# --- about me section:
 with col4:
  st.header('**About me!**')
  st.write("Whether you're embarking on a road trip, flying to a new destination, or exploring new places, we've got the perfect music suggestions for you! ")
  st.write('**1. Share your favorite artists or bands:**')
  st.write('Let us know the names of the artists or bands you currently enjoy listening to. This will help us understand your musical taste and recommend similar artists that will keep you grooving on your travels.')
  st.write('**2. Select a mood for your journey:**')
  st.write("Tell us about the mood you're looking for during your trip. Are you in the mood for upbeat and energetic tracks to keep you pumped up throughout the journey? Or perhaps you'd prefer some relaxing tunes to set a calm and peaceful atmosphere as you explore new places.")
  st.write("**3. Length of playlist:**")
  st.write("Lastly, how long would you like your playlist to be? Do you need music just for a short flight, a day-long road trip, or an entire week of travel? Let us know, and we'll create the perfect playlist to keep you entertained during your adventure.🌴 ")

# --- THE BODY
st.write('---')
st.header('Enter the following details below and get started👇')
col5,col6,col7=st.columns([2,2,4])
with col5:
 st.subheader('Enter your spotify username:')
 user_input = st.text_input(" ", label_visibility="collapsed")

 st.subheader('Enter your mood and playlist type you want:')
 user_mood = st.text_input("Your Mood", label_visibility='collapsed')

# Add a button to start processing the inputs
 if st.button("Generate Playlist"):
    # You can put your playlist generation logic here
    # For example, use the Spotify API to create a personalized playlist
    # based on the user's input.
    st.write("*Playlist generation is in progress...*")
    # Add your playlist generation code here
    with col7:
      df = pd.DataFrame(
    {
        "Artist_Name": ["A-boogie", "BTS", "Britney Spears"],
        "Song Name": ["In the Hood", "Stay Gold", "Toxic"],
        "Vibe Check": [3,7,8],
        "Links": ['www.toxic','fdf','dg']
    })
      st.write(df)

      audio_file = open('audio.mp3', 'rb')
      audio_bytes = audio_file.read()
      st.audio(audio_bytes)
    
with col6:
 lottie_music=load_lottiefile("speaker.json")
 st_lottie(
    lottie_music,
    speed=1,
    reverse=True,
    loop=True,
    quality="high", # medium ; high
    height=250,
    width=300,
    key=None,)
 
