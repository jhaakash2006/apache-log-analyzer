from parser import parse_log_line


def test_valid_log_line():
    line = '125.20.113.50 - - [17/Aug/2026:06:25:06 +0530] "GET / HTTP/1.1" 200 5798 "-" "Mozilla/5.0"'

    result = parse_log_line(line)

    assert result is not None
    assert result["ip"] == "125.20.113.50"
    assert result["method"] == "GET"
    assert result["url"] == "/"
    assert result["status"] == 200
    assert result["size"] == 5798


def test_failed_request_line():
    line = '125.20.113.50 - - [17/Aug/2026:06:25:26 +0530] "-" 408 5205 "-" "-"'

    result = parse_log_line(line)

    assert result is not None
    assert result["status"] == 408
    assert result["method"] == "UNKNOWN"


def test_bad_line():
    line = "this is not a valid apache log line"

    result = parse_log_line(line)

    assert result is None