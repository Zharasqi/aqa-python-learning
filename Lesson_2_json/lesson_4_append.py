import json

with open('users.json', 'r') as json_file:
    user = json.load(json_file)

data = {
    "id": 3,
    "name": "Dana",
    "age": 24,
    "skills": ["SQL"]
    }

user.append(data)
with open('users.json', 'w', encoding="utf-8") as outfile:
    json.dump(user, outfile, indent=4, ensure_ascii=False)

print(user)