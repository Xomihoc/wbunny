'''
Данный файл является за исполнение различных сцеариев (работа (чтение, запись) с бд;

Дата создания: 04.09.2024; 
Дата изменния: -;
'''


from backend.scenaries.scenaries_web_api.scenaries_web_api import ScenariesWebApi


class Scenaries:
    """
    Главный файл 
    """

    web_api = ScenariesWebApi()