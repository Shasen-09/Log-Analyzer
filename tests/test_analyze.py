from app.models import Log
from app.analyzer import analyze, level_logs, status_logs
from app.reader import read_logs
from app.parser import parse_logs


def test_analyze():
    logs = iter([

        Log("2026-01-01", "10:00:00", "INFO", "GET", "/", 200, 100),
        Log("2026-01-01", "10:01:00", "ERROR", "/POST", "/login", 500, 300),
        Log("2026-01-01", "10:02:00", "WARNING", "GET", "/api", 429, 200),

    ])

    result = analyze(logs)

    assert result["total"] == 3
    assert result["level"]["INFO"] == 1
    assert result["level"]["ERROR"] == 1
    assert result["level"]["WARNING"] == 1
    assert result["status"][200] == 1
    assert result["status"][429] == 1
    assert result["status"][500] == 1
    assert result["average_response_time"] == 200
    assert result["max_response_time"] == 300


def test_level_logs():
    logs = iter([

        Log("2026-01-01", "10:00:00", "INFO", "GET", "/", 200, 100),
        Log("2026-01-01", "10:01:00", "ERROR", "/POST", "/login", 500, 300),
        Log("2026-01-01", "10:02:00", "INFO", "GET", "/api", 429, 200),

    ])

    result = list(level_logs(logs, "INFO"))

    assert len(result) == 2
    assert all(log.level == "INFO" for log in result)


def test_reader_logs():
    result = list(read_logs("data/sample.log"))

    assert len(result) == 10000
    assert isinstance(result[0], str)


def test_parser_logs():
    logs = read_logs("data/sample.log")
    result = list(parse_logs(logs))

    assert len(result) == 9999
    assert isinstance(result[0], Log)
    assert isinstance(result[0].status, int)
    assert isinstance(result[0].response, int)


def test_status_filter():
    logs = iter([

        Log("2026-01-01", "10:00:00", "INFO", "GET", "/", 200, 100),
        Log("2026-01-01", "10:01:00", "ERROR", "/POST", "/login", 500, 300),
        Log("2026-01-01", "10:02:00", "INFO", "GET", "/api", 429, 200),

    ])

    result = list(status_logs(logs, 200))

    assert len(result) == 1
