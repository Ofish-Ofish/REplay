from dotenv import load_dotenv
import os
import numpy
import base64
from requests import post, get
import json
import urllib.request
import re
import pprint as pprint
from YoutubeApi import YoutubeSearch, songSave, playListSongSave
from functools import cache, lru_cache
from multiprocessing import Process
import csv
import pandas as pd  


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
  # json.dump((jsonResult["tracks"]["items"][0]["track"]["id"]), open('spotigfy.json', 'w'), indent=2)
  return jsonResult

def getSongInfo(playlist, token, id): 
  url = f"https://api.spotify.com/v1/audio-features/{id}"
  headers = getAuthHeader(token)
  result = get(url, headers=headers)
  jsonResult = json.loads(result.content)
  # json.dump(jsonResult, open(f'songInfo{playlist}.json', 'a'), indent=2)
  return jsonResult

def getPlayListID():
  playList = input("please click share on you spotify playlist and paste the url here: ")
  playListID = playList.split("/")[-1]
  playListID = playListID.split("?")[0]
  return playListID

def similarity(playlist,s1,s2):
  os.chdir("./playList/")
  playlistSongs = []
  with open(f'{playlist}.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='~', quotechar='|')
    for row in spamreader:
      playlistSongs.append([row[7], row[12], row[13]])
    pprint.pprint(playlistSongs)
  # numpy.cross()


def downloadPlayList(): 
  os.system("clear")
  playlist = input("please add the name of your playlist: ")
  playlist = playlist.replace(" ", "_")
  path = "./playList/"
  isExsist = os.path.exists(path)
  if not isExsist:
    os.chdir(".")
    os.makedirs("playList")
  os.chdir("./playList/")
  os.makedirs(playlist)
  os.chdir(playlist)
  playlistRaw = getPlaylist(token, getPlayListID())
  for i in playlistRaw["tracks"]["items"]:
    songName = i["track"]["name"].replace("[", "").replace("]", "").replace("~", "")
    youtubeSearch = YoutubeSearch(songName,1)
    songID = youtubeSearch["items"][0]["id"]["videoId"]
    playListSongSave(songID, playlist)


def csvSave(playlist):
  os.system("clear")
  os.chdir("./playList/")
  playlistRaw = getPlaylist(token, getPlayListID())
  with open(f"{playlist}.csv",'w',newline='',encoding='utf-8') as f:
    writer = csv.writer(f, delimiter='~')
    writer.writerow(['songName','songid','Albumid','danceability','energy','key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo','type','id','uri','track_href','analysis_url','duration_ms','time_signature','vector'])
  for i in playlistRaw["tracks"]["items"]:
    songName = i["track"]["name"].replace("[", "").replace("]", "").replace("~", "")
    songid = i["track"]["id"]
    Albumid = i["track"]["album"]["id"]
    data = (getSongInfo(playlist,token, i["track"]["id"]))
    data = list(data.values())
    data = [songName] + [songid] + [Albumid] + data
    with open(f"{playlist}.csv",'a',newline='', encoding='utf-8') as f:
      writer = csv.writer(f, delimiter='~')
      writer.writerow(data)

if __name__ == '__main__':
  os.system("clear")
  os.chdir(".")
  token = getToken()
  # csvSave("w")
  similarity("w","w","w")