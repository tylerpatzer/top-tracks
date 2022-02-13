import spotipy
import numpy as np
import pandas as pd 
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from os import environ


while 1: 

    print("Please enter your spotify username.")
    username = input()

    scope = 'playlist-modify-public user-top-read user-library-read' 
    token = SpotifyOAuth(scope=scope, username=username)
    sp = spotipy.Spotify(auth_manager = token)

    try:
      
        user_dict = sp.user(username)        
        df = pd.DataFrame.from_dict(user_dict, orient='index')
        break
       
    except:
        print("The user entered is invalid.")
        print("Please enter a valid user.")

print("Would you like to make a playlist?")
if input() == 'yes':
    print("Enter a name for the playlist")
    name = input()
    print("Enter how many songs you want in the playlist. (1 - 50)")
    num = input()
    playlist = sp.user_playlist_create(username, name)
    playlist_id = playlist["uri"]
    print("Getting your top artists")
    print("we are creating a top songs playlist for you")
    try:

        top_tracks = sp.current_user_top_tracks(num)
    except:
        print("invalid number of tracks")
  
    
    track_data = []
    top_list = top_tracks["items"]
    print(top_list)
    
    for l in range(len(top_list)):
        top_next = top_list[l]["uri"]
        track_data.append(top_next)

   
    sp.playlist_add_items(playlist_id, track_data)
    print("Your top tracks playlist is now populated")
      
else:
    print("Have a nice day...")
