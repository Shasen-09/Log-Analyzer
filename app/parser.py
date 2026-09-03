from typing import Iterator
from app.models import Log
from .utils import timer


def parse_logs(logs: Iterator[str]) -> Iterator[Log]:

    for line in logs:
        line = line.strip()
        if not line:
            continue
        date, time, level, method, path, status, response = line.split()
        status = int(status)
        response = int(response)
        yield Log(
            date,
            time,
            level,
            method,
            path,
            status,
            response)
