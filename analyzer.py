class LogAnalyzer:

    def __init__(self):
        self.total_requests = 0
        self.total_size = 0
        self.error_4xx = 0
        self.error_5xx = 0
        self.bots = 0

        self.unique_ips = set()
        self.ip_counts = {}
        self.url_counts = {}
        self.failed_by_ip = {}
        self.failed_logins = {}
        self.methods = {}
        self.status_codes = {}
        self.browsers = {}
        self.bot_types = {}
        self.hourly_requests = {}

        self.error_details = {}

    def update(self, record):

        self.total_requests += 1
        self.total_size += record["size"]

        ip = record["ip"]
        self.unique_ips.add(ip)

        self.ip_counts[ip] = self.ip_counts.get(ip, 0) + 1

        url = record["url"]
        self.url_counts[url] = self.url_counts.get(url, 0) + 1

        method = record["method"]
        self.methods[method] = self.methods.get(method, 0) + 1

        status = record["status"]
        self.status_codes[status] = self.status_codes.get(status, 0) + 1

        if 400 <= status <= 599:

            key = (ip, url, status)

            self.error_details[key] = (
                self.error_details.get(key, 0) + 1
            )

        if 400 <= status <= 499:

            self.error_4xx += 1
            self.failed_by_ip[ip] = self.failed_by_ip.get(ip, 0) + 1

        elif 500 <= status <= 599:

            self.error_5xx += 1

        if status == 401:

            self.failed_logins[ip] = self.failed_logins.get(ip, 0) + 1

        timestamp = record["timestamp"]
        hour = timestamp[12:14]

        self.hourly_requests[hour] = (
            self.hourly_requests.get(hour, 0) + 1
        )

        user_agent = record["user_agent"]

        if "Chrome" in user_agent:
            browser = "Chrome"

        elif "Firefox" in user_agent:
            browser = "Firefox"

        elif "Safari" in user_agent:
            browser = "Safari"

        else:
            browser = "Other"

        self.browsers[browser] = (
            self.browsers.get(browser, 0) + 1
        )

        user_agent_lower = user_agent.lower()

        bot_type = None

        if "googlebot" in user_agent_lower:
            bot_type = "Googlebot"

        elif "bingbot" in user_agent_lower:
            bot_type = "Bingbot"

        elif "facebookexternalhit" in user_agent_lower:
            bot_type = "Facebook"

        elif "curl" in user_agent_lower:
            bot_type = "curl"

        elif "wget" in user_agent_lower:
            bot_type = "wget"

        elif "python-requests" in user_agent_lower:
            bot_type = "Python Requests"

        elif "crawler" in user_agent_lower:
            bot_type = "Crawler"

        elif "spider" in user_agent_lower:
            bot_type = "Spider"

        elif "slurp" in user_agent_lower:
            bot_type = "Slurp"

        elif "bot" in user_agent_lower:
            bot_type = "Other Bot"

        if bot_type:

            self.bots += 1

            self.bot_types[bot_type] = (
                self.bot_types.get(bot_type, 0) + 1
            )

    def results(self):

        if self.total_requests:

            average_size = self.total_size / self.total_requests

        else:

            average_size = 0

        top_ips = sorted(
            self.ip_counts.items(),
            key=lambda item: item[1],
            reverse=True
        )[:10]

        top_urls = sorted(
            self.url_counts.items(),
            key=lambda item: item[1],
            reverse=True
        )[:20]

        suspicious_ips = []

        for ip, count in self.failed_by_ip.items():

            if count >= 3:

                suspicious_ips.append({
                    "ip": ip,
                    "4xx_count": count
                })

        risk_levels = []

        for ip, count in self.failed_logins.items():

            if count >= 20:

                risk = "HIGH"

            elif count >= 5:

                risk = "MEDIUM"

            else:

                risk = "LOW"

            risk_levels.append({
                "ip": ip,
                "failed_logins": count,
                "risk": risk
            })

        risk_summary = {
            "HIGH": 0,
            "MEDIUM": 0,
            "LOW": 0
        }

        for item in risk_levels:

            risk_summary[item["risk"]] += 1

        if risk_summary["HIGH"] > 0:

            overall_security = "HIGH"

        elif risk_summary["MEDIUM"] > 0:

            overall_security = "MEDIUM"

        else:

            overall_security = "LOW"

        suspicious_login_ips = []

        for ip, count in self.failed_logins.items():

            if count >= 5:

                suspicious_login_ips.append({
                    "ip": ip,
                    "failed_logins": count
                })

        if self.hourly_requests:

            busiest_hour = max(
                self.hourly_requests,
                key=self.hourly_requests.get
            )

            busiest_hour_requests = self.hourly_requests[busiest_hour]

        else:

            busiest_hour = None
            busiest_hour_requests = 0

        return {
            "total_requests": self.total_requests,
            "unique_ips": len(self.unique_ips),
            "methods": self.methods,
            "status_codes": self.status_codes,
            "top_ips": top_ips,
            "top_urls": top_urls,
            "total_size": self.total_size,
            "average_size": average_size,
            "4xx_errors": self.error_4xx,
            "5xx_errors": self.error_5xx,
            "suspicious_ips": suspicious_ips,
            "failed_logins": self.failed_logins,
            "suspicious_login_ips": suspicious_login_ips,
            "risk_levels": risk_levels,
            "risk_summary": risk_summary,
            "overall_security": overall_security,
            "browsers": self.browsers,
            "bots": self.bots,
            "bot_types": self.bot_types,
            "hourly_requests": self.hourly_requests,
            "busiest_hour": busiest_hour,
            "busiest_hour_requests": busiest_hour_requests,
            "error_details": self.error_details
        }