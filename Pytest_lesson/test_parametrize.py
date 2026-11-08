# from idlelib.iomenu import encoding
# import pytest
#
# def get_user_message(status_code):
#     if status_code == 200:
#         return "Успех"
#     elif status_code == 404:
#         return "Данные не найдены"
#     else:
#         return "Сервер временно недоступен"
# @pytest.mark.parametrize(
#     "status_code, expected_message",
#     [
#         (200, "Успех"),
#         (404, "Данные не найдены"),
#         (500, "Сервер временно недоступен"),
#     ],
#     ids=["Success", "Not Found", "Serve-error"]
# )
# def test_get_user_message(status_code, expected_message):
#     result = get_user_message(status_code)
#     assert result == expected_message
#
# # def is_success_status(status_code):
# #     return 200 <= status_code < 300
# #
# # @pytest.mark.parametrize(
# #     "status_code, expected_result",
# #     [
# #         (200, True),
# #         (201, True),
# #         (400, False),
# #         (404, False),
# #         (500, False),
# #     ],
# #     ids = ["status_code-200", "status_code-201", "status_code-400", "status_code-404", "status_code-500"],
# # )
# # def test_is_success_status(status_code, expected_result):
# #     result = is_success_status(status_code)
# #     assert result == expected_result
#
# # def is_adult(age):
# #     return age >= 18
# # @pytest.mark.parametrize(
# #     "age, expected_result",
# #     [
# #         (13, False),
# #         (18, True),
# #         (21, True),
# #     ]
# # )
# # def test_is_adult(age, expected_result):
# #     result = is_adult(age)
# #     assert result == expected_result