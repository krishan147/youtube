import argparse
import json
from googleapiclient.discovery import build
import requests

with open('apikey.txt', 'r') as apikey:
    apikey = apikey.read()


videoid = 'OU6CuSMzNus'
DEVELOPER_KEY = apikey
url = 'https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id='+videoid+'&key=' + DEVELOPER_KEY
request = requests.get(url)

print(request.text)
