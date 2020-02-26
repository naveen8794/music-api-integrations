import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from Configs.SpotifyConfig import CLIENT_ID, CLIENT_SECRET, USER

# Authorization Code flow required for redirecting app

# token = util.prompt_for_user_token(USER,client_id=CLIENT_ID, client_secret=CLIENT_SECRET,scope='user-library-read',redirect_uri= REDIRECT_URI)
#
# if token:
#     sp = spotipy.Spotify(auth=token)
#     results = sp.current_user_saved_tracks()
#     for item in results['items']:
#         track = item['track']
#         print(track['name'] + ' - ' + track['artists'][0]['name'])
# else:
#     print("Can't get token for", USER)


#### client credentials flow which doesnt require redirect URI

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlists = sp.user_playlists(USER)
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'], playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None
