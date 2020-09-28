from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .video_yt_scrapper import search_yt, get_youtube_video_duration
import json

@csrf_exempt
def yt_video_search_play(request, *args, **kwargs):
    if request.method == "POST":
        print("[POST]")
        client_data = json.loads(request.body.decode('utf-8'))
        query = client_data['videoQuery']
        print(query)
        searchResult = search_yt(query)
        # print("searchResult", searchResult)
        context = {
            "videoId" : searchResult['items'][0]['id']['videoId'],
        }
        # context = json.dumps(context)
        print(context)
        return JsonResponse(context)
    else:
        return render(request, 'index.html',)
