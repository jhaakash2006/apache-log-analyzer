from analyzer import LogAnalyzer


def test_total_requests():
    analyzer = LogAnalyzer()

    record = {
        "ip": "127.0.0.1",
        "timestamp": "17/Aug/2026:10:00:00 +0530",
        "method": "GET",
        "url": "/",
        "status": 200,
        "size": 1000,
        "referer": "-",
        "user_agent": "Mozilla/5.0"
    }

    analyzer.update(record)

    result = analyzer.results()

    assert result["total_requests"] == 1
    assert result["unique_ips"] == 1
    assert result["total_size"] == 1000


def test_status_code():
    analyzer = LogAnalyzer()

    record = {
        "ip": "127.0.0.1",
        "timestamp": "17/Aug/2026:10:00:00 +0530",
        "method": "GET",
        "url": "/test",
        "status": 404,
        "size": 500,
        "referer": "-",
        "user_agent": "Mozilla/5.0"
    }

    analyzer.update(record)

    result = analyzer.results()

    assert result["status_codes"][404] == 1
    assert result["4xx_errors"] == 1