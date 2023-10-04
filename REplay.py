from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json
import urllib.request
import re

load_dotenv()

clientId = os.getenv("CLIENT_ID")
clientSecret = os.getenv("CLIENT_SECRET")


def getToken():
  authString = clientId + ":" + clientSecret
  authByte = authString.encode("utf-8")
  authBase64 = str(base64.b64encode(authByte), "utf-8")


  url = "https://accounts.spotify.com/api/token"
  headers = {
    "Authorization": "Basic " + authBase64,
    "Content-Type": "application/x-www-form-urlencoded"
  }
  data = {"grant_type": "client_credentials"}
  result = post(url, headers=headers, data=data)
  jsonResult = json.loads(result.content)
  token = jsonResult["access_token"]
  return token

def getAuthHeader(token):
  return {"Authorization": "Bearer " + token}

def searchForArtist(token, artistName):
  url = "https://api.spotify.com/v1/search"
  headers = getAuthHeader(token)
  query = f"?q={artistName}&type=artist&limit=1"
  
  queryUrl = url + query
  result = get(queryUrl, headers=headers)
  jsonResult = json.loads(result.content)
  print(jsonResult["artists"]["items"])


def getPlaylist(token, playListID): 
  url = f"https://api.spotify.com/v1/playlists/{playListID}"
  headers = getAuthHeader(token)
  result = get(url, headers=headers)
  jsonResult = json.loads(result.content)
  return jsonResult


token = getToken()

playlistRaw = getPlaylist(token,"57edcOl1dxSb7x3a0xuYe4")
json.dump((playlistRaw), open('spotifyPlayList.json', 'w'), indent=2)

f = open("songPlayList.txt", "w", encoding='utf-8')
for i in playlistRaw["tracks"]["items"]:
  songName = i["track"]["name"]
  f.write(songName)
  f.write("\n")
f.close()


query = "Nocturne in C-Sharp Minor" 
query = query.replace(" ", "")
html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + query, )
videoIDs = re.findall(r"watch\?v=(\S{11})", html.read().decode('utf-8'))
print(videoIDs[0])
print("https://www.youtube.com/watch?v=" + videoIDs[0])