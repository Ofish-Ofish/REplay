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
def SongSave(songUrl, path, SongName):
  try:
    YouTube(songUrl).streams.get_audio_only("mp4").download(filename= SongName + ".mp3")
    print("The video is downloaded in MP3")
  except KeyError:
    print("Unable to fetch video information. Please check the video URL or your network connection.")
