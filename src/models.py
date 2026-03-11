from dataclasses import dataclass

# базовая таска, красивая
@dataclass
class Task:
    id: str
    payload: dict
