import json

f = open('./data/users.json')
arr = json.load(f)
f.close()

f = open("./data/data.json", "w")
# json.dump(sorted(arr, key=lambda x: x.get("username")), f, indent=2)
json.dump(sorted(arr, key=lambda x: x["username"]), f, indent=2)
f.close()
