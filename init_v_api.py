'''
Данный файл отвечает за запуск api.
В файле init_v_api.py прописываются версии api. 
'''


from fastapi import FastAPI

from backend.controller.api.v_1 import main_api_v_1


app = FastAPI()
# Подулючаем существующие версии api 
app.include_router(router=main_api_v_1.router, prefix="/api/v_1.0")

