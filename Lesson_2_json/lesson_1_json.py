import json

students_json = '''
[
  {
    "name": "Dias",
    "age": 19,
    "city": "Almaty",
    "scores": [80, 90, 75]
  },
  {
    "name": "Aruzhan",
    "age": 22,
    "city": "Astana",
    "scores": [95, 88, 92]
  },
  {
    "name": "Miras",
    "age": 18,
    "city": "Shymkent",
    "scores": [60, 70, 65]
  }
]
'''

json_text = json.loads(students_json)
# for _ in range(len(json_text)):
#     for key, value in json_text[_].items():
#         if key == "scores":
#             json_text[_]["scores"]= sum(json_text[_]["scores"]) / len(json_text[_]["scores"])
#             #print(json_text[_]["scores"])
#             scores = json_text[_]["scores"]
#             print(f"{json_text[_]['name']}: {scores:.2f}")

for student in json_text:
    scores = student["scores"]
    average = sum(scores) / len(scores)
    print(f"{student['name']}: {average:.2f}")