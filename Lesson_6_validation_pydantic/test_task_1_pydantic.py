import pytest
from pydantic import BaseModel, Field, ValidationError

class User(BaseModel):
    id: int
    name: str
    age: int = Field(ge=0)

def test_user_data(user):
    assert user.id == 1
    assert user.name == 'Zharas'
    assert user.age == 33
def test_user_invalid_age():
    with pytest.raises(ValidationError) as err:
        User(id=1, name='Zharas', age=-1)
    first_error = err.value.errors()[0]
    assert first_error["loc"][0] == 'age'
    assert first_error["type"] == "greater_than_equal"
    print(first_error["type"])
