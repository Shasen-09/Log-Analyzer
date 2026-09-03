from dataclasses import dataclass


@dataclass
class Log:
    date: str
    time: str
    level: str
    method: str
    path: str
    status: int
    response: int
