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
import pygame
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
import sys


class MyWindow(QMainWindow):
  def __init__(self):
    super(MyWindow,self).__init__()
    self.initUI()
    
  def button_clicked(self):
    self.label.setText("you pressed the button")
    pygame.mixer.init() 
    pygame.mixer.music.load(f"C:\\Users\\Ofish\\Documents\\GitHub\\REplay\\playList\\classical\\Chopin (Etude Op 25 No 9 )Butterfly.wav") 
    pygame.mixer.music.set_volume(0.7) 
    pygame.mixer.music.play() 
    self.update()
    
  def initUI(self):
    self.setGeometry(0,0,self.screen().size().width(),self.screen().size().height())
    self.setWindowTitle("REplay")
    # self.setStyleSheet("background-color: black;")
    self.label = QtWidgets.QLabel(self)
    # self.label.setStyleSheet("color: white;")
    self.label.setText("my first label!")
    self.label.move(50,50)
    
    self.b1 = QtWidgets.QPushButton(self)
    self.b1.setText("cplay music")
    self.b1.clicked.connect(self.button_clicked)

  def update(self):
    self.label.adjustSize()

  
  


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
  return np.sqrt(np.sum(v**2)) 

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
        else: SongSave(songUrl[0], path, songName); break

def downloadSong(errorLimit): 
  path = f"./song"
  os.chdir(path)
  songName = input("please enter a song name: ").replace("[", "").replace("]", "").replace(",", "").replace("'", "").replace('"', "").replace('&#39;', "").replace("&amp;","").replace("&quot;","").replace('.', "").replace(':', "").replace('/', "").replace('\\', "").replace('|', "")
  songUrl = YoutubeSearch(songName.strip().replace(" ", "+"))
  for i in range(errorLimit):
    if len(songUrl) < 1:
      songUrl = YoutubeSearch(songName.strip().replace(" ", "+"))
      print(i)
    else: SongSave(songUrl[0], path, songName); break

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

def PlaylistSaveSpotify(token):
  os.system("clear")
  os.chdir(f".")
  playlistRaw = getPlaylist(token, getPlayListID())
  playlist = playlistRaw["name"]
  playlist = playlist.replace(" ", "_")
  path = "./playList/"

  isExsist = os.path.exists(path)
  if not isExsist:
    os.makedirs("playList")
  os.chdir(path)
  os.makedirs(playlist)
  os.chdir(playlist)

  img_data = get(playlistRaw["images"][0]["url"]).content
  with open(f'{playlist}.jpg', 'wb') as handler:
      handler.write(img_data)

  with open(f"{playlist}.csv",'w',newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['songName','songid','Albumid','danceability','energy','key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo','type','id','uri','track_href','analysis_url','duration_ms','time_signature','vector'])
    for i in playlistRaw["tracks"]["items"]:
      print("start of api",time.time(), )
      data = formatData(i, playlist, token)
      print("start of write",time.time())
      writer.writerow(data)
      print("end of write",time.time())

    txtfile = open(f'{playlist}.txt', 'w')
    txtfile.write(f"{playlist}\n")
    txtfile.write(f"{playlistRaw['owner']['display_name']}\n")
    txtfile.write(f"{str(len(playlistRaw['tracks']['items']))}\n")
    txtfile.close()

    

def stringToVec(string):
  return np.vectorize(float)([x for x in string[1:-1].split(" ") if x != ''])

def shuffle(randomSongs):
  os.chdir(f"./playList/{PLAYLISTNAME}")
  with open(f'{PLAYLISTNAME}.csv', newline='', encoding='utf-8') as csvfile:
    dictList = [row for row in csv.DictReader(csvfile, delimiter=',', quotechar='|')]
    randomSongDict = random.choice(dictList)
    while randomSongDict in randomSongs[-10:]:
      randomSongDict = random.choice(dictList)

  for i in range(len(dictList)):
    dictList[i]["cross"] = similarity(stringToVec(randomSongDict['vector']), stringToVec(dictList[i]['vector']))

  dictList = sorted(dictList, key=lambda d: d['cross'])
  uniquealb = []
  uniquealbSongs = []
  for i in range(1, len(dictList)):
    if dictList[i]["Albumid"] not in uniquealb:
      uniquealb += [dictList[i]["Albumid"]]
      uniquealbSongs.append(dictList[i])

  shuffleSongList = [randomSongDict['songName']] + [uniquealbSongs[i]["songName"] for i in range(9)]
  return shuffleSongList, randomSongDict

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec())

def main():
  os.system("clear")  
  os.chdir(".")
  token = getToken()
  # PLAYLISTNAME = createPlayList()
  PlaylistSaveSpotify(token)
  # downloadPlayList(PLAYLISTNAME, ERROR_LIMIT)
  # randomsongs = []
  # shuffledSongList, randomSong = shuffle(randomsongs)
  # randomsongs.append(randomSong)
  # print(shuffledSongList[0])
  # pygame.mixer.init() 
  # pygame.mixer.music.load(f"C:\\Users\\Ofish\\Documents\\GitHub\\REplay\\playList\\classical\\Chopin (Etude Op 25 No 9 )Butterfly.wav") 
  # pygame.mixer.music.set_volume(0.7) 
  # pygame.mixer.music.play() 
  # while pygame.mixer.music.get_busy() == True:
  #   continue
  # downloadSong(ERROR_LIMIT)

  # window()



if __name__ == '__main__':
  main()
