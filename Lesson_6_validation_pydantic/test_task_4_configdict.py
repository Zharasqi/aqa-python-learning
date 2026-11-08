from pydantic import BaseModel, Field, ConfigDict, ValidationError
import pytest

class User(BaseModel):
    id: int
    name: str
    age: int = Field(ge=0)
    model_config = ConfigDict(extra="forbid")

user_data = {
        'id': 1,
        'name': 'Zharas',
        'age': 33,
        "email": "zharas@mail.ru"
    }
def test_user_data():
    with pytest.raises(ValidationError) as e:
        User.model_validate(user_data)
    first_error = e.value.errors()[0]
    assert first_error['loc'] == ('email',)
    assert first_error['type'] == "extra_forbidden"