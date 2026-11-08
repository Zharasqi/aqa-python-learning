#import json
# products = [
#     {"name": "Laptop", "price": 350000, "in_stock": True},
#     {"name": "Mouse", "price": 8000, "in_stock": True},
#     {"name": "Keyboard", "price": 15000, "in_stock": False}
# ]
# with open('products.json', 'w') as outfile:
#     json.dump(products, outfile, indent=2, ensure_ascii=False)
#
# with open('products.json', "r") as json_file:
#     products = json.load(json_file)
# total = 0
# for product in products:
#     if product["in_stock"]:
#         total += product["price"]
#         print(f"{product['name']} - {product['price']}")
#
#
#     else:
#         print(f"{product['name']}: не в наличии")
#         print()
# print(f"Total: {total}")
import json
settings = [
     {"name": "Laptop", "price": 350000, "in_stock": True},
     {"name": "Mouse", "price": 8000, "in_stock": True},
     {"name": "Keyboard", "price": 15000, "in_stock": False}
]
with open("settings.json", "w") as json_file:
    json.dump(settings, json_file, indent=2, ensure_ascii=False)


try:
    with open("settings.json", "r") as f:
        settings = json.load(f)
        print("Settings loaded")
        print(settings)

except FileNotFoundError:
    print("settings.json not found")

except json.JSONDecodeError:
    print("Invalid JSON format")