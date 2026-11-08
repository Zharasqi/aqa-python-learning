import pytest

# def test_get_token(get_token):
#     assert get_token["token"] == "abc123"
#
# def test_get_token_value(get_token):
#     assert get_token == {"token": "abc123"}
# def test_temp_fail_content(temp_file):
#     file_content = temp_file.read_text()
#     assert file_content == "hello"
# def test_users_count(user_list):
#     assert len(user_list) == 2
#
# def test_first_user_id(user_list):
#     assert user_list[0]["id"] == 1
# def test_new_user(new_user):
#     assert new_user["name"] == "Dana"

# def test_new_user(new_user):
#     assert new_user["username"] == "Zharas"
#     assert new_user["status"] == "active"

# def test_token_is_not_empty(api_token):
#     assert len(api_token) > 0

# @pytest.fixture
# def shopping_cart():
#     data = ["laptop", "mouse", "keyboard"]
#     print("Список товаров создался")
#
#     yield data
#
#     print("[Cleanup] Очищаем корзину")
#
# def test_cart_not_empty(shopping_cart):
#     assert len(shopping_cart) > 0
# @pytest.fixture
# def sample_user():
#     # 1. Шаг подготовки (до yield): создаем данные для теста
#     user_data = {"id": 101, "name": "Zharas", "role": "QA"}
#     print("\n[Setup] Пользователь создан в базе")
#
#     # Отдаем данные в тест
#     yield user_data
#
#     # 2. Шаг очистки (после yield): удаляем данные, чтобы не оставлять мусор
#     print("\n[Teardown] Пользователь удален из базы")
#
#
# def test_user_role(sample_user):
#     # Тест просто принимает фикстуру в аргументах и использует её готовые данные
#     assert sample_user["role"] == "QA"
#     assert sample_user["id"] > 0