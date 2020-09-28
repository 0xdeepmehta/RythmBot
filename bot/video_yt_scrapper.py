import json 
import requests 
import os
from googleapiclient.discovery import build 
import googleapiclient.errors


API_KEY = 'AIzaSyBNELGOGgf4l62O8FyMD6egN8oG5od36sc'

def get_youtube_video_duration(video_id):
    url = f"https://www.googleapis.com/youtube/v3/videos?part=contentDetails&id={video_id}&key={API_KEY}"

    response = requests.get(url) # Perform the GET request 
    data = response.json() # Read the json response and convert it to a Python dictionary 

    return data['items'][0]['contentDetails']['duration']

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def search_yt(query):

    api_service_name = "youtube"
    api_version = "v3"

    youtube = build(
                api_service_name, 
                api_version, 
                developerKey = API_KEY
            )

    request = youtube.search().list(
        part="snippet",
        maxResults=1,
        type="video",
        q=query
    )
    response = request.execute()

    return response

# if __name__ == "__main__":
#     searchResult = search_yt("love me baby")
#     videoId = searchResult['items'][0]['id']['videoId']
#     videoTitle = searchResult['items'][0]['snippet']['title']
#     searched_video_duration = get_youtube_video_duration(videoId)

#     print("Video Title : ", videoTitle)
#     print("Video Id : ", videoId)
#     print("Duration : ", searched_video_duration)
#     print(f"video link : https://www.youtube.com/watch?v={videoId}")



