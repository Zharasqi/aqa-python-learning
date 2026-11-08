# import json
# book = {
#     "title": "Python Basics",
#     "author": "Dias",
#     "year": 2026,
#     "tags": ["python", "json", "practice"],
#     "available": True
# }
# json_str = json.dumps(book, indent=2)
# print(json_str)
#
#
# book.update({
#     "rating": 4.8
# })
# print(json.dumps(book, indent=2))

import json

user = {
    "name": "Dias",
    "age": 19
}

with open("users.json", "w") as file:
    json.dump(user, file, indent=2)

with open("users.json", "r") as file:
    data = json.load(file)

print(data["name"])