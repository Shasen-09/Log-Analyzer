from contextlib import contextmanager


@contextmanager
def open_log(filename):
    file = open(filename, "r")
    try:
        yield file
    finally:
        file.close()


with open_log("data/sample.log") as f:
    print(f.readline())
    raise ValueError("Test error")
