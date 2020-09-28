from django.shortcuts import render
from .video_yt_scrapper import search_yt, get_youtube_video_duration

def yt_video_search_play(request, *args, **kwargs):
    if request.method == "POST":
        print("[POST] ")
        query = request.POST['videoName']
        print(query)
        searchResult = search_yt(query)
        # print("searchResult", searchResult)
        context = {
            "videoId" : searchResult['items'][0]['id']['videoId'],
        }
        return render(request, 'index.html',context=context)
    else:
        return render(request, 'index.html',)
