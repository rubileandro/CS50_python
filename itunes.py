import json
import requests 
import sys

# Error checking
if len(sys.argv) != 2:
    sys.exit()

# Request
response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])
# print(json.dumps(response.json(), indent=2))

# Grabbing servers response
o = response.json()
for result in o["results"]:
    print(result["trackName"])