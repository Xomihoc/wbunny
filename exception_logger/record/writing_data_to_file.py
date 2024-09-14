"""
Система записи данных в бд

Примечание для разработчика:

    1. Необходимо прописать метод для исправления данных - 
        (self.__directory = self.__directory + ".txt");
    2. Необходимо что-то придумать с системой реагирования;
"""


import os


class Record:
    def __directory_correction(self,
                               directory,
                               logger_file_name,
                               ):
        if not directory.endswith(logger_file_name):
            return os.path.join(directory, logger_file_name)
        else:
            return directory
        
    def __detect_file_name(self, file_name):
        if not file_name:
            return "data_logger.txt"
        if not os.path.splitext(file_name)[-1]:
            return f"{file_name}.txt"

        return file_name

    def __init__(self,
                error_type,
                module,
                error,
                time,
                directory,
                logger_file_name,
                data=None,
                ):
        """
        :error_type: - уровень ошибки (1,2,3 - описанны в главном файле 
            (\exception_logger\main_exception_logger.py));
        :module: - место ошибки (модуль);
        :data=None: - набор данных;
        :error: - полученная ошибка;
        :time: - время;
        :directory: - дирректория сохранения данных;
        """

        self.__error_type = error_type
        self.__module = module
        self.__data = data
        self.__error = error
        self.__time = time
        self.__logger_file_name = self.__detect_file_name(logger_file_name)
        self.__directory = self.__directory_correction(
            directory=directory,
            logger_file_name=self.__logger_file_name,
            ) # ИСПРАВИТЬ (1)
    
    def __string_formation(self):
        data = str({
            "error_type": str(self.__error_type),
            "module": str(self.__module),
            "error": str(self.__error),
            "time": str(self.__time),
            "data": str(self.__data),
            "directory": str(self.__directory),
        }) + "\n"
        return data

    def __module_record(self):
        """
        запись массива данных в файл 
        """

        data = self.__string_formation()

        # try:
        with open(file=self.__directory, mode="a") as file:
            file.write(data)

        # except Exception:
        #     pass # ИСПРАВИТЬ (2)
        
    def __call__(self):
        self.__module_record()
 