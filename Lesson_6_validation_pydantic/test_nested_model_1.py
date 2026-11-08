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
# data = {
#     "id": 1,
#     "name": "Dana",
#     "address": {"city": "Almaty", "street": "Abay 10", "zip_code": "050000"}
# }
# user = User.model_validate(data)
# print(user.address.city)
# print(user.model_dump())
