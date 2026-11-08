import json

def load_json(filename):
    with open(filename, encoding="utf-8") as file:
        return json.load(file)

def save_json(filename, data):
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(data, file, indent = 4, ensure_ascii = False)

data = [
    {
        "id": 1,
        "name": "Zharas",
        "age": 25,
        "skills": ["Python", "HTML"]
    },
    {
        "id": 2,
        "name": "Ayan",
        "age": 22,
        "skills": ["JavaScript"]
    }
]
save_json("users.json", data)

read_json = load_json("users.json")
# read_json["is_student"] = True
# del read_json["city"]
# read_json["skills"].append("Git")
# read_json["is_student"] = False
for name in read_json:
    if name["id"] == 2:
        name["age"] = 23
        name["skills"].append("React")


save_json("users.json", read_json)
print(read_json)
