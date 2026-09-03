class MyContext:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, "r")
        return self.file

    def __exit__(self, exc_type, exc, tb):
        print(f"Exception type:{exc_type}")
        print(f"Exception: {exc}")
        print(f"Traceback: {tb}")
        self.file.close()
        return False


with MyContext("data/sample.log") as f:
    data = f.read()
    raise ValueError("Something went wrong")
