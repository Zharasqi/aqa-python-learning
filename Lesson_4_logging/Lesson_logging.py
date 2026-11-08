import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="app.log",
    filemode="w",
    encoding="utf-8",
    format='%(asctime)s - %(levelname)s - %(message)s - %(name)s'
)
logger = logging.getLogger(__name__)
logger.debug("Начинается вычисление")
lst = ["12", "abc", "0"]
count = 0
for i in lst:
    try:
        i = int(i)
        result = 100 / i
    except ZeroDivisionError:
        logger.exception("Ошибка вычетания на ноль нельзя делить")
    except ValueError:
        logger.exception("Значение нельзя преобразовывать в цисло")
    else:
        logger.info("Результат вычесления: %s",result)
    finally:
        count += 1
        logger.debug("Завершена обработка текущего значения, количество: %s", count)

# for i in lst:
#     try:
#         i = int(i)
#         result = 100 / i
#         logger.info(result)
#     except ZeroDivisionError:
#         logger.exception("Ошибка вычетания на ноль нельзя делить")
#     except ValueError:
#         logger.exception("Значение нельзя преобразовывать в цисло")
# logger = logging.getLogger(__name__)
# user_id = 7
# user_name = "Zharas"
# logger.info("Проверяем пользователя: id=%s, name = %s", user_id, user_name)
# logger.debug("Начинается вычесления")
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     logger.exception("Ошибка вычетания на ноль нельзя делить")
