class DataNotDict(Exception):
    pass


class ForeignKeyFieldError(Exception):
    pass


class DataNotTuple(Exception):
    pass


class ColumnNameNotFound(Exception):
    pass


class DictionaryKeyException(Exception):
    pass


class MeaningTestError(Exception):
    """
    Данное исключение исполняется в случае если одно из условий метода 
    (meaning_test) небыло выполнено 
    """

    class NullError(Exception):
        """
        Пустая строка
        """
        pass

    class MinLengthError(Exception):
        """
        Несоответствие нижнего порога
        """
        pass

    class MaxLengthError(Exception):
        """
        Несоответствие верхнего порога
        """
        pass

    class DataTypeError(Exception):
        """
        Неверный тип данных
        """
        pass

    class ValueMatchingError(Exception):
        """
        Несоответствие значения
        """
        pass


class ParsingCleaningStringError(Exception):
    """
    Обработка входных данных
    """

    class PhoneNumber(Exception):
        """
        Обработка номера телефона 
        """
        pass

    class MailError(Exception):
        """
        Обработка почты
        """
        pass

    class SocialNetworkNames(Exception):
        """
        Обработка имен из соц-сетей
        """
        pass


class ConverterError(Exception):
    """
    Вызывается при негативной распределении данных в словарь    
    """
    pass