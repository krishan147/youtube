import argparse
import json
from googleapiclient.discovery import build

with open('apikey.txt', 'r') as apikey:
    apikey = apikey.read()

DEVELOPER_KEY = apikey
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


def youtube_search(query='olay', max_results=25):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q=query,
        part='id,snippet',
        maxResults=max_results
    ).execute()

    print (search_response)

d = youtube_search()