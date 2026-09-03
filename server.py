from app.reader import read_logs
from app.parser import parse_logs
from app.analyzer import analyze


log = read_logs("./data/sample.log")
logs = list(parse_logs(log))
result = analyze(logs)


print(f"Total logs: {result["total"]}\n")
for data, value in result["level"].items():
    print(f"{data} : {value}")
print("")
for status, count in result["status"].items():
    print(f"Status-{status} : {count}")

print(
    f"\nAverage Response: {result["average_response_time"]:.2f} milliseconds")
print(f"Max Response Time: {result["max_response_time"]:.2f} milliseconds")
