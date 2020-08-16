import json

from datetime import datetime

with open('db.json') as f:
    data = json.load(f)

for obj in data:
    if obj["model"] == "apiserver.ranking":
        time = obj["fields"]["time"]
        try:
            inttime = int(time)
            realtime = datetime.utcfromtimestamp(inttime).strftime('%Y-%m-%d %H:%M:%S')
            obj["fields"]["time"] = realtime
        except:
            pass

with open('out.json', mode="wt") as writer:
    json.dump(data, writer)

