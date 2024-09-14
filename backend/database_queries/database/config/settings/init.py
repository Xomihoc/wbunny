from tortoise import Tortoise
from backend.database_queries.database.config.models import models


async def init():
    await Tortoise.init(
        config = {
            "connections": {
                "default": 'sqlite://backend/database_queries/database/data_storage_location/db.sqlite3',
            },
            "apps": {
                "models": {
                    'models': ['backend.database_queries.database.config.models.models'],
                    'default_connection': 'default',
                }
            },
        }
    )
    await Tortoise.generate_schemas()
