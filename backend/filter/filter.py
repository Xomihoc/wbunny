'''
Формируется список фильтров, для проверки данных
'''


from re import search, fullmatch

from backend.exception import exception


class FilterData:
    """
    Формируется список фильтров, для проверки данных
    """

    def __init__(self) -> None:
        pass

    def work_option(self, work_option: str) -> str:
        """
        Проверка вариаций работ
        """

        if work_option.lower() in ["курсовая"]:
            return work_option
        else:
            text_error = f"invalid type of work specified ({work_option})"
            raise exception.ScenariesWebApiFilterError.WorkOptionError(text_error)
        
    def software_curs(self, software_curs: str) -> str:
        """
        Проверка вида программы
        """

        if software_curs.lower() in ["web", "desktop"]:
            return software_curs
        else:
            text_error = f"invalid program type specified ({software_curs})"
            raise exception.ScenariesWebApiFilterError.SoftwareCursError(text_error)
        
    def terms_of_reference(self, terms_of_reference: str) -> str:
        """
        Техническое задание к проект
        """

        if 0 < len(terms_of_reference) <= 2000:
            return terms_of_reference
        else:
            text_error = "technical specification exceeds the permissible number of characters from 1 to 2000"
            raise exception.ScenariesWebApiFilterError.TermsOfReferenceError(text_error)

    def evaluation(self, evaluation: int) -> int:
        """
        Проверка желаемой оценки
        """

        if evaluation in [1, 2, 3, 4, 5]:
            return evaluation
        else:
            text_error = f"you specified an incorrect rating type ({evaluation})"
            raise exception.ScenariesWebApiFilterError.EvaluationError(text_error)
        
    def adaption(self, adaption: bool) -> bool:
        """
        Адаптив 
        """

        if isinstance(adaption, bool):
            return adaption
        else:
            text_error = "invalid data type specified"
            raise exception.ScenariesWebApiFilterError.AdaptionError(text_error)
        
    def animation(self, animation: bool) -> bool:
        """
        Анимации
        """
        
        if isinstance(animation, bool):
            return animation
        else:
            text_error = "invalid data type specified"
            raise exception.ScenariesWebApiFilterError.AnimationError(text_error)
        
    def price(self, price: int) -> int:
        """
        Цена
        """

        if isinstance(price, (int, float)):
            return price
        else:
            text_error = "invalid data type specified, must be (int, float)"
            raise exception.ScenariesWebApiFilterError.PriceError(text_error)
        
    def specialty(self, specialty: str) -> str:
        """
        Специальность
        """

        if len(specialty) <= 75:
            return specialty
        else:
            text_error = "the name of the specialty should not be more than (75) characters"
            raise exception.ScenariesWebApiFilterError.SpecialtyError(text_error)

    def full_name(self, full_name: str) -> str:
        """
        ФИО заказчика
        """

        full_name = full_name.split(" ")

        if len(full_name) == 3:
            for name in full_name:
                if not 2 <= len(name) <= 20:
                    text_error = ""
                    raise exception.ScenariesWebApiFilterError.FullNameError(text_error)
                return full_name
        else:
            text_error = "you must indicate your last name, first name and patronymic with spaces"
            raise exception.ScenariesWebApiFilterError.FullNameError(text_error)
        
    def teacher(self, teacher: str) -> str:
        """
        преподователя
        """

        if len(teacher) <= 200:
            return teacher
        else:
            text_error = "the teacher's name must not contain more than (200) characters"
            raise exception.ScenariesWebApiFilterError.TeacherError(text_error)

    def number_phone(self, number_phone: str) -> str:
        """
        Номер телефона
        """

        if not len(number_phone) > 1:
            text_error = f"the phone number must contain 10 or 11 numbers. You specified ({len(number_phone)})"
            raise exception.ScenariesWebApiFilterError.NumberPhoneError(text_error)
        
        new_phone_number = ""

        for number in number_phone:
            if number in "0123456789":
                new_phone_number += number

        if not 10 <= len(new_phone_number) <= 11:
            text_error = "the number of numbers in the number does not correspond to the acceptable range of 10 to 11"
            raise exception.ScenariesWebApiFilterError.NumberPhoneError(text_error)
        
        if len(new_phone_number) == 11:
            if not new_phone_number[0] == "7":
                text_error = f"the number type must be +7 and not ({new_phone_number[0]})"
                raise exception.ScenariesWebApiFilterError.NumberPhoneError(text_error)
            else:
                new_phone_number = new_phone_number[1:]

        return new_phone_number
    
    def user_name_tg(self, user_name_tg: str) -> str:
        """
        Тг имя пользователя (@test_name)
        """

        pattern = r"@([0-9A-Za-z-_]+$)"
        match = search(pattern=pattern, string=user_name_tg)
 
        if match:
            return match.group(1)
        else:
            match = fullmatch(pattern=r"([0-9A-Za-z-_]+$)", string=user_name_tg)
            if match:
                return match.group()
            else:
                text_error = "telegram account name is incorrect"
                raise exception.ScenariesWebApiFilterError.UserNameTgError(text_error)

    def mail(self, mail: str) -> str:
        """
        Почта пользователя
        """

        pattern = r"^([0-9A-Za-z-_%+.]{2,60}@[0-9A-Za-z-_.]{1,15}[0-9A-Za-z-_]{1,15}\.[A-Za-z-_]{2,15})$"
        match = search(pattern=pattern, string=mail)
        if match:
            return match.group(1)
        else:
            text_error = "incorrect email address"
            raise exception.ScenariesWebApiFilterError.MailError(text_error)

    def vk(self, vk: str) -> str:
        """
        Вк имя пользователя (@test_name)
        """

        pattern = r"@([0-9A-Za-z-_]+$)"
        match = search(pattern=pattern, string=vk)
 
        if match:
            return match.group(1)
        else:
            match = fullmatch(pattern=r"([0-9A-Za-z-_]+$)", string=vk)
            if match:
                return match.group()
            else:
                text_error = "VK account name is incorrect"
                raise exception.ScenariesWebApiFilterError.VkError(text_error)
