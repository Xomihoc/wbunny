'''
Все исключения используемые в бэкенд части


Примечание: необходимо улучшить обращение к исключениям
'''


class DataNotTuple(Exception):
    """
    Не является кортежем
    """
    pass


class FilterError(Exception):
    """
    Фильтрации данных
    """
    pass


class ScenariesWebApiFilterError(Exception):
    """
    Срабатывает при анализе данных
    """

    class WorkOptionError(Exception):
        """
        Варианты работ (Курсовая, дипломная и т.д.)
        """
        pass

    class SoftwareCursError(Exception):
        """
        Выбор web или desktop
        """
        pass

    class TermsOfReferenceError(Exception):
        """
        Техническое задание к проекту
        """
        pass

    class EvaluationError(Exception):
        """
        Желаемая оценка
        """
        pass

    class AdaptionError(Exception):
        """
        Адаптив
        """
        pass

    class AnimationError(Exception):
        """
        Анимации
        """
        pass

    class PriceError(Exception):
        """
        Цена
        """
        pass

    class SpecialtyError(Exception):
        """
        Специальность
        """
        pass

    class FullNameError(Exception):
        """
        ФИО заказчика
        """
        pass

    class TeacherError(Exception):
        """
        Преподователь
        """
        pass

    class NumberPhoneError(Exception):
        """
        Номер телефона
        """
        pass

    class UserNameTgError(Exception):
        """
        ник телеграм
        """
        pass

    class MailError(Exception):
        """
        почта
        """
        pass

    class VkError(Exception):
        """
        има профиля вк
        """
        pass


class ArrayFormation(Exception):
    """
    Формирование корректного массива данных для обращения к БД
    """
    pass


class RecordDataBaseError(Exception):
    """
    Запись данных в БД
    """
    pass
