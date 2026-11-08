# from pydantic import BaseModel
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
# class UserResponse(BaseModel):
#     users: list[User]
#     total: int
#
# data = {
#     "users": [
#         {"id": 1, "name": "Dana", "address": {"city": "Almaty", "street": "Abay 10", "zip_code": "050000"}},
#         {"id": 2, "name": "Zharas", "address": {"city": "Astana", "street": "Saryarka 5", "zip_code": "010000"}}
#     ],
#     "total": 2
# }
# def test_user_response():
#     resp = UserResponse.model_validate(data)
#     assert resp.total == 2
#     assert len(resp.users) == 2
#     assert resp.users[0].name == "Dana"
#     assert resp.users[1].address.city == "Astana"