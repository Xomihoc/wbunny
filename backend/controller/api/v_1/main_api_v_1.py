'''
Версия api 1.0;

В данном файле указываются все роутеры, существующие в данной версии api;
Дата создания: 29.08.2024;
Дата создания: -;
'''


from fastapi import APIRouter

from backend.controller.api.v_1.handlers.creating_application import handler_creating_application


router = APIRouter()

router.include_router(
    router=handler_creating_application.router,
    prefix="/creating_application",
    )
