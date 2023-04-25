import json

data = {"User":1, "User2":2}

with open("json_data.json", "w") as json_file:
    json.dump(data, json_file)

with open('json_data.json') as json_file:
    data = json.load(json_file)
    print(data)