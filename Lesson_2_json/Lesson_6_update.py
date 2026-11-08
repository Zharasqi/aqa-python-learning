import json

def load_json(filename):
    with open(filename) as file:
        return json.load(file)

def save_json(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

data = {
    "id": 2,
    "name": "Ayan",
    "age": 23,
    "skills": ["JavaScript", "React"]
}
users = load_json('users.json')
user_exists = False
for user in users:
    if user["id"] == 2:
        user_exists = True
        break

if user_exists:
    print("Пользователь уже существует")
else:
    users.append(data)
    save_json('users.json', users)
    print(users)