from yahoo_oauth import OAuth2
from dotenv import load_dotenv
import json
import os

load_dotenv()

CLIENT_ID = os.getenv("YAHOO_FANTASY_CLIENT_ID")
CLIENT_SECRET = os.getenv("YAHOO_FANTASY_CLIENT_SECRET")

# Use the variables from os.getenv instead of 'my_key' / 'my_secret'
creds = {
    'consumer_key': CLIENT_ID,
    'consumer_secret': CLIENT_SECRET
}

# Write directly to 'oauth2.json' so OAuth2 can find it
with open('oauth2.json', 'w') as f:
    json.dump(creds, f)
