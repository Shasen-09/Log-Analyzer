from .utils import timer
from typing import Iterator
from .models import Log
from collections import defaultdict
from collections.abc import Iterable


@timer
def analyze(logs: Iterable[Log]) -> dict[str, object]:
    status_counts = defaultdict(int)
    level_counts = defaultdict(int)
    total = 0
    total_response_time = 0
    max_response_time = 0
    for log in logs:
        total += 1
        level_counts[log.level] += 1
        status_counts[log.status] += 1

        total_response_time += log.response
        max_response_time = max(max_response_time, log.response)

    average_response_time = total_response_time / total if total else 0

    data = {
        "total": total,
        "level": dict(level_counts),
        "status": dict(status_counts),
        "average_response_time": average_response_time,
        "max_response_time": max_response_time}

    return data


def level_logs(logs: Iterable[Log], level: str) -> Iterator[Log]:
    for log in logs:
        if log.level == level:
            yield log


def status_logs(logs: Iterable[Log], status: int) -> Iterator[Log]:
    for log in logs:
        if log.status == status:
            yield log
