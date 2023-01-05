# Spotify-API-Demo
This is a basic demo of the spotify API using python. It requests the currently playing song on your spotify account and prints the title and the artist to the console. There is a function to download the album cover in the Song class. This project served as a demo to use the spotify API for the current playing song. I converted this code to work with a raspberry pi LED matrix to display the album cover of the song I was playing. 
The tokens.py file could not be uploaded since it contains information specific to my account
To get the tokens for the file you will need to curl them following the instructions in the Spotify Web API docs.

The tokens.py file contains:
- spotify token for the request
- spotify username
- spotify refresh token
- spotify developer client id
- base64 encoded client_id:client_secret (in that format) for the refresh token

The tokens.py format:
spotify_token = ""
spotify_user_id = ""
refresh_token = ""
base_64 = ""


