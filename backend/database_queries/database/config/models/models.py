'''
В данном файле хроняться модели (таблицы) базы данных
_____________________________________________________
Дата: 24.08.2024
Дата изменения: 26.08.2024
'''


from tortoise.models import Model
from tortoise import fields


class Users(Model):
    """
    Таблица для хронения данных на пользователей.
    ____________________________________________
    """
    user_id = fields.IntField(primary_key=True) # id записи
    user_id_tg = fields.CharField(null=True, max_length=30) # tg_id
    user_name_tg = fields.CharField(null=True, max_length=32) # tg_name - (@test_name)
    registered = fields.BooleanField(null=True) # зарегистрирован или нет
    account_status = fields.BooleanField(null=True) # Заблокирован или нет
    role = fields.CharField(max_length=25) # роль – (Пользователь, программист, копирайтер, все)
    admin_role = fields.BooleanField(null=True) # роль администратора
    time_last_visit = fields.DatetimeField(null=True, auto_now=True) # время последнего посещения
    registration_datetime = fields.DatetimeField(null=True, auto_now_add=True) # дата и время регистрации
    first_name = fields.CharField(null=True, max_length=30) # имя
    last_name = fields.CharField(null=True, max_length=50) # фамилия
    patronymic = fields.CharField(null=True, max_length=30) # отчестов
    phone_number = fields.CharField(null=True, max_length=10) # номер телефона
    name_educational_institution = fields.CharField(null=True, max_length=200) # название учебного заведения
    record_book = fields.CharField(null=True, max_length=15) # номер зачетной книжки
    vk = fields.CharField(null=True, max_length=100) # вк
    specialty = fields.CharField(null=True, max_length=75) # специальность
    mail = fields.CharField(null=True, max_length=300) # почта


class Orders(Model):
    """
    Таблица для хранения данных о заказах.
    ____________________________________________
    """
    order_id = fields.IntField(primary_key=True) # id заказа
    status = fields.CharField(max_length=40) # статус (размещен)
    work_option = fields.CharField(max_length=20) # вариант работы (курсова, диплом и т.д.)
    scope_of_work = fields.CharField(max_length=25) # объем работы
    terms_of_reference = fields.CharField(max_length=2000) # техническое задание
    submission_deadline = fields.CharField(null=True, max_length=30) # срок сдачи работы
    customer_id = fields.ForeignKeyField(null=True, model_name="models.Users", related_name="customer_id") # заказчик id
    copywriter_id = fields.ForeignKeyField(null=True, model_name="models.Users", related_name="copywriter_id") # копирайтер id
    programmer_id = fields.ForeignKeyField(null=True, model_name="models.Users", related_name="programmer_id") # программист id
    course_project_topic = fields.CharField(null=True, max_length=125) # тема курсового проекта
    teacher = fields.CharField(null=True, max_length=200) # преподователь
    evaluation = fields.CharField(max_length=1) # оценка
    customer_status = fields.CharField(null=True, max_length=25) # подключение к чату, заказчик
    copywriter_status = fields.CharField(null=True, max_length=25) # подключение к чату, копирайтер
    programmer_status = fields.CharField(null=True, max_length=25) # подключение к чату, программист
    programmer_job_status = fields.CharField(null=True, max_length=25) # работа программиста статус
    copywriter_job_status = fields.CharField(null=True, max_length=25) # работа копирайтера статус
    software_curs = fields.CharField(null=True, max_length=25) # web or desktop program
    adaption = fields.BooleanField() # адаптив сайта делать или нет
    animation = fields.BooleanField() # объем анимаций бльше меньше
    price = fields.IntField() # стоимость работы
    time_order = fields.DatetimeField(auto_now_add=True) # время размещения заказа


class Message(Model):
    """
    Таблица для хранения сообщений и данных о них.
    ______________________________________________
    """
    message_id = fields.IntField(primary_key=True)
    message_text = fields.TextField(null=True)
    user = fields.ForeignKeyField(model_name="models.Users", related_name="user")
    departure_date = fields.DatetimeField(auto_now_add=True)
    message_type = fields.CharField(max_length=25)
    status = fields.CharField(max_length=25)
