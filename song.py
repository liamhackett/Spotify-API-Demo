import json
import requests
from tokens import spotify_user_id
from refresh import Refresh
import urllib.request

class Song:
    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_token=""
        self.spotify_link = "https://api.spotify.com/v1/me/player/currently-playing"
        self.track_info = ""

    def __str__(self):
        return f"{self.track_info['name']} \nBy {self.track_info['artists']}\n"
    
    def download_image(self, link):
        if(self.track_info["is_playing"]):
            urllib.request.urlretrieve(link, "image.jpg")
        else:
           urllib.request.urlretrieve("https://i.scdn.co/image/ab6775700000ee852d2d6d902367a475428d683d", "image.jpeg")

    def call_refresh(self):
        refreshCaller = Refresh()
        self.spotify_token = refreshCaller.refresh()

    def get_track(self):
        try:
            head = {"Authorization": f"Bearer {self.spotify_token}"}
            response = requests.get(self.spotify_link, headers=head)

        
            response_json = response.json()
        
            track_id = response_json['item']['id']
            track_name = response_json['item']['name']

            artists = [artist for artist in response_json['item']['artists']]
            artist_names = ', '.join([artist['name'] for artist in artists])

            image = response_json['item']['album']['images'][2]['url']
            link = response_json['item']['external_urls']['spotify']

            is_playing = response_json["is_playing"]
           
            self.track_info = {
                "id": track_id,
                "name": track_name,
                "artists": artist_names,
                "link": link,
                "image": image,
                "is_playing": is_playing
            }

            return self.track_info

        except json.JSONDecodeError:
            return 0

