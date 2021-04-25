import urllib.request
import json
import urllib
import requests
import sys

def is_rick_rol():
    if "rick" in result or "Rick" in result or "Never Gonna" in result:
        print("Probably a rick roll")
    else:
        print("Probably not a rick roll")

input_url = input("enter sus url: ")
if 'thisworldthesedays'in input_url:
    print('probobly a rick roll')
    sys.exit()
elif 'youtube' not in input_url:
    input_url = requests.head(input_url).headers['location']


params = {"format": "json", "url": input_url}
url = "https://www.youtube.com/oembed"
query_string = urllib.parse.urlencode(params)
url = url + "?" + query_string

with urllib.request.urlopen(url) as response:
    response_text = response.read()
    data = json.loads(response_text.decode())
    result = data['title']
    is_rick_rol()
    print("Titel: ", result)
    print("Channel: ", data["author_url"])

input("Press a key to exit...")
