from pathlib import Path

filename = Path("data/sample.log")


class FileIterator:
    def __init__(self, filename):
        self.file = open(filename, "r")

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()

        if line == "":
            self.file.close()
            raise StopIteration

        return line


logs = FileIterator(filename)

print(next(logs))
print(next(logs))
print(next(logs))
print(next(logs))
print(next(logs))
