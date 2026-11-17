from yahoo_oauth import OAuth2
from dotenv import load_dotenv
import yahoo_fantasy_api as yfa
import json
import os
import logging

logging.getLogger('yahoo_oauth').setLevel(logging.ERROR)
logging.getLogger('mod_yahoo_oauth').setLevel(logging.ERROR)

oauth = OAuth2(None, None, from_file='oauth2.json')
if not oauth.token_is_valid():
    oauth.refresh_access_token()

gm = yfa.Game(oauth, 'nhl')

league_id = gm.league_ids()[-1]
lg = gm.to_league(league_id)

matchups = lg.matchups()
print(matchups)

