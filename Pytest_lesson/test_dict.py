# user = {
#     "name": "Dana",
#     "age": 24,
#     "is_active": True,
#     "skills": [
#         "Python",
#         "Go"
#     ]
# }
#
# def test_user_has_required_fields():
#     assert "name" in user
#     assert "age" in user
#     assert "is_active" in user
#     assert "skills" in user
#
# def test_user_name():
#     assert user["name"] == "Dana"
#
# def test_age():
#     assert user["age"] == 24
#
# def test_is_active():
#     assert user["is_active"]
#
# def test_skills():
#     assert "Python" in user["skills"]
#
# def test_count():
#     assert len(user["skills"]) == 2