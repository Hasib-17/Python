import requests,sys
import json
if len(sys.argv)!=2:
    sys.exit()

respose=requests.get("https://itunes.apple.com/search?entity=song&limit=10&term="+sys.argv[1])

# print(json.dumps(respose.json(),indent=2))
obj=respose.json()
for result in obj["results"]:
    print(result["trackName"])
