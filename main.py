from song import Song

def main():
    s = Song()
    last_track = ""
    while True:
        s.call_refresh()
        track_info = s.get_track()
        try:
            if track_info["name"] != last_track and track_info["is_playing"]:
                last_track = track_info["name"]   
                print(s)

            elif track_info["is_playing"] == False:
                if(last_track != "NULL"):
                    print("No Song Playing\n")
                    last_track = "NULL"
                    
        except TypeError:
            if(last_track != "NULL"):
                print("No Song Playing\n")
                last_track = "NULL"

main()