'''
Данный модуль отвечает за запись или перезапись данных в бд;
Дата создания: 28.08.2024;
Дата изменения: -;

Проблема с логером


'''


from typing import *

from tortoise.exceptions import ValidationError
from tortoise import Tortoise

from backend.database_queries.database.config.models.models import (
    Message,
    Orders,
    Users,
)
from backend.database_queries.database.config.settings.init import init
from backend.database_queries.requests.reading.data_test.test_model import Test_model
from backend.database_queries.exceptions import exceptions


class CreateDataTable:
    """
    Данный класс отвечате за создание новых записей в таблицах базы данных.
    """

    def __init__(self) -> None:
        pass

    async def data_record(self,
                          model: (Users | Orders | Message),
                          **kwargs: Dict[str, Any],
                          ) -> Union[List[Dict[str, Any]], None]:
        await init() # иницыализация конфигурации базы данных
        """
        Записывает словарь данных в указанную model.

        :param model: Один из клаассов - Users, Orders, Message.
        :param kwargs: Арибуты спецефичные для переданного класса.
                        Принимаются в качестве данных для записи.
        """

        await Test_model.test_model(model=model)
        await Test_model.test_kwargs(kwargs=kwargs)
        try:
            await model.create(**kwargs)
        except ValidationError as error:
            text_exception = f"Обработанный Validation: {error}"
            raise ValidationError(text_exception)
        except Exception as error:
            pass

        await Tortoise.close_connections()


class RewriteDataTable:
    """
    Данный клас выполняет перезапись данных в таблицах базы данных.
    """

    def __init__(self) -> None:
        pass

    async def data_rewrite(self,
                           model: (Users | Orders | Message),
                           data_rewrite: Dict[str, Any],
                           **kwargs: Dict[str, Any],
                           ) -> Union[List[Dict[str, Any]], None]:
        await init() # иницыализация конфигурации базы данных
        """
        Перезаписывает словарь данных в указанную model.

        :param model: Один из классов - Users, Orders, Message.
        :param data_rewrite: Новые данные.
        :param kwargs: Арибуты спецефичные для переданного класса.
                        Принимаются в качестве данных для записи.
        """

        await Test_model.test_model(model=model)
        await Test_model.test_kwargs(kwargs=kwargs)
        try:
            await model.filter(**kwargs).update(**data_rewrite)

        except ValidationError:
            pass
        except Exception as text_exception:
            raise exceptions.NotDetectException(text_exception)

        await Tortoise.close_connections()

