'''
Данный сценарий отвечает за запись данных в БД, полученных послердством API

Дата создания: 04.09.2024;
Дата изменения: -;
'''


from typing import Any, Union
import asyncio

from backend.exception import exception
from backend.filter.filter import FilterData
from backend.database_queries.main_requests import Requests
from backend.database_queries.database.config.models.models import Users, Orders


class ScenariesWebApi:
    """
    Данный сценарий выполняет анализ данных полученных посредством API, 
        а следом записывает в БД;
    """

    def __init__(self) -> None:
        pass

    async def _main(self, data):
        # экземпляры
        converting_object_dictionary = _ConvertingObjectDictionary()
        filter_data_api = _FilterDataApi()
        array_formation = _ArrayFormation()
        record_data_base = _RecordDataBase()

        # инициализация 
        data_dict = converting_object_dictionary(data=data) # преобразует в словарь
        filtered_data_dict = filter_data_api(data=data_dict)
        array_formation_dict = array_formation(data=filtered_data_dict)
        record_data_base_dict = await record_data_base(data=array_formation_dict)
        return record_data_base_dict

    async def _forming_response(self, data):
        try:
            return await self._main(data=data)
        except exception.DataNotTuple as text_error:
            return text_error
        except exception.FilterError as text_error:
            return text_error
        except exception.ScenariesWebApiFilterError as text_error:
            return text_error
        except exception.ScenariesWebApiFilterError.WorkOptionError as text_error:
            return text_error
        except exception.ScenariesWebApiFilterError.SoftwareCursError as text_error:
            return text_error
        except exception.ScenariesWebApiFilterError.TermsOfReferenceError as text_error:
            return text_error
        except exception.ScenariesWebApiFilterError.EvaluationError as text_error:
            return text_error
        except exception.ScenariesWebApiFilterError.AdaptionError as text_error:
            return text_error
        except exception.ScenariesWebApiFilterError.AnimationError as text_error:
            return text_error
        except exception.ScenariesWebApiFilterError.PriceError as text_error:
            return text_error
        except exception.ScenariesWebApiFilterError.SpecialtyError as text_error:
            return text_error
        except exception.ScenariesWebApiFilterError.FullNameError as text_error:
            return text_error
        except exception.ScenariesWebApiFilterError.TeacherError as text_error:
            return text_error
        except exception.ScenariesWebApiFilterError.NumberPhoneError as text_error:
            return text_error
        except exception.ScenariesWebApiFilterError.UserNameTgError as text_error:
            return text_error
        except exception.ScenariesWebApiFilterError.MailError as text_error:
            return text_error
        except exception.ScenariesWebApiFilterError.VkError as text_error:
            return text_error
        except exception.ArrayFormation as text_error:
            return text_error
        except exception.RecordDataBaseError as text_error:
            return text_error

             
    async def __call__(self, data) -> None:
        return await self._forming_response(data=data)


class _ConvertingObjectDictionary:
    """
    Преобразует объект в словарь
    """

    def __init__(self) -> None:
        pass

    def __test_data_on_tuple(self, data: Union[tuple, Any]) -> None:
        """
        Проверяет, является ли data кортежем.
        """

        for element in data:
            if not isinstance(element, tuple):
                text_error = f"element ({element}) is not a 'tuple'"
                raise exception.DataNotTuple(text_error)
            
    def _convert_to_dictionary(self, data: Union[tuple, Any]) -> dict:
        """
        Проверяет, является ли data кортежем.

        :param data: Данные для преобразования.
        """
        
        new_data = {}
        
        for element in data:
            key = element[0]
            meaning = element[1]

            new_data[key] = meaning
        return new_data

    def __call__(self, data: Union[tuple, Any]) -> dict:
        """
        Преобразует в dict.

        :param data: Данные для анализа и преобразования.
        """

        self.__test_data_on_tuple(data=data)
        return self._convert_to_dictionary(data=data)


class _FilterDataApi:
    """
    Выполняет проверку данных.
    """

    def __init__(self) -> None:
        self.init_filter_data = FilterData() # экземпляр класса с фильтрами

    def _data_filtering(self, data: dict) -> dict:
        """
        Подбирает фильтр и выполняет отчистку данных.

        :param data: Неотфильтрованные данные.
        """
        filter_set = {
            "work_option": self.init_filter_data.work_option,
            "software_curs": self.init_filter_data.software_curs,
            "terms_of_reference": self.init_filter_data.terms_of_reference,
            "evaluation": self.init_filter_data.evaluation,
            "adaption": self.init_filter_data.adaption,
            "animation": self.init_filter_data.animation,
            "price": self.init_filter_data.price,
            "specialty": self.init_filter_data.specialty,
            "full_name": self.init_filter_data.full_name,
            "teacher": self.init_filter_data.teacher,
            "number_phone": self.init_filter_data.number_phone,
            "user_name_tg": self.init_filter_data.user_name_tg,
            "mail": self.init_filter_data.mail,
            "vk": self.init_filter_data.vk,
        }

        new_data = {}

        for key, item in data.items():
            record = filter_set.get(key)
            if record:
                answer = record(item)
                if key == "full_name":
                    new_data["first_name"] = answer[0]                 
                    new_data["last_name"] = answer[1]                 
                    new_data["patronymic"] = answer[2]   
                else:              
                    new_data[key] = answer
            else:
                text_error = f"incorrect parameter ({key}) - ({item})"
                raise exception.FilterError(text_error)
            
        return new_data

    def __call__(self, data: dict) -> dict:
        """
        Подбирает фильтр и выполняет отчистку данных.

        :param data: Не отфильтрованные данные.
        """
        return self._data_filtering(data=data)


class _ArrayFormation:
    """
    Формирование словаря для записи в БД
    """

    def __init__(self) -> None:
        pass

    def _table_search(self, name_item: str, table: str) -> bool:
        return name_item in self.__table_structure[table]

    def _formation_of_dictionary(self, data: dict) -> dict:
        table_structure = {
            "Users": {
                "user_name_tg": data.get("user_name_tg"),                # tg_name
                "role": "пользователь",                         # роль
                "first_name": data.get("first_name"),                   # имя
                "last_name": data.get("last_name"),                    # фамилия
                "patronymic": data.get("patronymic"),                   # отчество
                "phone_number": data.get("number_phone"),                 # номер телефона
                "record_book": data.get("record_book"),                  # номер зачетной книжки
                "vk": data.get("vk"),                           # вк
                "specialty": data.get("specialty"),                   # специальность
                "mail": data.get("mail"),                          # почта
            },
            "Orders": {
                "status": "размещен",                   # статус (размещен)
                "work_option": data.get("work_option"),           # вариант работы
                "scope_of_work": "полная",                 # объем работы
                "terms_of_reference": data.get("terms_of_reference"),           # техническое задание
                "teacher": data.get("teacher"),                     # преподаватель
                "evaluation": data.get("evaluation"),                   # оценка
                "software_curs": data.get("software_curs"),               # web or desktop program
                "adaption": data.get("adaption"),                    # адаптив сайта делать или нет
                "animation": data.get("animation"),                    # объем анимаций больше меньше
                "price": data.get("price"),                        # стоимость работы
            },
        }
            
        return table_structure

    def __call__(self, data: dict) -> dict:
        return self._formation_of_dictionary(data=data)


class _RecordDataBase:
    """
    Выполняет запись данных  в БД
    """

    def __init__(self) -> None:
        pass

    async def _record_data_base(self, data: dict) -> None:
        self.copy_requests = Requests()

        for name_table, data_table in data.items():
            if name_table == "Users":
                await self.copy_requests.data_record(
                    model=Users(),
                    **data_table,
                )
            elif name_table == "Orders":
                await self.copy_requests.data_record(
                    model=Orders(),
                    **data_table,
                )
            else:
                text_error = "table error"
                raise exception.RecordDataBaseError(text_error)
        return True

    async def __call__(self, data: dict) -> None:
        return await self._record_data_base(data=data)
