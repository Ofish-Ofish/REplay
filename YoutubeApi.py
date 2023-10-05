from dotenv import load_dotenv
import os
import googleapiclient.discovery
import pprint as pprint

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
    order="viewCount",
    type="video"
  )

  response = request.execute()
  pprint.pprint(response)