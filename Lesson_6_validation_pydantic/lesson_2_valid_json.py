from pydantic import BaseModel
from pydantic import ValidationError
class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool

bad_data = {"id": "abc", "name": "Dana", "email": "dana@example.com", "is_active": True}
try:
    bad_json = User.model_validate(bad_data)
except ValidationError as e:
    print("Всего ошибок:", len(e.errors()))
    for err in e.errors():
        print(err["loc"], err["type"], err["msg"])

# json_str = '{"id": 1, "name": "Dana", "email": "dana@example.com", "is_active": true}'
# user = User.model_validate_json(json_str)
# print(user.model_dump())