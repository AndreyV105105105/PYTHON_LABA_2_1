import logging
from typing import List
from ..models import Task

logger = logging.getLogger(__name__)

class ApiSource:
    """Имитирует получение задач из внешнего API."""
    def get_tasks(self) -> List[Task]:
        logger.info("Запрос к API-заглушке")
        # Имитация успешного ответа
        return [
            Task(id="api-task-300", payload={"user_id": 105, "action": "сделан пост"}),
            Task(id="api-task-105", payload={"user_id": 300, "action": "поставлен лайк"})
        ]
