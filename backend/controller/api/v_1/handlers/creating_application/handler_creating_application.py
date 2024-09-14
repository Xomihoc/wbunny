'''
В данном роутере описанны все обработчики, доступные в версии api 1.0

Дата создания: 29.08.2024;
Дата изменения: 04.09.2024;
'''


from fastapi import APIRouter, HTTPException, Request

from backend.scenaries.scenaries import Scenaries
from backend.controller.api.v_1.data_verification.verification_applications import VerificationApplications


router = APIRouter()


@router.post("/")
async def reade_root(data: VerificationApplications, requests: Request):
    """
    Принимает аргументы и выполняет запись в базу данных.
    """
    
    try:
        scenaries = Scenaries()
        otvet = str(await scenaries.web_api(data=data))

        # Проверка значения
        return {"response": otvet}
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="error processing the request",
        )
