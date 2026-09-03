from typing import Iterator


def read_logs(filename: str) -> Iterator[str]:
    with open(filename, "r") as f:
        for line in f:
            yield line
