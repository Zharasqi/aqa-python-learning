

# today = date.today()
# week_day = today + timedelta(days=7)
#
# if today <= week_day:
#     print("Промокод активен")
# else:
#     print("Промокод истёк")
from datetime import date, timedelta
today = date.today()
final_day = today - timedelta(days=1)

if today <= final_day:
    print(f"Промокод активен: {final_day}")
else:
    print(f"Промокод истёк: {final_day}")