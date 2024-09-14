from backend.scenaries.scenaries_web_api.scenaries_web_api import ScenariesWebApi
from pprint import pprint
import asyncio


async def main():
    scenaries_web_api = ScenariesWebApi()


    data = {
        "work_option": "курсовая",
        "software_curs": "web",
        "terms_of_reference": "В данном сообщении описан текст данном сообщении описан текст данном сообщении описан текст данном сообщении описан текст ",
        "evaluation": 4,
        "adaption": False,
        "animation": False,
        "price": 1250,
        "specialty": "ХЗ какая-то специальность",
        "full_name": "Медведев Артем Евгеньевич",
        "teacher": "Преподователь",
        "number_phone": "+7 999 342-33-32",
        "user_name_tg": "@Artem_test",
        "mail": "test_mail@test.test",
        "vk": "@Test_name",
    }

    print(await scenaries_web_api(data=data))


asyncio.run(main())
