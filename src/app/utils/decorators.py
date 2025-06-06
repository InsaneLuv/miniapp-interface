import functools

from httpx import HTTPStatusError, HTTPError
from litestar.status_codes import HTTP_429_TOO_MANY_REQUESTS, HTTP_404_NOT_FOUND
from pydantic_core import ValidationError
import logging

logger = logging.getLogger('ew')

def exceptions_wrapped(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except HTTPStatusError as exc:
            if exc.response.status_code == HTTP_429_TOO_MANY_REQUESTS:
                logger.warning(f"Клиентский сервис отклонил запрос: {exc}")
                return exc
            if exc.response.status_code == HTTP_404_NOT_FOUND:
                logger.warning(f"Клиентский сервис не вернул данные: {exc}")
                return exc
            logger.critical(f"Необработанное исключение: {exc}")
            raise
        except HTTPError as exc:
            logger.critical(f"Потеряно интернет-соединение: {exc}")
            raise
        except ValidationError as exc:
            logger.warning(f"Модель не прошла валидацию с аргументами [{args}] [{kwargs}]: {exc}")
            return exc

    return wrapper
