import sys
import json

from parser import parse_log_line
from analyzer import LogAnalyzer


if len(sys.argv) < 2:
    print("Usage: python main.py <logfile>")
    sys.exit(1)


filename = sys.argv[1]

analyzer = LogAnalyzer()


with open(filename, "r", encoding="utf-8") as file:

    for line in file:

        record = parse_log_line(line)

        if record:
            analyzer.update(record)


result = analyzer.results()


print()
print("========================================")
print("          APACHE LOG ANALYZER")
print("========================================")

print()
print("----------- BASIC SUMMARY --------------")
print(f"Total Requests       : {result['total_requests']}")
print(f"Unique IPs           : {result['unique_ips']}")
print(f"Total Size           : {result['total_size']} bytes")
print(f"Average Response     : {result['average_size']:.2f} bytes")


print()
print("----------- HTTP METHODS ---------------")

for method, count in result["methods"].items():
    print(f"{method:<20}: {count}")


print()
print("----------- STATUS CODES ---------------")

for status, count in result["status_codes"].items():
    print(f"{status:<20}: {count}")


print()
print("----------- ERRORS --------------------")
print(f"4xx Errors           : {result['4xx_errors']}")
print(f"5xx Errors           : {result['5xx_errors']}")


print()
print("----------- SECURITY ------------------")

print(f"Overall Security     : {result['overall_security']}")
print(f"HIGH Risk IPs        : {result['risk_summary']['HIGH']}")
print(f"MEDIUM Risk IPs      : {result['risk_summary']['MEDIUM']}")
print(f"LOW Risk IPs         : {result['risk_summary']['LOW']}")

print()
print(f"Failed Login Attempts: {sum(result['failed_logins'].values())}")

print()
print("Suspicious Login IPs:")

for item in result["suspicious_login_ips"]:
    print(
        f"IP: {item['ip']} | "
        f"Failed Logins: {item['failed_logins']}"
    )


print()
print("----------- TOP IPs -------------------")

for ip, count in result["top_ips"]:
    print(f"{ip:<20}: {count}")


print()
print("----------- TOP URLs ------------------")

for url, count in result["top_urls"]:
    print(f"{count:<8} {url}")


print()
print("----------- BROWSERS -----------------")

for browser, count in result["browsers"].items():
    print(f"{browser:<20}: {count}")


print()
print("----------- BOTS ----------------------")

print(f"Total Bots           : {result['bots']}")

for bot, count in result["bot_types"].items():
    print(f"{bot:<20}: {count}")


print()
print("----------- HOURLY TRAFFIC ------------")

for hour, count in sorted(result["hourly_requests"].items()):
    print(f"{hour}:00              : {count}")


print()
print("----------- BUSIEST HOUR --------------")

print(f"Busiest Hour         : {result['busiest_hour']}:00")
print(f"Requests             : {result['busiest_hour_requests']}")


print()
print("========================================")
print("             ANALYSIS DONE")
print("========================================")


with open("report.txt", "w", encoding="utf-8") as report:

    report.write("========================================\n")
    report.write("          APACHE LOG ANALYZER\n")
    report.write("========================================\n\n")

    report.write("----------- BASIC SUMMARY --------------\n")
    report.write(f"Total Requests       : {result['total_requests']}\n")
    report.write(f"Unique IPs           : {result['unique_ips']}\n")
    report.write(f"Total Size           : {result['total_size']} bytes\n")
    report.write(
        f"Average Response     : "
        f"{result['average_size']:.2f} bytes\n"
    )

    report.write("\n----------- HTTP METHODS ---------------\n")

    for method, count in result["methods"].items():
        report.write(f"{method:<20}: {count}\n")

    report.write("\n----------- STATUS CODES ---------------\n")

    for status, count in result["status_codes"].items():
        report.write(f"{status:<20}: {count}\n")

    report.write("\n----------- ERRORS --------------------\n")
    report.write(f"4xx Errors           : {result['4xx_errors']}\n")
    report.write(f"5xx Errors           : {result['5xx_errors']}\n")

    report.write("\n----------- SECURITY ------------------\n")
    report.write(
        f"Overall Security     : "
        f"{result['overall_security']}\n"
    )

    report.write(
        f"HIGH Risk IPs        : "
        f"{result['risk_summary']['HIGH']}\n"
    )

    report.write(
        f"MEDIUM Risk IPs      : "
        f"{result['risk_summary']['MEDIUM']}\n"
    )

    report.write(
        f"LOW Risk IPs         : "
        f"{result['risk_summary']['LOW']}\n"
    )

    report.write(
        f"\nFailed Login Attempts: "
        f"{sum(result['failed_logins'].values())}\n"
    )

    report.write("\nSuspicious Login IPs:\n")

    for item in result["suspicious_login_ips"]:
        report.write(
            f"IP: {item['ip']} | "
            f"Failed Logins: {item['failed_logins']}\n"
        )

    report.write("\n----------- TOP IPs -------------------\n")

    for ip, count in result["top_ips"]:
        report.write(f"{ip:<20}: {count}\n")

    report.write("\n----------- TOP URLs ------------------\n")

    for url, count in result["top_urls"]:
        report.write(f"{count:<8} {url}\n")

    report.write("\n----------- BROWSERS -----------------\n")

    for browser, count in result["browsers"].items():
        report.write(f"{browser:<20}: {count}\n")

    report.write("\n----------- BOTS ----------------------\n")

    report.write(f"Total Bots           : {result['bots']}\n")

    for bot, count in result["bot_types"].items():
        report.write(f"{bot:<20}: {count}\n")

    report.write("\n----------- HOURLY TRAFFIC ------------\n")

    for hour, count in sorted(result["hourly_requests"].items()):
        report.write(f"{hour}:00              : {count}\n")

    report.write("\n----------- BUSIEST HOUR --------------\n")

    report.write(
        f"Busiest Hour         : "
        f"{result['busiest_hour']}:00\n"
    )

    report.write(
        f"Requests             : "
        f"{result['busiest_hour_requests']}\n"
    )

    report.write("\n========================================\n")
    report.write("             ANALYSIS DONE\n")
    report.write("========================================\n")


json_result = result.copy()

if "error_details" in json_result:

    json_error_details = {}

    for key, count in json_result["error_details"].items():

        if isinstance(key, tuple):
            new_key = " | ".join(str(value) for value in key)
        else:
            new_key = str(key)

        json_error_details[new_key] = count

    json_result["error_details"] = json_error_details


with open("report.json", "w", encoding="utf-8") as file:
    json.dump(json_result, file, indent=4)


print()
print("Report saved to: report.txt")
print("JSON report saved to: report.json")  