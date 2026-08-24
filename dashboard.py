import streamlit as st
from parser import parse_log_line
from analyzer import LogAnalyzer


st.set_page_config(
    page_title="Apache Log Analyzer",
    page_icon="🔎",
    layout="wide"
)


def read_log(uploaded_file):

    analyzer = LogAnalyzer()

    data = uploaded_file.getvalue().decode(
        "utf-8",
        errors="ignore"
    )

    for line in data.splitlines():

        record = parse_log_line(line)

        if record:
            analyzer.update(record)

    return analyzer.results()


st.title("Apache Log Analyzer")
st.write("Analyze Apache access logs and check server activity.")


uploaded_file = st.file_uploader(
    "Select access.log",
    type=["log", "txt"]
)


if uploaded_file is not None:

    result = read_log(uploaded_file)

    st.success("Analysis completed")


    st.subheader("Summary")

    a, b, c, d = st.columns(4)

    a.metric(
        "Requests",
        result["total_requests"]
    )

    b.metric(
        "Unique IPs",
        result["unique_ips"]
    )

    c.metric(
        "4xx Errors",
        result["4xx_errors"]
    )

    d.metric(
        "5xx Errors",
        result["5xx_errors"]
    )


    st.subheader("Request Methods")

    st.bar_chart(
        result["methods"]
    )


    st.subheader("Status Codes")

    status_data = {}

    for status, count in result["status_codes"].items():

        status_data[str(status)] = count

    st.bar_chart(
        status_data
    )


    st.subheader("Hourly Requests")

    st.line_chart(
        result["hourly_requests"]
    )


    st.subheader("Most Active IPs")

    ip_data = {}

    for ip, count in result["top_ips"]:

        ip_data[ip] = count

    st.bar_chart(
        ip_data
    )


    st.subheader("Popular URLs")

    for url, count in result["top_urls"]:

        st.write(
            str(count) + "  " + url
        )


    st.subheader("Browsers")

    st.bar_chart(
        result["browsers"]
    )


    st.subheader("Bot Activity")

    st.write(
        "Total Bots:",
        result["bots"]
    )

    if result["bot_types"]:

        for bot, count in result["bot_types"].items():

            st.write(
                bot,
                count
            )


    st.subheader("Security")

    security = result["overall_security"]

    if security == "HIGH":

        st.error(
            "Overall Security: HIGH"
        )

    elif security == "MEDIUM":

        st.warning(
            "Overall Security: MEDIUM"
        )

    else:

        st.success(
            "Overall Security: LOW"
        )


    a, b, c = st.columns(3)

    a.metric(
        "High Risk",
        result["risk_summary"]["HIGH"]
    )

    b.metric(
        "Medium Risk",
        result["risk_summary"]["MEDIUM"]
    )

    c.metric(
        "Low Risk",
        result["risk_summary"]["LOW"]
    )


    st.subheader("Suspicious Login Activity")

    if result["suspicious_login_ips"]:

        for item in result["suspicious_login_ips"]:

            st.warning(
                item["ip"]
                + "  |  Failed Logins: "
                + str(item["failed_logins"])
            )

    else:

        st.success(
            "No suspicious login activity found."
        )


    st.subheader("Risk Details")

    for item in result["risk_levels"]:

        st.write(
            item["ip"]
            + "  |  "
            + str(item["failed_logins"])
            + " failed logins  |  "
            + item["risk"]
        )


    st.subheader("Response Size")

    a, b, c = st.columns(3)

    a.metric(
        "Total Size",
        str(result["total_size"]) + " bytes"
    )

    b.metric(
        "Average Size",
        str(round(result["average_size"], 2)) + " bytes"
    )

    c.metric(
        "Busiest Hour",
        result["busiest_hour"] + ":00"
    )


    st.subheader("Download Report")

    report = []

    report.append("APACHE LOG ANALYZER")
    report.append("")
    report.append(
        "Total Requests: "
        + str(result["total_requests"])
    )
    report.append(
        "Unique IPs: "
        + str(result["unique_ips"])
    )
    report.append(
        "4xx Errors: "
        + str(result["4xx_errors"])
    )
    report.append(
        "5xx Errors: "
        + str(result["5xx_errors"])
    )
    report.append(
        "Total Bots: "
        + str(result["bots"])
    )
    report.append(
        "Overall Security: "
        + result["overall_security"]
    )
    report.append(
        "Busiest Hour: "
        + result["busiest_hour"]
        + ":00"
    )

    report_data = "\n".join(report)

    st.download_button(
        "Download Report",
        report_data,
        "apache_report.txt",
        "text/plain"
    )


else:

    st.info(
        "Upload an Apache access.log file to begin."
    )