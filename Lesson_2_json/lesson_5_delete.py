import json
import pathlib

def load_json(filename):
    with open(filename) as file:
        return json.load(file)

def save_json(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

users = load_json('users.json')

new_users = []
for user in users:
    if user['id'] != 1:
        new_users.append(user)

save_json('users.json', new_users)
print(new_users)