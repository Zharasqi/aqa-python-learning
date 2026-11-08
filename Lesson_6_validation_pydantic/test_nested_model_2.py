# from pydantic import BaseModel, ValidationError
#
# class Address(BaseModel):
#     city: str
#     street: str
#     zip_code: str
#
# class User(BaseModel):
#     id: int
#     name: str
#     address: Address
#
# bad_data = {
#     "id": 1,
#     "name": "Dana",
#     "address": {"city": "Almaty", "zip_code": "050000"}
# }
# try:
#     User.model_validate(bad_data)
# except ValidationError as e:
#     first_error = e.errors()[0]
#     print(first_error["loc"])
#     print(first_error["type"])
#     print(first_error["msg"])