import logging
from typing import List
from ..models import Task

logger = logging.getLogger(__name__)

class GeneratorSource:
    """Генерирует задачи циклом."""
    def __init__(self, count: int = 3):
        self._count = count

    def get_tasks(self) -> List[Task]:
        logger.info(f"Генерация {self._count} задач")
        return [Task(id=f"gen-{i + 1}", payload={"step": i + 1, "status": "готово"}) for i in range(self._count)]
