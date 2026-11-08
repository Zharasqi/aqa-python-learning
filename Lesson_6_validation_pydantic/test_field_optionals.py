# from typing import Optional
#
# import pytest
# from pydantic import BaseModel, Field, ValidationError
#
#
# class User(BaseModel):
#     id: int = Field(gt=0)
#     name: str = Field(min_length=1, max_length=50)
#     age: int = Field(ge=0, le=120)
#     middle_name: Optional[str]=None
#
# def test_user_valid():
#     user = User(
#         id=1,
#         name="Dana",
#         age=26
#     )
#     assert user.id == 1
#     assert user.middle_name is None
#
# def test_invalid_age():
#     with pytest.raises(ValidationError) as exc_info:
#         User(
#             id=1,
#             name="Dana",
#             age=200,
#             middle_name="Talgat"
#         )
#     assert exc_info.value.errors()[0]["loc"] == ("age", )
#     assert exc_info.value.errors()[0]["type"] == "less_than_equal"