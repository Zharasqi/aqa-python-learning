import json

def load_json(filename):
    try:
        with open(filename, encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        return []
# users = load_json("broken.json")
# print(users)
data = []
def save_json(filename, data):
    try:
        with open(filename, "w", encoding = "utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii = False)
            return "Файл успешно сохранён"
    except Exception as e:
        return "Ошибка при сохранении файла"


print(save_json("broken.json", data))