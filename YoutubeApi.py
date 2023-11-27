from dotenv import load_dotenv
import os
import pprint as pprint
from functools import cache, lru_cache
from pytube import YouTube
import urllib.request
import re
from bs4 import BeautifulSoup
import json

load_dotenv()

def YoutubeSearch(searchKeyword):
  results = []
  searchKeyword = urllib.parse.quote(searchKeyword)
  html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + searchKeyword)
  html = html.read().decode('utf-8')
  soup = BeautifulSoup(html, 'html.parser')
  scripts = soup.find_all('script')
  for script in scripts:
    if re.findall(r"watch\?v=([^&=]+)", str(script)):
      vidsData = script.string.split("ytInitialData = ")[1].replace(";", "").replace("</script>", "")
      vidsData = json.loads(vidsData)
      for i in range(10):
        try:
          results.append("https://www.youtube.com/watch?v="+vidsData["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"]["sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"][i]["videoRenderer"]["videoId"])
        except:
          continue
      return results

@lru_cache(maxsize=5)

# def songSave(SongName,songID, playlist):
#   # json.dump((response["items"][0]["id"]["videoId"]), open('youtube.json', 'w'), indent=2)
#   yt = YouTube("https://www.youtube.com/watch?v="+songID) 
#   video = yt.streams.filter(only_audio=True).first() 
#   destination = './song'
#   out_file = video.download(output_path=destination) 
#   base, ext = os.path.splitext(out_file) 
#   new_file = SongName + '.mp3'
#   os.rename(out_file, new_file) 
#   print(yt.title + " has been successfully downloaded.")

# should be removed
@lru_cache(maxsize=5)
def SongSave(songUrl, path, SongName):
  yt = YouTube(songUrl) 
  video = yt.streams.filter(only_audio=True).first() 
  destination = path
  out_file = video.download(output_path=destination) 
  base, ext = os.path.splitext(out_file) 
  new_file = SongName + '.mp3'
  os.rename(out_file, new_file) 
  print(yt.title + " has been successfully downloaded.")

