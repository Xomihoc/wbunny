'''
Данные допустимые для принятия
'''


from pydantic import BaseModel


class VerificationApplications(BaseModel):
        work_option: str # вариант работы (курсова, дипломная, практическая и т.д.)
        software_curs: str # # web или desktop программа
        terms_of_reference: str # техническое задание к проекту
        evaluation: int # оценка
        adaption: bool # адаптив сайта
        animation: bool # анимации сайта
        price: int # цена
        specialty: str # специальность
        full_name: str # ФИО
        teacher: str # преподователь
        number_phone: str # номер телефона
        user_name_tg: str # ник телеграм
        mail: str # почта
        vk: str # ник вк
