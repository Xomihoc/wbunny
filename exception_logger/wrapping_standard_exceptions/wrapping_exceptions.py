"""
Оберточные исключения
"""


from time import strftime

from exception_logger.record.writing_data_to_file import Record


class WrappingLevel:

    def __init__(self,
                directory,
                logger_file_name,
                ):
        self.__directory = directory
        self.__logger_file_name = logger_file_name

    def __call__(self, 
                module,
                data,
                error_type,
                ):

        def decorator(func):
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except Exception as error:
                    time = strftime("%m.%d.%y - %H:%M:%S")
                    
                    record = Record(
                        error_type=error_type,
                        module=module,
                        error=error,
                        data=data,
                        time=time,
                        directory=self.__directory,
                        logger_file_name=self.__logger_file_name,
                    )

                    record()

                return None
            return wrapper
        return decorator
