import pytest
from Lesson_6_validation_pydantic.test_task_1_pydantic import User

@pytest.fixture
def user():
    user_data = {
        'id': 1,
        'name': 'Zharas',
        'age': 33
    }
    return User.model_validate(user_data)


# @pytest.fixture()
# def get_token():
#     print("\nsetup session")
#     token = {"token": "abc123"}
#     yield token
#     print("\nteardown session")

# @pytest.fixture
# def user_data():
#     user = {
#     "id": 1,
#     "name": "Dana",
#     "age": 24
# }
#     print(f"\n[Setup] Тестовый пользователь создан\nuser = {user}")
#     yield user
#     print("\n[Teardown] Удаляем тестового пользователя")

# @pytest.fixture()
# def temp_file():
#     folder = Path("test_data")
#     folder.mkdir(exist_ok=True)
#     file_path = folder / "tmp.txt"
#     file_path.write_text("hello")
#
#     yield file_path
#
#     file_path.unlink()
# @pytest.fixture(scope="module")
# def user_list():
#     user_list = [{
#     "id": 1,
#     "name": "Dana",
#     "age": 24
# }, {
#     "id": 2,
#     "name": "Zharas",
#     "age": 26
#     }]
#     print(f"\n[Setup] Тестовый пользователь создан\nuser = {user_list}")
#     yield user_list
#     print("\n[Teardown] Удаляем тестового пользователя")

