# from tortoise import run_async
# from database_queries.database.config.models.models import Users, Orders, Message
# from database_queries.database.config.settings.init import init
# from pprint import pprint


# run_async(init())

# async def main():
#     # Or by .create()

#     user_data = {
#         "user_id_tg":"23354592484",
#         "user_name_tg":"Sasa",
#         "registered":False,
#         "account_status":False,
#         "role":"User",
#         "admin_role":True,
#         "first_name":"Name",
#         "last_name":"Last",
#         "patronymic":"noeirb",
#         "phone_number":"9293069927",
#         "name_educational_institution":"KKRIT",
#         "record_book":"0369",
#         "vk":"Artem",
#         "speciality":"9IS-1.21",
#         "mail":"medmap@test.com",
#     }

#     copywriter = await Users.filter(user_id_tg="21354572484").first() # Замените на нужный user_id_tg
#     programmer = await Users.filter(user_id_tg="23354592484").first()
#     orders_data = {
#         "status": "Начат",
#         "work_option": "Курсовая",
#         "scope_of_work": "полная",
#         "terms_of_reference": "Тут расположиться текст" * 5,
#         "submission_deadline": "14.05.25-14:00:00",
#         "course_project_topic": "Хз",
#         "teacher": "Татарникова",
#         "copywriter_id":copywriter,
#         "programmer_id":programmer,
#         "grade": "5",
#         "programmer_job_status": "В процессе",
#         "copywriter_job_status": "В процессе",
#         "software_curs": "веб",
#         "adaption": True,
#         "animation": True,
#         "price": 5590,
#     }



#     # pprint(user_data)

#     # await Users.create(**user_data)

#     await Orders.create(**orders_data)
#     # await user.order.add(*order)
#     # prin = await Users.filter(phone_number="9293069927")
#     # # prin = await Users.first(user_id=1)
#     # print(type(prin))
#     # print(prin)
#     # for i in prin:
#     #     print(i.admin_role)
    






# run_async(main())
