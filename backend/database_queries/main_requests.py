'''
Данный модуль отвечает за чтение и запись данных в бд;
Дата создания: 28.08.2024;
Дата изменения: 12.09.2024;
'''


from backend.database_queries.database.config.settings.init import init
from backend.database_queries.requests.reading.reading import ReadingTable
from backend.database_queries.requests.reading.record import CreateDataTable, RewriteDataTable


class Requests(CreateDataTable, RewriteDataTable, ReadingTable):
    pass
