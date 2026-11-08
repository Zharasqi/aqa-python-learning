import pytest
from pydantic import BaseModel, Field, ValidationError

class User(BaseModel):
    id: int
    name: str
    age: int = Field(ge=0)

def test_user_copy(user):
    updated_user = user.model_copy(update={"age": 34})
    assert updated_user.age == 34
    assert user.age == 33
    assert user.id == updated_user.id
    assert user.name == updated_user.name
    print(updated_user)
def test_user_copy_without_validation(user):
    updated_user = user.model_copy(update={"age": -1})
    assert updated_user.age == -1
    assert user.age == 33
    assert user.id == updated_user.id
    assert user.name == updated_user.name
    print(updated_user)
def test_user_copy_with_validation(user):
    updated_user = user.model_copy(update={'age': -2})
    dict_json = updated_user.model_dump()
    with pytest.raises(ValidationError) as err:
        User.model_validate(dict_json)
    first_error = err.value.errors()[0]
    assert first_error["loc"] == ('age',)
    assert first_error["type"] == "greater_than_equal"

