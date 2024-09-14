'''
Задача модуля: отвечает за анализ обработку и запись полученных 
посредством API или других способов.;
________________________________________________________________________________
Дата создания: 31.08.2024;
Дата редактирования: -;
________________________________________________________________________________
Краткое описание возможностей модуля:
 - Модуль получает словарь данных на запись данных в БД;
 - К БД относиться как sql;
 - После проверки данный выполняется их запись в БД;
'''


from re import search
from typing import Any, Union

from controller.exception import exception
from database_data_template.database_date_template import DatabaseDataTemplate 


class __ConvertToDictionary:
    """
    Отвечает за преобразование объекта класса в словарь
    """

    def __init__(self) -> None:
        pass

    def __test_data_on_tuple(self,
                                   data: Union[tuple, Any],
                                   ) -> None | exception.DataNotTuple:
        """
        Проверяет, является ли data кортежем.

        :param data: Данные для проверки.
        :raises exception.DataNotTuple: Если data не является кортежем.
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

    async def _init(self, data: Union[tuple, Any]) -> dict:
        """
        Преобразует в dict.

        :param data: Данные для анализа и преобразования.
        """
        self.__test_data_on_tuple(data=data)
        data_dict = self._convert_to_dictionary(data=data)
        return data_dict

    async def __call__(self, data: Union[tuple, Any]) -> dict:
        """
        Преобразует в dict.

        :param data: Данные для анализа и преобразования.
        """

        return await self._init(data=data)


class __ParsingCleaningString:
    """
    Данный класс отчищает входные данные ()
    """

    def phone_number(self, phone_number: int | str):
        """
        Отвечает за преобразование номера телефона
        """

        phone_number = str(phone_number)
        new_phone_number = "".join([number for number in phone_number if number in "0123456789"])
        print("-" * 15)
        print(phone_number)
        if len(new_phone_number) == 10:
            pass
        elif len(new_phone_number) == 11:
            new_phone_number = new_phone_number[1:]
        else:
            text_error = "the number is incorrect"
            raise exception.ParsingCleaningStringError.PhoneNumber(text_error)

        return new_phone_number

    def mail(self, mail: str):
        """
        Отвечает за преобразование почты
        """

        if not "@" in mail:
            text_error = f"({mail}) is missing the (@) symbol"
            raise exception.ParsingCleaningStringError.MailError(text_error)
            # raise exception.ParsingCleaningStringError.MailError(text_error)
        if not "." in mail[mail.index("@"):]:
            text_error = f"({mail}) is missing the (.) symbol"
            raise exception.ParsingCleaningStringError.MailError(text_error)
        re_mail = search(pattern=r"(\S+@\S+\.\S+)", string=mail)
        if re_mail:
            return re_mail.group()
        else:
            text_error = "the email address is incorrect"
            raise exception.ParsingCleaningStringError.MailError(text_error)
            
        
    def social_network_names(self, name: str):
        """
        Обрабатывает имена из соц сетей, удаляя символ (@)
        """
        return name.replace("@", "")

    def _main(self,
            item_name: str,
            meaning: Union[str, int, bool],
            ) -> None:
        
        meaning = meaning.strip() # отчистка от пробелов по бокам
        
        if item_name == "phone_number":
            return self.phone_number(phone_number=meaning)
        elif item_name == "mail": 
            return self.mail(mail=meaning)
        elif item_name == ("user_name_tg", "vk"):
            return self.social_network_names(name=meaning)
        else:
            return meaning

    def __call__(self,
                 item_name: str,
                 meaning: Union[str, int, bool],
                 ) -> None | Exception:
        """
        Отвечает за отчистку данных
        """

        return self._main(
            item_name=item_name,
            meaning=meaning,
        )


class __InputDataChecking:
    """
    Данный класс отвечает за проверку входных данных
    """

    def __test_data(self, data: dict) -> None | exception.DataNotDict:
        if not isinstance(data, dict):
            text_error = f"data ({data}) is not a 'dict'"
            raise exception.DataNotDict(text_error)

    def __init__(self) -> None:
        pass

    def _main_test(self, data: dict) -> None:
        """
        Отвечает за проверку ключа и значения 

        :param data: Словарь с ключем в виде ячейки БД
            и значение соответствующее условиям
            описанным в DatabaseDataTemplate.
        """
        new_data = {}
        self.__test_data(data=data) # проверка: является ли data словарем
        for item_name, meaning in data.items():
            # экземпляры
            database_data_template = DatabaseDataTemplate()
            parsing_cleaning_string = __ParsingCleaningString()

            field_parameters = database_data_template.key_get(key=item_name) # возвращает исключение или параметры для проверки поля
            processed_meaning = parsing_cleaning_string(
                item_name=item_name,
                meaning=meaning,
                ) # выполняет отчистку строки и возврощает
            database_data_template.meaning_test(
                meaning=processed_meaning,
                parameters=field_parameters,
                ) # проверка параметров отчищенных данных 
            
            new_data[item_name] = processed_meaning
        
        return new_data

        фыв 0 # запись в БД

    def _init(self, data: dict) -> dict:
        self.__test_data(data=data)
        return self._main_test(data=data)

    async def __call__(self, data: dict) -> dict:
        return self._init(data=data)


class Converting_Data_For_Database:
    """
    Разбивает данные по словарям
    """

    def __init__(self) -> None:
        pass

    async def 

    async def _init(self, data: dict):
        return await self.

    async def __call__(self, data: dict) -> None:
        return await self._init(data=data)

class ApiController:
    """
    Отвечате за обработку и запись данных в БД
    """

    def __init__(self) -> None:
        pass

    async def _scenario(self, data: Union[tuple, Any]) -> str:
        # инициализация экземпляров
        convert_to_dictionary = __ConvertToDictionary() # выполняется конвертация данный объекта в словарь
        input_data_checking = __InputDataChecking()

        # запуск __call__ экземпляров
        data_dict = await convert_to_dictionary(data=data) # преобразование
        verified_data = await input_data_checking(data=data_dict)

    async def _init(self, data: Union[tuple, Any]) -> str:
        try:
            return await self._scenario(data=data)
        except Exception as error:
            pass

    async def __call__(self, data) -> str:
        return await self._init(data=data)