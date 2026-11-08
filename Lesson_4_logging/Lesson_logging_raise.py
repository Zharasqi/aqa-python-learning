import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="app.log",
    filemode="w",
    encoding="utf-8",
    format='%(asctime)s - %(levelname)s - %(message)s - %(name)s'
)
logger=logging.getLogger(__name__)
def validate_age(age):
    if 0 > age  or age > 120:
        raise ValueError("Age must be between 0 and 120")
    else:
        return age
lst = [25, -5, 150]
for i in lst:
    try:
        validate_age(i)
        logger.info("Возраст корректный: %s", i)
    except ValueError:
        logger.exception("Некорректный возраст: %s", i)