# Задача 1,2
# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def is_adult(self):
#         if self.age >= 18:
#             return True
#         else:
#             return False
#     def show_info(self):
#         return f"Имя: {self.name}, Возраст: {self.age}"
# user = User("Zharas", 25)
# print(user.show_info())
# print(user.is_adult())
#Задача 3
# class ApiResponse:
#     def __init__(self, status_code, data):
#         self.status_code = status_code
#         self.data = data
#     def is_success(self):
#         if 300 > self.status_code >= 200:
#             return True
#         else:
#             return False
# api1 = ApiResponse(200, "Успешный код ответа")
# api2 = ApiResponse(404, "Not Found")
# print(api1.is_success())
# print(api2.is_success())

# Задача 4
# import json
# class TestDataLoader:
#     def __init__(self, filename):
#         self.filename = filename
#     def load_data(self):
#         with open(self.filename, encoding="utf-8") as f:
#             return json.load(f)
# read_json = TestDataLoader("test_data.json")
# print(read_json.load_data())
# Задача 5
# class BasePage:
#     def __init__(self, base_url):
#         self.base_url = base_url
#     def get_url(self):
#         return self.base_url
# class LoginPage(BasePage):
#     def __init__(self, base_url):
#         super().__init__(base_url)
#     def login(self,username, password):
#         return f"{username} вошел в систему"
# login_page = LoginPage("https://www.goedele.com")
# print(login_page.get_url())
# print(login_page.login("Zharas", "qwerty123"))
# Задача 6
class User:
    def __init__(self, name, age):
        if age < 0:
            raise ValueError("Возраст некорректный, не может быть меньше 0")
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} ({self.age})"
try:
    data = User("Zharas", -5)
    print(data)
except ValueError as error:
    print(error)
user = User("Zharas", 24)
print(user)




