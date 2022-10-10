import json


def printJSON(data):
    parsed = json.loads(data)
    print(json.dumps(parsed, indent=4))
