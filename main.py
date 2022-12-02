# Spotify token
# 

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

DATABASE_LOCATION = "sqlite:///my_played_tracks.sqlite"
USER_ID = os.getenv("SPOTIFY_ID") #spotify ID
TOKEN = os.getenv("SPOTIFY_TOKEN")

if __name__ == "__main__":

    # Extract part of the ETL process

    # Headers for the Spotify API
    headers {
        "Accept": "application/json",
        "Content-Type": "application/json"
        "Authorization" : "Bearer {token}".format(token=TOKEN)
    }