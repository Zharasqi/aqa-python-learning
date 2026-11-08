from datetime import datetime, date

today = date.today()
response = {
    "created_at": "2026-09-03",
    "expires_at": "2026-09-10"
}
date_created = datetime.strptime(response["created_at"], "%Y-%m-%d").date()
date_expire = datetime.strptime(response["expires_at"], "%Y-%m-%d").date()

assert today == date_created,"Дата создания должна быть сегодняшней"
assert date_created < date_expire, "Дата окончания должна быть позже даты создания"

# today = date.today()
# response = {
#     "created_at": "2026-09-03"
# }
# date_stock = response["created_at"]
# date_res = datetime.strptime(date_stock, "%Y-%m-%d").date()
# assert today == date_res, "Дата создания должна быть сегодняшней"
# response = {
#     "id": 1,
#     "name": "Promo",
#     "expires_at": "2026-09-06"
# }
# date_stock = response["expires_at"]
# date_res = datetime.strptime(date_stock, "%Y-%m-%d").date()
# if today <= date_res:
#     print("OK")
# else:
#     print("ERROR")
# date_from_api = "2026/09/06"
# print(datetime.strptime(date_from_api, "%Y/%m/%d").date())
# print(datetime.strptime("06.09.2026", "%d.%m.%Y").date())
# date_from_api = "2026-09-06"
# date_api = datetime.strptime(date_from_api, "%Y-%m-%d").date()
# today = date.today()
# if today <= date_api:
#     print("Дата корректная")
# else:
#     print("Дата некорректная")
# date_from_time = "2026-09-06"
# print(datetime.strptime(date_from_time, "%Y-%m-%d"))
# print(today.strftime("%d.%m.%Y"))
# print(today.strftime("%Y/%m/%d"))