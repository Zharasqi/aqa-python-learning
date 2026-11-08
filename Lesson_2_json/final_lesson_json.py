import json

def load_json(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_json(filename, data):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
            return "Файл успешно сохранён"
    except FileNotFoundError:
        return "Ошибка при сохранении файла"


data = {
    "id": 4,
    "name": "Miras",
    "age": 28,
    "skills": ["Python", "Pytest"]
}

users = load_json("users.json")
json_exists = False
for user in users:
    if user["id"] == 4:
        json_exists = True
        break
if json_exists:
    print("Данные уже есть в файле")
else:
    users.append(data)
    result = save_json("users.json", users)
    print(f"{result} - Данные успешно добавились в файл")