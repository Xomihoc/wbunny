"""
 Версия: 1.0
 Дата создания: 14.08.2024
 Дата последнего изменения: - 
________________________________________________________________________________
Описание: Данный модуль отвечает за логирование всех ошибок при работе системы;
________________________________________________________________________________
Уровни логирования:
 - 1 - (FirstLevel) - Первый уровень и наименее важные исключения 
    (не вредять системе);
 - 2 - (SecondLevel) - Второй уровень ошибки среднего уровня 
    (они способны перерости в ошибки третьего уроня, за ними следует наблюдать);
 - 3 - (ThirdLevel) - Третий уровень ошибки способные навредить системе;
________________________________________________________________________________

Примечание: 
 - 1. Я думаю стоит исправить путь сохранения логов -> (Logger -> __file_path);
________________________________________________________________________________
 Идеи:
 - 1. Микро настройки которые прописываются в файле и из него система берет 
    все данные для работы;
 - 2. Анализ уровней ошибок;
________________________________________________________________________________
"""


import os

# from exceptions.exceptions import NotDirectory
# from wrapping_standard_exceptions.wrapping_exceptions import WrappingLevel
from exception_logger.wrapping_standard_exceptions.wrapping_exceptions import WrappingLevel
from exception_logger.wrapping_standard_exceptions.standard_exceptions import StandardLevel
# from wrapping_standard_exceptions.standard_exceptions import StandardLevel


class Logger:

    def __file_path(self):
        file_path = os.path.abspath(__file__)
        directory = os.path.dirname(file_path)
        return directory

    def __directory_analysis(self, directory):
        if not directory:
            return self.__file_path()
        if not os.path.isdir(directory):
            # raise NotDirectory("Дирректория не найдена")
            raise TypeError("errrrKsdnfkSDN")
        return directory

    def __init__(self, 
                logger_file_name=None,
                directory=None,
                ):
        """
        Если directory=None, то по умолчанию ставиться путь исполнения ->
         -> данного файла;
        """

        self.__directory = self.__directory_analysis(directory=directory)
        self.__logger_file_name = logger_file_name
        
        # уровни ошибок
        self.wrapping_level = WrappingLevel(
            directory=self.__directory,
            logger_file_name=self.__logger_file_name,
            )
        self.standard_level = StandardLevel(
            directory=self.__directory,
            logger_file_name=self.__logger_file_name,
            )
