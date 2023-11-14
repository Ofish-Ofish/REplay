from dotenv import load_dotenv
import os
import googleapiclient.discovery
import pprint as pprint
from functools import cache, lru_cache
from pytube import YouTube
from pytube import Search
import urllib.request
import re


load_dotenv()

def YoutubeSearch():
  search_keyword="Boulanger:+Vielle+priere+bouddhique+(Priere+quotidienne+pour+tout+lUnivers)+For+Tenor+Chorus"
  html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
  # pprint.pprint(html.read().decode())
  video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
  print("https://www.youtube.com/watch?v=" + video_ids[0])

@lru_cache(maxsize=5)
def songSave(SongName,songID, playlist):
  # json.dump((response["items"][0]["id"]["videoId"]), open('youtube.json', 'w'), indent=2)
  yt = YouTube("https://www.youtube.com/watch?v="+songID) 
  video = yt.streams.filter(only_audio=True).first() 
  destination = './song'
  out_file = video.download(output_path=destination) 
  base, ext = os.path.splitext(out_file) 
  new_file = SongName + '.mp3'
  os.rename(out_file, new_file) 
  print(yt.title + " has been successfully downloaded.")

# should be removed
@lru_cache(maxsize=5)
def playListSongSave(SongName,songID, playlist):
  yt = YouTube("https://www.youtube.com/watch?v="+songID) 
  video = yt.streams.filter(only_audio=True).first() 
  destination = '.'
  out_file = video.download(output_path=destination) 
  base, ext = os.path.splitext(out_file) 
  new_file = SongName + '.mp3'
  os.rename(out_file, new_file) 
  print(yt.title + " has been successfully downloaded.")

