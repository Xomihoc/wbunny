'''
Данный модуль отвечает за чтение данных  из бд;
Дата создания: 28.08.2024;
Дата изменения: -;
'''


from typing import Any, Dict, List, Union

from tortoise.exceptions import MultipleObjectsReturned

from backend.database_queries.database.config.models.models import (
    Message,
    Orders,
    Users, 
)
from backend.database_queries.database.config.settings.init import init
from backend.database_queries.requests.reading.data_test.test_model import Test_model
from backend.database_queries.exceptions import exceptions


class ReadingTable:
    """
    Данный класс отвечает за чтение данных из таблиц: Users, Orders, Message.
    """


    def __init__(self) -> None:
        pass

    async def read_get(self,
                       model: (Users | Orders | Message),
                       **kwargs: Dict[str, Any],
                       ) -> Union[List[Dict[str, Any]], None]:
        await init() # иницыализация конфигурации базы данных
        """
        Выводить только одну запись, проходящюю по фильтрам.
        В противном случае возвращает исключение 
            HandlingNamedArgument.tortoise.exceptions.MultipleObjectsReturned:

        :param model: Один из клаассов - Users, Orders, Message.
        :param kwargs: Арибуты спецефичные для переданного класса.
                        Принимаются в качестве фильтров.
        """

        await Test_model.test_model(model=model)
        try:
            return await model.get(**kwargs)
        except MultipleObjectsReturned as error:
            raise exceptions.ExpectedExactlyOne(error)


    async def read_filter(self, model: (Users | Orders | Message),
                          **kwargs: Dict[str, Any],
                          ) -> Union[List[Dict[str, Any]], None]:
        """
        Выводить перечень всех записей проходящих по фильтрам.

        :param model: Один из клаассов - Users, Orders, Message.
        :param kwargs: Арибуты спецефичные для переданного класса.
                        Принимаются в качестве фильтров.
        """

        await Test_model.test_model(model=model)
        return await model.filter(**kwargs)

    async def read_filter_first(self, model: (Users | Orders | Message),
                                **kwargs: Dict[str, Any],
                                ) -> Union[List[Dict[str, Any]], None]:
        """
        Выводить из полученной перечни первый результат проходящих по фильтрам.

        :param model: Один из клаассов - Users, Orders, Message.
        :param kwargs: Арибуты спецефичные для переданного класса.
                        Принимаются в качестве фильтров.
        """

        await Test_model.test_model(model=model)
        return await model.filter(**kwargs).first()
