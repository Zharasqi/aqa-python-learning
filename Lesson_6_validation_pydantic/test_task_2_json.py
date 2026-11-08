import json
from pydantic import BaseModel, Field

class User(BaseModel):
    id: int
    name: str
    age: int = Field(ge=0)

def test_user_json(user):
    json_text = user.model_dump_json()
    assert isinstance(json_text, str)
    data = json.loads(json_text)
    assert data["name"] == "Zharas"
    assert data["age"] == 33
    assert data["id"] == 1