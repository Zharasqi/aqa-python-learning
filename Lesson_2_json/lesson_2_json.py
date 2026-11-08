import json

orders_json = '''
[
  {
    "id": 1,
    "customer": {
      "name": "Dias",
      "city": "Almaty"
    },
    "items": [
      {"title": "Book", "price": 5000, "quantity": 2},
      {"title": "Pen", "price": 300, "quantity": 5}
    ]
  },
  {
    "id": 2,
    "customer": {
      "name": "Aruzhan",
      "city": "Astana"
    },
    "items": [
      {"title": "Laptop", "price": 350000, "quantity": 1},
      {"title": "Mouse", "price": 8000, "quantity": 2}
    ]
  },
  {
    "id": 3,
    "customer": {
      "name": "Miras",
      "city": "Shymkent"
    },
    "items": [
      {"title": "Backpack", "price": 12000, "quantity": 1},
      {"title": "Notebook", "price": 1000, "quantity": 4}
    ]
  }
]
'''

json_text = json.loads(orders_json)

for i in range(len(json_text)):
    total = 0
    for j in json_text[i]["items"]:
        # if key == "items":
        #     for item in value:
        total += j["price"] * j["quantity"]

    print(f"Order #{json_text[i]["id"]} - {json_text[i]["customer"]["name"]}: {total}")


