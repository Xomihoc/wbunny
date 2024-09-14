from typing import Any

from controller.exception import exception


class DatabaseDataTemplate:

    def __get_exceptions(
            from_table,
            place,
            request,
            ):
        """
        Формирует исключение если не неаходится ссылки на другую таблицу
        """
        text_error = f"Field ({place}) not found in table ({request}) from table ({from_table})"
        raise exception.ForeignKeyFieldError(text_error)
    
    USERS_DATA = {
        "user_id_tg": {
            "null": True,
            "min_length": None,
            "max_length": 30,
            "type": int,
        },
        "user_name_tg": {
            "null": True,
            "min_length": None,
            "max_length": 32,
            "type": str,
        },
        "registered": {
            "null": True,
            "type": bool,
        },
        "account_status": {
            "null": True,
            "type": bool,
        },
        "role": {
            "null": None,
            "min_length": 1,
            "max_length": 25,
            "type": str,
            "value": (),
        },
        "admin_role": {
            "null": True,
            "type": bool,
        },
        "first_name": {
            "null": True,
            "min_length": None,
            "max_length": 30,
            "type": str,
        },
        "last_name": {
            "null": True,
            "min_length": None,
            "max_length": 50,
            "type": str,
        },
        "patronymic": {
            "null": True,
            "min_length": None,
            "max_length": 30,
            "type": str,
        },
        "phone_number": {
            "null": True,
            "min_length": None,
            "max_length": 10,
            "type": str,
        },
        "name_educational_institution": {
            "null": True,
            "min_length": None,
            "max_length": 200,
            "type": str,
        },
        "record_book": {
            "null": True,
            "min_length": None,
            "max_length": 15,
            "type": int,
        },
        "vk": {
            "null": True,
            "min_length": None,
            "max_length": 100,
            "type": str,
        },
        "speciality": {
            "null": True,
            "min_length": None,
            "max_length": 75,
            "type": str,
        },
        "mail": {
            "null": True,
            "min_length": None,
            "max_length": 300,
            "type": str,
        },
    }

    ORDERS_DATA = {
        "status": {
            "null": None,
            "min_length": 1,
            "max_length": 40,
            "type": str,  # Изменено
        },
        "work_option": {
            "null": None,
            "min_length": 1,
            "max_length": 20,
            "type": str,  # Изменено
            "value": (),
        },
        "scope_of_work": {
            "null": None,
            "min_length": 1,
            "max_length": 25,
            "type": str,  # Изменено
            "value": (),
        },
        "terms_of_reference": {
            "null": None,
            "min_length": 1,
            "max_length": 2000,
            "type": str,  # Изменено
        },
        "submission_deadline": {
            "null": True,
            "min_length": None,
            "max_length": 30,
            "type": str,  # Изменено
        },
        "customer_id": {
            "null": True,
            "min_length": None,
            "max_length": 30,
            "type": int,
        },
        "copywriter_id": {
            "null": True,
            "min_length": None,
            "max_length": 30,
            "type": int,
        },
        "programmer_id": {
            "null": True,
            "min_length": None,
            "max_length": 30,
            "type": int,
        },
        "course_project_topic": {
            "null": None,
            "min_length": 1,
            "max_length": 125,
            "type": str,  # Изменено
        },
        "teacher": {
            "null": True,
            "min_length": None,
            "max_length": 200,
            "type": str,  # Изменено
        },
        "grade": {
            "null": None,
            "min_length": 1,
            "max_length": 1,
            "type": str,  # Изменено
            "value": (),
        },
        "customer_status": {
            "null": True,
            "min_length": None,
            "max_length": 25,
            "type": str,  # Изменено
        },
        "copywriter_status": {
            "null": True,
            "min_length": None,
            "max_length": 25,
            "type": str,  # Изменено
        },
        "programmer_status": {
            "null": True,
            "min_length": None,
            "max_length": 25,
            "type": str,  # Изменено
        },
        "programmer_job_status": {
            "null": None,
            "min_length": 1,
            "max_length": 25,
            "type": str,  # Изменено
            "value": (),
        },
        "copywriter_job_status": {
            "null": None,
            "min_length": 1,
            "max_length": 25,
            "type": str,  # Изменено
            "value": (),
        },
        "software_curs": {
            "null": True,
            "min_length": None,
            "max_length": 25,
            "type": str,  # Изменено
        },
        "adaption": {
            "null": None,
            "type": bool,  # Обновлено, заменено на bool
        },
        "animation": {
            "null": None,
            "type": bool,  # Обновлено, заменено на bool
        },
        "price": {
            "null": None,
            "min_length": 1,
            "max_length": None,
            "type": int,  # Изменено (можно использовать str для представления цены)
        },
    }

    # Пример данных для класса Message
    MESSAGE_DATA = {
        "message_text": {
            "null": True,
            "min_length": None,
            "max_length": None,
            "type": str,
        },
        "user": {
            "null": True,
            "min_length": None,
            "max_length": 30,
            "type": int,
        },
        "message_type": {
            "null": None,
            "min_length": None,
            "max_length": 25,
            "type": str, # УКАЗАТЬ ТИПЫ СООБЩЕНИЙ
            "value": (), # УКАЗАТЬ ТИПЫ СООБЩЕНИЙ
        },
        "status": {
            "null": None,
            "min_length": 1,
            "max_length": 25,
            "type": str, # УКАЗАТЬ ТИПЫ СООБЩЕНИЙ
            "value": (), # УКАЗАТЬ ТИПЫ СООБЩЕНИЙ
        },
    }

    async def converter(self, data: dict) -> dict:
        tables = {
            "users_data": self.USERS_DATA,
            "orders_data": self.ORDERS_DATA,
            "message_user": self.MESSAGE_DATA,
        }
        new_data = {}
        for name, item in data.items():
            get_users = tables["users_data"].get(name, False)
            get_orders = tables["orders_data"].get(name, False)
            get_message = tables["message_user"].get(name, False)

            if get_users:
                new_data["users"] = get_users[name] = item
            elif get_orders:
                new_data["orders"] = get_orders[name] = item
            elif get_message:
                new_data["message"] = get_message[name] = item
            else:
                text_error = f"name ({name}) not found in one of (({get_users}), ({get_orders}), ({get_message}))"
                raise exception.ConverterError(text_error)
            
    def key_get(self, key: str):
        """
        Модуль проверяет налицие отправленного ключа в базе
        """
        data = [self.USERS_DATA, self.ORDERS_DATA, self.MESSAGE_DATA]

        for table in data:
            for name, parameters in table.items():
                if key == name:
                    return parameters 
        else:
            text_error = f"the specified key ({key}) was not found"
            raise exception.ColumnNameNotFound(text_error)
        
    def meaning_test(self,
            meaning: Any,
            parameters: dict,
            ):
        """
        Проверка на соответствие параметрам
        """
        null = parameters.get("null", "not_found")
        min_length = parameters.get("min_length", "not_found")
        max_length = parameters.get("max_length", "not_found")
        data_type = parameters.get("type", "not_found")
        value = parameters.get("value", "not_found")

        if not null == "not_found":
            if len(meaning) <= 0 and not null:
                text_error = f"string size ({meaning}) must be greater than zero"
                raise exception.MeaningTestError.NullError(text_error)
            elif len(meaning) <= 0 and null: # если строка не обязательна к заполнению и ее размер равен нулю
                return # возвращаем пустую строку 
        if not min_length == "not_found":
            if len(meaning) < min_length:
                text_error = f"the lower ({meaning}) row threshold ({min_length}) is equal to"
                raise exception.MeaningTestError.MinLengthError(text_error)
        if not max_length == "not_found":
            if len(meaning) > max_length:
                text_error = f"row upper threshold ({meaning}) is ({max_length})"
                raise exception.MeaningTestError.MaxLengthError(text_error)
        if not data_type == "not_found":
            if not isinstance(meaning, data_type):
                text_error = f"the data type of string ({meaning}) must be ({data_type})"
                raise exception.MeaningTestError.DataTypeError(text_error)
        if not value == "not_found":
            if not meaning.lower() in value:
                text_error = f"Available values ​({value}) strings ({meaning})"
                raise exception.MeaningTestError.ValueMatchingError(text_error)
