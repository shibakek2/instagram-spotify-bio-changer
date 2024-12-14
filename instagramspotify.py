import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
import requests
from datetime import datetime
import random

# SPOTIFY
CLIENT_ID = ''
CLIENT_SECRET = ''
REDIRECT_URI = 'http://localhost:8888/callback'


# INSTAGRAM

# AUTH
# Grab this from any request sent on instagram, best way to grab both the cookie is by changing you'r bio and catching the request
XCsrftoken = "" 
COOKIE = ""

# BIO

# All info here needs to be filled out, Again change your bio and search for this request https://www.instagram.com/api/v1/web/accounts/edit/, Below is the payload
current_times = datetime.now().strftime("%I:%M %p")
base_bio = "Solo Developer, Python,js,HTML,CSS. "
secont_bio = f"I make random things for fun :) Last updated at {current_times}"
email = "" # Your email
first_name = "Wilhem Norman" # Your Name
username = "cometdev420" # your username, you can change this to change your display name aswell
phone_number = None # keep as none unless you have a phone number
external_url = "https://discord.com/invite/3hT8GkQBzg" # This does not matter as much as you cant change links on desktop only on mobile

#Null
#"X-Asbd-Id": XAsbdId,
#"X-Ig-App-Id": XIgAppId,
#"X-Ig-Www-Claim": HMAC,
#"X-Instagram-Ajax": XInstagramAjax,
#XIgAppId = ""
#XInstagramAjax = ""
#XAsbdId = ""
#HMAC = "hmac."

def get_current_song():
    sp_oauth = SpotifyOAuth(client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            scope="user-read-playback-state user-read-currently-playing")
    current_times = datetime.now().strftime("%I:%M %p")
    sp = spotipy.Spotify(auth_manager=sp_oauth)
    current_track = sp.currently_playing()

    if current_track and current_track['is_playing']:
        track = current_track['item']
        artist = track['artists'][0]['name']
        song = track['name']
        current_time_ms = current_track['progress_ms']
        song_length_ms = track['duration_ms']
        current_time = time.strftime('%M:%S', time.gmtime(current_time_ms / 1000))
        song_length = time.strftime('%M:%S', time.gmtime(song_length_ms / 1000))
        progress_ratio = current_time_ms / song_length_ms
        slider_length = 10
        filled_slider_length = int(slider_length * progress_ratio)
        slider = "─" * filled_slider_length + "〇" + "─" * (slider_length - filled_slider_length - 1)
        song_output = f"🎵 {song} | {artist}\n"
        song_output += f"{current_time} ─{slider}─ {song_length}\n"
        song_output += f"⇄ ◃◃ ⅠⅠ ▹▹ ↻\n"
        song_output += f"On Spotify\nLast updated at {current_times}"
        return song_output, song, f"."
    else:
        return base_bio, None, secont_bio

def update_bio(current_song, song_url):
    url = "https://www.instagram.com/api/v1/web/accounts/edit/"
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-CA,en;q=0.9",
        "Content-Length": "193",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": COOKIE,
        "Origin": "https://www.instagram.com",
        "Referer": "https://www.instagram.com/accounts/edit/",
        "Sec-Ch-Prefers-Color-Scheme": "dark",
        "Sec-Ch-Ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        "Sec-Ch-Ua-Full-Version-List": "\"Google Chrome\";v=\"131.0.6778.86\", \"Chromium\";v=\"131.0.6778.86\", \"Not_A Brand\";v=\"24.0.0.0\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Model": "\"\"",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Ch-Ua-Platform-Version": "\"10.0.0\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "X-Csrftoken": XCsrftoken,
        "X-Requested-With": "XMLHttpRequest"
    }

    payload = {
        "biography": f"{current_song} {song_url}",
        "chaining_enabled": "on",
        "email": email,
        "external_url": external_url,
        "first_name": first_name ,
        "phone_number": phone_number,
        "username": username
    }
    response = requests.post(url, headers=headers, data=payload)
    if response.json().get("status") == "ok":
        pass
    else:
        print(f"Error updating bio: Check your account details")

def main():
    last_song = "1"
    while True:
        try:
            current_song, song, song_url = get_current_song()
            if current_song:
                if last_song != song:
                    update_bio(current_song, song_url)
                    print(f"Updated Instagram bio: {current_song}")
                    last_song = song
                else:
                    print("Song has not changed, bio not updated.")
            else:
                print("No song is currently playing.")
            sleep_time = random.randint(300, 600)
            time.sleep(sleep_time) 
        except requests.exceptions.RequestException: 
            print("There was an error")

if __name__ == "__main__":
    main()
