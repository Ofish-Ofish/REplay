from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json
import urllib.request
import re
import pprint as pprint
from YoutubeApi import YoutubeSearch
from functools import cache, lru_cache
from multiprocessing import Process
from pytube import YouTube 

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


@lru_cache(maxsize=5)
def getAuthHeader(token):
  return {"Authorization": "Bearer " + token}

@lru_cache(maxsize=5)
def searchForArtist(token, artistName):
  url = "https://api.spotify.com/v1/search"
  headers = getAuthHeader(token)
  query = f"?q={artistName}&type=artist&limit=1"
  
  queryUrl = url + query
  result = get(queryUrl, headers=headers)
  jsonResult = json.loads(result.content)
  print(jsonResult["artists"]["items"])

@lru_cache(maxsize=5)
def getPlaylist(token, playListID): 
  url = f"https://api.spotify.com/v1/playlists/{playListID}"
  headers = getAuthHeader(token)
  result = get(url, headers=headers)
  jsonResult = json.loads(result.content)
  json.dump((jsonResult), open('spotifyPlayList.json', 'w'), indent=2)
  return jsonResult

def getPlayListID():
  playList = input("please click share on you spotify playlist and paste the url here: ")
  playListID = playList.split("/")[-1]
  playListID = playListID.split("?")[0]
  return playListID

if __name__ == '__main__':
  token = getToken()

  playlistRaw = getPlaylist(token,"57edcOl1dxSb7x3a0xuYe4")

  f = open("songPlayList.txt", "w", encoding='utf-8')
  for i in playlistRaw["tracks"]["items"]:
    songName = i["track"]["name"]
    f.write(songName)
    f.write("\n")
  f.close()

  youtubeSearch = YoutubeSearch("Piano Sonata No. 2 in B-Flat Minor, Op. 36: II. Non allegro. Lento",1)
  json.dump((youtubeSearch["items"][0]["id"]["videoId"]), open('youtube.json', 'w'), indent=2)

  yt = YouTube("https://www.youtube.com/watch?v="+youtubeSearch["items"][0]["id"]["videoId"]) 
  
  # extract only audio 
  video = yt.streams.filter(only_audio=True).first() 
    
  # check for destination to save file 
  print("Enter the destination (leave blank for current directory)") 
  destination = str(input(">> ")) or '.'
    
  # download the file 
  out_file = video.download(output_path=destination) 
    
  # save the file 
  base, ext = os.path.splitext(out_file) 
  new_file = base + '.mp3'
  os.rename(out_file, new_file) 
    
  # result of success 
  print(yt.title + " has been successfully downloaded.")
