# Spotify token
# BQDwDCa79PuhtU2BVMl_dbYSm4-A_kk6-dzFoxIbqiR8KEsKlYWaEhiLnDcD4g69W3v9mjom44VFqZBsZYsJDvxSdRg8e9wJCAaNtcPhgSEElTUhmIglDquMFeMBXxl96fJbsmZtIghFbwIczVAWTbdWPa9ZtEWdVotH7h0XPwnzfikqnNj4ww

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

