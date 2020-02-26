import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from Configs.SpotifyConfig import CLIENT_ID, CLIENT_SECRET, USER


def get_playlists():
    """client credentials flow which doesnt require redirect URI"""


client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlists = sp.user_playlists(USER)
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("Playlist-%d : URI - %s ,Playlist_Name - %s." % (
            i + 1 + playlists['offset'], playlist['uri'], playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None

