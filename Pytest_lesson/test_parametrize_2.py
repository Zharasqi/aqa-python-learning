# import pytest
#
# def has_required_fields(user):
#     if "id" in user and "name" in user and "email" in user:
#         return True
#     else:
#         return False
#
# @pytest.mark.parametrize(
#     "user, expected_result",
#     [
#         ({"id": 1, "name": "John", "email": ""},  True),
#         ({"id": 1, "name": "John"},False),
#         ({"id": 1, "email": ""}, False)
#     ],
#     ids=["correct data", "not email", "not name"]
# )
#
# def test_has_required_fields(user,expected_result):
#     result = has_required_fields(user)
#     assert result == expected_result