# import libraries
import sqlalchemy
import pandas as pd
from sqlalchemy.orm import sessionmaker
import requests
import json
from datetime import datetime
import datetime
import sqlite3
import os
from dotenv import load_dotenv

# load_dotenv will look for a .env file and if it finds one, it will load the environment variables from it
load_dotenv()

# Spotify TOKEN generation:
# https://developer.spotify.com/console/get-recently-played/

DATABASE_LOCATION = "sqlite:///my_played_tracks.sqlite"
USER_ID = os.getenv("SPOTIFY_ID")  # Spotify ID
TOKEN = os.getenv("SPOTIFY_TOKEN") # Spotify Token (needs to be re-generated when expired)

if __name__ == "__main__":

    # Extract part of the ETL process

    # Structure
    # curl -X "GET" "https://api.spotify.com/v1/me/player/recently-played?limit=10&after=1484811043508" -H 
    # "Accept: application/json" -H 
    # "Content-Type: application/json" -H 
    # "Authorization: Bearer TOKEN"

    # Headers for the Spotify API
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization" : "Bearer {token}".format(token=TOKEN)
    }

    # Convert time to Unix timestamp in miliseconds 
    today                       = datetime.datetime.now()
    yesterday                   = today - datetime.timedelta(days=1)
    yesterday_unix_timestamp    = int(yesterday.timestamp()) * 1000

    # Download all songs you've listened to "after yesterday", which means in the last 24 hours      
    r = requests.get("https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time=yesterday_unix_timestamp), headers = headers)

    if r.status_code == 200:
        print(f"Requests' status OK, code: {r.status_code}.\n")
    else:
        print("Problem with Requests")


    data = r.json()

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    song_names = []
    artist_names = []
    played_at_list = []
    timestamps = []

    # Print songs
    # for song in data["items"]:
    #     print(song["track"]["album"]["artists"][0]["name"], "-", song["track"]["name"])
    #     print(song["played_at"])
    #     print(song["played_at"][0:10])
    #     print()

    # Extracting only the relevant bits of data from the json object      
    for song in data["items"]:
        song_names.append(song["track"]["name"])
        artist_names.append(song["track"]["album"]["artists"][0]["name"])
        played_at_list.append(song["played_at"])
        timestamps.append(song["played_at"][0:10])

    song_dict = {
        "song_name" : song_names,
        "artist_name" : artist_names,
        "played_at" : played_at_list,
        "timestamp" : timestamps
    }
   
    song_df = pd.DataFrame(song_dict)

    print(song_df)
