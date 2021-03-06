import requests
import time
import pandas as pd

with open('apikey.txt', 'r') as apikey:
    apikey = apikey.read()
    DEVELOPER_KEY = apikey

def youtubeComments(videoId):
    time.sleep(6)

    url = 'https://www.googleapis.com/youtube/v3/commentThreads?key=' + DEVELOPER_KEY + '&textFormat=plainText&part=snippet&videoId=' + videoId + '&maxResults=100'

    request = requests.get(url)
    data = request.json()
    list_frames = []
    time.sleep(10)

    for items in data['items']:
        snippet = items['snippet']
        df = pd.DataFrame.from_dict(snippet)
        list_frames.append(df)

    if 'nextPageToken' in str(data):
        while 'nextPageToken' in str(data):
            time.sleep(8)
            next_page_token =  data['nextPageToken']
            concurrent_pages = 'https://www.googleapis.com/youtube/v3/commentThreads?key=' + DEVELOPER_KEY + '&textFormat=plainText&part=snippet&videoId=' + videoId + '&maxResults=100' + '&pageToken=' + next_page_token
            request = requests.get(concurrent_pages)
            data = request.json()

            for items in data['items']:
                snippet = items['snippet']
                df = pd.DataFrame.from_dict(snippet)
                list_frames.append(df)

    return list_frames

with open ('youtube.txt', 'r') as list_video_url:
    for video_url in list_video_url.readlines():
        video_url = video_url.replace('\n', '')
        videoId = video_url.replace('https://www.youtube.com/watch?v=','')
        list_frames = youtubeComments(videoId)
        df = pd.concat(list_frames)
        print (videoId)
        df.to_csv("results/"+str(videoId)+".csv")