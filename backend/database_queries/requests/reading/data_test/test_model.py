'''
____
'''


from typing import Dict, Any

from backend.database_queries.database.config.models.models import (
    Message,
    Orders,
    Users, 
)
from backend.database_queries.exceptions import exceptions


class Test_model:
    async def test_model(model) -> None | exceptions.ModelError:
        """
        Данный метод отвечает за проверку корректной передачи экземпляра таблицы.
        """

        if not isinstance(model, (Users, Orders, Message)):
            print(model)
            text_exception = f"Указан неверный модуль ({model})"
            raise exceptions.ModelError(text_exception)
        
    async def test_kwargs(
            **kwargs: Dict[str, Any],
            ) -> None | exceptions.KwargsError:
        """
        Данный метод отвечает за проверку корректной передачи 
            именнованных аргументов.
        """

        if not isinstance(kwargs, dict):
            text_exception = f"Переданные kwargs не являются dict"
            raise exceptions.KwargsError(text_exception)
        