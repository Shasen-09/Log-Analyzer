from pathlib import Path

file = Path("data/sample.log")
info = 0
error = 0
warning = 0
request = 0

status200 = 0
status500 = 0
status429 = 0

totalresponsetime = 0


with file.open("r") as f:
    for line in f:
        parts = line.strip().split()
        request += 1

        level = parts[2]
        status = int(parts[5])
        response_time = int(parts[-1])
        totalresponsetime += response_time

        if level == "INFO":
            info += 1
        elif level == "ERROR":
            error += 1
        elif level == "WARNING":
            warning += 1
        if status == 200:
            status200 += 1
        elif status == 500:
            status500 += 1
        elif status == 429:
            status429 += 1

avgResponseTime = totalresponsetime / request

print(f"Number of log requests: {request}")
print(f"INFO: {info}")
print(f"ERROR: {error}")
print(f"WARNING: {warning}")

print(f"200: {status200}")
print(f"500: {status500}")
print(f"429: {status429}")

print(f"Average response time: {avgResponseTime}ms")
