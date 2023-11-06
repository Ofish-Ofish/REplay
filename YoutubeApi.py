from dotenv import load_dotenv
import os
import googleapiclient.discovery
import pprint as pprint
from functools import cache, lru_cache
from pytube import YouTube 

load_dotenv()

@lru_cache(maxsize=5)
def YoutubeSearch(query,maxResults):
  api_service_name = "youtube"
  api_version = "v3"
  DEVELOPER_KEY = os.getenv("GOOGLE_API_KEY")

  youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey = DEVELOPER_KEY
  )

  request = youtube.search().list(
    part='snippet',
    q = query,
    maxResults=maxResults,
    order="relevance",
    type="video"
  )

  response = request.execute()
  return response


@lru_cache(maxsize=5)
def songSave(respSongNameonse, songID):
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

