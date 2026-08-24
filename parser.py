import re


def parse_log_line(line):

    line = line.strip()

    start = line.find("[")

    if start == -1:
        return None

    first_part = line[:start].strip()

    ips = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", first_part)

    if not ips:
        return None

    ip = ips[0]

    rest = line[start:]

    pattern = r'^\[([^\]]+)\]\s+"([^"]*)"\s+(\d{3})\s+(\S+)\s+"([^"]*)"\s+"([^"]*)"$'

    match = re.match(pattern, rest)

    if not match:
        return None

    timestamp = match.group(1)
    request = match.group(2)
    status = int(match.group(3))
    size_text = match.group(4)
    referer = match.group(5)
    user_agent = match.group(6)

    if size_text == "-":
        size = 0
    else:
        try:
            size = int(size_text)
        except:
            size = 0

    parts = request.split()

    if len(parts) >= 2:
        method = parts[0]
        url = parts[1]
    else:
        method = "UNKNOWN"
        url = "-"

    return {
        "ip": ip,
        "timestamp": timestamp,
        "method": method,
        "url": url,
        "status": status,
        "size": size,
        "referer": referer,
        "user_agent": user_agent
    }