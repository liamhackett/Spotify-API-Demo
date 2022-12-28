# Spotify-API-Demo
This is a basic demo of the spotify API using python. It requests the currently playing song on your spotify account and prints the title and the artist to the console. There is a function to download the album cover in the Song class. This project served as a demo to use the spotify API for the current playing song. I converted this code to work with a raspberry pi LED matrix to display the album cover of the song I was playing. 
The tokens.py file could not be uploaded since it contains information specific to my account

The tokens.py file contains:
- spotify token for the request
- spotify username
- spotify refresh token
- spotify developer client id
- base64 encoded url for the refresh token

The tokens.py format:
spotify_token = ""
spotify_user_id = ""
refresh_token = ""
base_64 = ""


