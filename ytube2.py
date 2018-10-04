#! python3
__author__ = 'rls'
__version__ = 0.1
''' Program written by Robin Sharpton
    rest of DocString goes here 
'''

import json
from urllib.request import urlopen
url = "https://gdata.youtube.com/feeds/api/standardfeeds/top_rated?alt=json"
response = urlopen(url)
contents = response.read()
text = contents.decode('utf8')
data = json.loads(text)
for video in data['feed']['entry'][0:6]:
    print(video['title']['$t'])