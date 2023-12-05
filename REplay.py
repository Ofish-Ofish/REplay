from dotenv import load_dotenv
import os
import numpy as np
import base64
from requests import post, get
import json
import pprint as pprint
from YoutubeSearch import YoutubeSearch, SongSave
from functools import cache, lru_cache
from multiprocessing import Process
import csv
import random
import time

PLAYLISTNAME = "classical"
ERROR_LIMIT = 20

load_dotenv()

clientId = os.getenv("CLIENT_ID")
clientSecret = os.getenv("CLIENT_SECRET")

def getToken():
  authString = clientId + ":" + clientSecret
  authByte = authString.encode("utf-8")
  authBase64 = str(base64.b64encode(authByte), "utf-8")
  URL = "https://accounts.spotify.com/api/token"
  headers = {
    "Authorization": "Basic " + authBase64,
    "Content-Type": "application/x-www-form-urlencoded"
  }
  data = {"grant_type": "client_credentials"}
  result = post(URL, headers=headers, data=data)
  jsonResult = json.loads(result.content)
  token = jsonResult["access_token"]
  return token

@lru_cache(maxsize=5)
def getAuthHeader(token):
  return {"Authorization": "Bearer " + token}

@lru_cache(maxsize=5)
def searchForArtist(token, artistName):
  URL = "https://api.spotify.com/v1/search"
  headers = getAuthHeader(token)
  query = f"?q={artistName}&type=artist&limit=1"
  
  queryUrl = URL + query
  result = get(queryUrl, headers=headers)
  jsonResult = json.loads(result.content)
  print(jsonResult["artists"]["items"])

@lru_cache(maxsize=5)
def getPlaylist(token, playListID): 
  URL = f"https://api.spotify.com/v1/playlists/{playListID}"
  headers = getAuthHeader(token)
  result = get(URL, headers=headers)
  jsonResult = json.loads(result.content)
  # json.dump((jsonResult["tracks"]["items"][0]["track"]["id"]), open('spotigfy.json', 'w'), indent=2)
  return jsonResult

def getSongInfo(playlist, token, id): 
  URL = f"https://api.spotify.com/v1/audio-features/{id}"
  headers = getAuthHeader(token)
  result = get(URL, headers=headers)
  jsonResult = json.loads(result.content)
  # json.dump(jsonResult, open(f'songInfo{playlist}.json', 'a'), indent=2)
  return jsonResult

def getPlayListID():
  playList = input("please click share on you spotify playlist and paste the url here: ")
  playListID = playList.split("/")[-1]
  playListID = playListID.split("?")[0]
  return playListID

def vectorNormalizer(threeitmeList):
  if len(threeitmeList) != 3:
    raise f"length error... list length is {len(threeitmeList)}, not 3"
  v = np.vectorize(float)(threeitmeList)
  normalized_v = v / np.sqrt(np.sum(v**2))
  return normalized_v
  
def similarity(cs,s):
  v = np.cross(cs, s)
  return np.sqrt(np.sum(v**2)) * 1000

def downloadPlayList(playList, errorLimit): 
  path = f"./playList/{playList}"
  os.chdir(path)
  with open(f"{playList}.csv", newline='', encoding='utf-8') as csvfile:
    reader  = csv.DictReader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
      songName = row["songName"]
      songUrl = YoutubeSearch(songName.strip().replace(" ", "+"))
      for i in range(errorLimit):
        if len(songUrl) < 1:
          songUrl = YoutubeSearch(songName.strip().replace(" ", "+")) 
          print(i)
        else: break
      SongSave(songUrl[0], path, songName,)

def downloadSong(errorLimit): 
  path = f"./song"
  os.chdir(path)
  songName = input("please enter a song name: ").replace("[", "").replace("]", "").replace(",", "").replace("'", "").replace('"', "").replace('&#39;', "").replace("&amp;","").replace("&quot;","").replace('.', "").replace(':', "").replace('/', "").replace('\\', "").replace('|', "")
  songUrl = YoutubeSearch(songName.strip().replace(" ", "+"))
  for i in range(errorLimit):
    if len(songUrl) < 1:
      songUrl = YoutubeSearch(songName.strip().replace(" ", "+"))
      print(i)
    else: break
  SongSave(songUrl[0], path, songName)

def createPlayList():
  os.system("clear")
  playlist = input("please add the name of your playlist: ")
  playlist = playlist.replace(" ", "_")
  path = "./playList/"
  os.chdir(".")
  isExsist = os.path.exists(path)
  if not isExsist:
    os.makedirs("playList")
  os.chdir(path)
  os.makedirs(playlist)
  os.chdir(playlist)
  return playlist

def formatData(item, playlist, token):
  songName = item["track"]["name"].replace("[", "").replace("]", "").replace(",", "").replace("'", "").replace('"', "").replace('&#39;', "").replace("&amp;","").replace("&quot;","").replace('.', "").replace(':', "").replace('/', "").replace('\\', "").replace('|', "")
  songid = item["track"]["id"]
  Albumid = item["track"]["album"]["id"]
  data = getSongInfo(playlist, token, item["track"]["id"])
  data = list(data.values())
  data = [songName] + [songid] + [Albumid] + data
  data.append(vectorNormalizer([data[4], data[12], data[13]]))
  return data

def csvSave(playlist, token):
  os.system("clear")
  os.chdir(f".")
  playlistRaw = getPlaylist(token, getPlayListID())
  with open(f"{playlist}.csv",'w',newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['songName','songid','Albumid','danceability','energy','key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo','type','id','uri','track_href','analysis_url','duration_ms','time_signature','vector'])
    for i in playlistRaw["tracks"]["items"]:
      print("start of api",time.time(), )
      data = formatData(i, playlist, token)
      print("start of write",time.time())
      writer.writerow(data)
      print("end of write",time.time())

def stringToVec(string):
  return np.vectorize(float)([x for x in string[1:-1].split(" ") if x != ''])

def shuffle():
  os.chdir("./playList")
  # save csv as a modifable list of dics
  dictList = []
  with open(f'{PLAYLISTNAME}.csv', newline='', encoding='utf-8') as csvfile:
    dictList = [row for row in csv.DictReader(csvfile, delimiter=',', quotechar='|')]
  
  # choose random song and remove all songs witht he same albumid
  randomSongDict = random.choice(dictList)
  to_remove = [x for x in reversed(range(len(dictList)-1)) if dictList[x]['Albumid'] == randomSongDict["Albumid"]]
  for index in reversed(to_remove):
    dictList.pop(index)

  # get a list of all crosses
  crosses = np.array([])
  for i in range(len(dictList) - 1):
    dictList[i]["cross"] = similarity(stringToVec(randomSongDict['vector']), stringToVec(dictList[i]['vector']))
    crosses = np.append(crosses,dictList[i]["cross"])
  
  # return 10 songs. the first song being the random one picked at the start; the rest of the songs are the 9 most siliar songs shuffled
  crosses = np.argsort(crosses)[:9]
  shuffleSongList = [dictList[i]["songName"] for i in crosses]
  random.shuffle(shuffleSongList)
  shuffleSongList = [randomSongDict['songName']] + shuffleSongList
  return shuffleSongList

def main():
  os.system("clear")  
  os.chdir(".")
  token = getToken()
  # PLAYLISTNAME = createPlayList()
  # csvSave(PLAYLISTNAME, token)
  # downloadPlayList(PLAYLISTNAME)
  downloadSong(ERROR_LIMIT)
  # pprint.pprint(shuffle())
  # keyward = "taking whats not yours".strip().replace(" ", "+")
  # pprint.pprint(YoutubeSearch(keyward)[0])

if __name__ == '__main__':
  main()
