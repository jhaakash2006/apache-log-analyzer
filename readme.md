# Apache Log Analyzer

Apache Log Analyzer is a Python-based project that reads Apache web server access logs and analyzes website traffic, HTTP errors, client information, and basic security activity.

The project can process thousands of log requests and generate useful statistics in the terminal, a text report, a JSON report, and an interactive Streamlit dashboard.

**GitHub Repository:** https://github.com/jhaakash2006/apache-log-analyzer

---

## Table of Contents

- [Project Overview](#project-overview)
- [Project Objectives](#project-objectives)
- [Project Workflow](#project-workflow)
- [Features](#features)
- [Project Files](#project-files)
- [Requirements](#requirements)
- [Installation and Setup](#installation-and-setup)
- [How to Run the Project](#how-to-run-the-project)
- [Generated Reports](#generated-reports)
- [Current Analysis Results](#current-analysis-results)
- [Security Analysis](#security-analysis)
- [Testing](#testing)
- [Technologies Used](#technologies-used)
- [Python Concepts Used](#python-concepts-used)
- [Git and GitHub](#git-and-github)
- [Project Structure](#project-structure)
- [Project Output](#project-output)
- [Limitations and Future Scope](#limitations-and-future-scope)
- [Conclusion](#conclusion)
- [Author](#author)

---

## Project Overview

Apache Log Analyzer processes an Apache access log file line by line.

Each log entry is parsed and converted into structured information that can be analyzed to understand website traffic, identify HTTP errors, examine client activity, and detect basic security-related patterns.

The parser extracts the following information from each log entry:

- IP address
- Timestamp
- HTTP method
- Requested URL
- HTTP status code
- Response size
- Referer
- User-Agent

The parsed records are passed to the analyzer, which calculates statistics and prepares the final results.

The project supports terminal output, TXT and JSON report generation, and an interactive Streamlit dashboard.

## Project Objectives

The main objectives of this project are:

- To read and parse Apache access log files.
- To analyze website traffic and request patterns.
- To identify frequently requested URLs and active IP addresses.
- To monitor HTTP 4xx and 5xx errors.
- To detect failed login attempts based on HTTP 401 responses.
- To classify login activity into basic risk levels.
- To identify browsers and common bots.
- To generate readable and structured reports.
- To present analysis results through an interactive dashboard.
- To test the parser and analyzer using pytest.

## Project Workflow

The complete project workflow is shown below:

```text
Apache Access Log
        |
        v
     main.py
        |
        v
Read Log File Line by Line
        |
        v
     parser.py
        |
        v
   Parse Log Entry
        |
        v
 Parsed Log Record
        |
        v
    analyzer.py
        |
        v
Analyze Traffic, Errors,
Clients and Security
        |
        v
 Generate Final Results
        |
        +--------------------+--------------------+
        |                    |                    |
        v                    v                    v
    report.txt          report.json       Streamlit Dashboard
                                                  |
                                                  v
                                           4xx / 5xx Details
                                                  |
                                                  v
                                         IP + URL + Status
                                              + Count

       Testing: pytest
       Version Control: Git and GitHub
```

### Project Flowchart

The project flowchart provides a visual representation of how log data moves through the parser, analyzer, report generator, and dashboard.

![Apache Log Analyzer Project Flowchart](project-flowchartt.png)

**Note:** Keep the flowchart image in the project root and ensure its filename matches `project-flowchart.png`. If your actual image uses another filename, update the link above accordingly.

---

## Features

### 1. Basic Analysis

The analyzer calculates:

- Total number of requests
- Number of unique IP addresses
- HTTP methods used
- HTTP status code distribution
- Total response size
- Average response size

### 2. Traffic Analysis

The project examines website traffic using:

- Top IP addresses
- Most requested URLs
- Requests grouped by hour
- Busiest hour of the day

These statistics help summarize request distribution and identify the most active periods.

### 3. HTTP Error Analysis

The analyzer tracks HTTP errors and their occurrence counts.

Features include:

- 4xx client errors
- 5xx server errors
- Error counts by IP address
- Detailed 4xx error information
- Detailed 5xx error information
- IP address, URL, status code, and occurrence count for errors

The Streamlit dashboard allows users to open the 4xx and 5xx error summaries and inspect their details.

### 4. Security Analysis

The project includes basic security-related analysis:

- Failed login attempts
- Suspicious IP addresses
- Failed login counts by IP
- Security risk classification

Risk levels are classified as:

- **LOW**
- **MEDIUM**
- **HIGH**

The classification uses the number of HTTP 401 responses associated with an IP address.

These are project-defined rules for learning and log analysis, not a professional security verdict.

### 5. Client and Bot Analysis

The analyzer examines User-Agent information to identify browser and client activity.

Depending on the log entries and the detection logic, it can identify:

- Browser information
- Bot activity
- Detected bot types
- Python Requests clients
- curl clients
- Other recognized bots

Detection depends on the User-Agent values available in the log file and the patterns implemented in the project.

---

## Project Files

### `main.py`

`main.py` is the main entry point of the project.

It performs the following tasks:

- Accepts the log filename through a command-line argument.
- Reads the log file.
- Sends each line to the parser.
- Passes valid parsed records to the analyzer.
- Displays the analysis results in the terminal.
- Generates `report.txt`.
- Generates `report.json`.

Run the analyzer with:

```powershell
python main.py akash.log
```

Replace `akash.log` with another log filename if required.

### `parser.py`

This file is responsible for parsing Apache log entries.

It extracts:

- IP address
- Timestamp
- HTTP method
- Requested URL
- Status code
- Response size
- Referer
- User-Agent

The parser also handles invalid or unusual entries so that processing can continue for the remaining log lines.

### `analyzer.py`

This file contains the main `LogAnalyzer` class.

It processes parsed log records and calculates:

- Total request count
- Unique IP addresses
- Top IP addresses
- Top requested URLs
- HTTP method statistics
- HTTP status code statistics
- Total and average response sizes
- 4xx errors
- 5xx errors
- Failed login attempts
- Suspicious IP information
- Security risk levels
- Browser statistics
- Bot statistics
- Hourly traffic
- Busiest hour

The final analysis results are returned in a dictionary and used by the reporting and dashboard components.

### `dashboard.py`

This file contains the Streamlit dashboard.

It provides a visual interface for exploring the analysis results.

The dashboard displays:

- Summary statistics
- Traffic analysis
- Security information
- Browser information
- Bot information
- 4xx error summaries
- 5xx error summaries

The 4xx and 5xx summaries can be opened to view detailed information, including:

- IP address
- Requested URL
- HTTP status code
- Number of occurrences

### `check_parser.py`

This utility checks the parser's performance on a log file.

It displays:

- Total log lines
- Successfully parsed lines
- Failed lines

**Previously recorded results for the original log file:**

- Total Lines: 42,131
- Parsed Lines: 42,131
- Failed Lines: 0

These figures refer to the original dataset and should not be assumed to describe the newer `akash.log` dataset.

If `check_parser.py` uses a hardcoded filename, update it to use `akash.log` or modify it to accept a filename from the command line.

### `test_parser.py`

This file contains pytest tests for the parser.

It checks whether log entries are correctly converted into structured records.

### `test_analyzer.py`

This file contains pytest tests for the analyzer.

It checks whether the analyzer calculates statistics and security-related results correctly.

### `akash.log`

This is the current synthetic Apache log file used as input for the project.

It contains 1,000 generated log entries and can be used to test parsing, traffic analysis, HTTP error analysis, and the dashboard without using real website traffic.

The synthetic dataset uses documentation-only IP address ranges and fictional domains.

### `report.txt`

This file contains the analysis results in a readable text format.

Its sections include:

- Basic Summary
- HTTP Methods
- Status Codes
- Errors
- Security
- Top IPs
- Top URLs
- Browsers
- Bots
- Hourly Traffic
- Busiest Hour

The report is generated when the main analyzer runs successfully.

### `report.json`

This file stores the analysis results in JSON format.

JSON provides a structured representation that other programs and applications can read and process.

### `requirements.txt`

This file lists the Python package required for the Streamlit dashboard.

Current requirement:

```text
streamlit
```

### `README.md`

This file documents the project's purpose, features, setup, workflow, commands, and results.

### `project-flowchart.png`

This image represents the overall project workflow. The image must exist in the project root for the README preview to display it correctly.

---

## Requirements

Before running the project, make sure you have:

- Python installed
- pip package manager
- VS Code or another code editor
- The project files downloaded or cloned
- The input log file, such as `akash.log`

Streamlit is required to run the dashboard. Pytest is required to run the automated tests.

If pytest is not already installed, install it separately:

```powershell
python -m pip install pytest
```

## Installation and Setup

### Step 1: Clone the Repository

```powershell
git clone https://github.com/jhaakash2006/apache-log-analyzer.git
```

### Step 2: Open the Project Folder

```powershell
cd apache-log-analyzer
```

Open the folder in VS Code, or open a PowerShell terminal inside the project directory.

### Step 3: Install Requirements

```powershell
python -m pip install -r requirements.txt
```

If you want to run the automated tests, install pytest if needed:

```powershell
python -m pip install pytest
```

### Step 4: Check the Input File

Ensure that `akash.log` is present in the project directory.

The project structure and command examples in this README use `akash.log` as the current input filename.

---

## How to Run the Project

### Step 1: Run the Analyzer

```powershell
python main.py akash.log
```

The program reads the input file, parses log entries, analyzes the data, and displays the results in the terminal.

It also generates:

```text
report.txt
report.json
```

### Step 2: Check Parser Statistics

```powershell
python check_parser.py
```

This utility reports the total number of lines, successfully parsed lines, and failed lines.

If the utility is configured for a different filename, update its input path to `akash.log` first.

### Step 3: Launch the Streamlit Dashboard

```powershell
python -m streamlit run dashboard.py
```

Streamlit displays a local URL in the terminal. Open that address in your browser to explore the dashboard.

If the dashboard is configured to read a fixed filename, ensure that it points to `akash.log`.

### Step 4: Run the Tests

```powershell
python -m pytest
```

This command runs the available parser and analyzer tests, including:

- `test_parser.py`
- `test_analyzer.py`

Review the terminal output to see which tests pass or fail.

---

## Generated Reports

The main analyzer generates two report files.

### Text Report: `report.txt`

The text report is designed for easy reading.

It presents the key analysis results in organized sections, including traffic, methods, status codes, errors, security, clients, and hourly statistics.

### JSON Report: `report.json`

The JSON report stores the results in a structured format.

It can be useful for:

- Processing results with another Python script
- Integrating analysis results into another application
- Reusing statistics without parsing the text report

The actual contents depend on the input log file and the analysis performed.

---

## Current Analysis Results

The following figures were recorded for the **original log dataset containing 42,131 requests**. They are historical results and are not the results of the newer 1,000-line synthetic `akash.log` file.

| Metric | Previously Recorded Result |
|---|---:|
| Total Requests | 42,131 |
| Unique IP Addresses | 139 |
| Total Response Size | 844,976,114 bytes |
| Average Response Size | 20,055.92 bytes |
| 4xx Errors | 2,161 |
| 5xx Errors | 32 |
| Failed Login Attempts | 94 |
| Busiest Hour | 15:00 |
| Requests During Busiest Hour | 6,899 |

The analyzer also examines suspicious login activity and assigns risk levels based on failed login counts.

To document results from the current synthetic dataset, run the analyzer on `akash.log` and use the values produced by that run instead of the historical figures above.

---

## Security Analysis

The project implements a basic security monitoring mechanism using HTTP response codes and IP-based counts.

### Failed Login Detection

HTTP `401` responses are treated as failed login attempts by the project's analysis logic.

The analyzer tracks these events to identify IP addresses with repeated failed login activity.

### Risk Classification

The project uses the following thresholds:

| Failed Login Attempts | Risk Level |
|---|---|
| 20 or more | HIGH |
| 5 to 19 | MEDIUM |
| Fewer than 5 | LOW |

These thresholds are project-level rules applied to the available log data.

### Suspicious IP Detection

The analyzer also tracks repeated HTTP 4xx errors by IP address. In the current implementation, an IP may be flagged as suspicious when it has at least three tracked 4xx errors. Failed-login activity has a separate threshold of at least five attempts for suspicious login IP tracking.

These thresholds help demonstrate basic security analysis but do not prove that an IP address is malicious.

### Security Limitations

- HTTP 401 responses do not always represent a password failure; their meaning depends on the application.
- A high error count does not automatically mean an attack occurred.
- The project does not replace a professional SIEM, intrusion detection system, or security monitoring platform.
- Risk classifications depend on the implemented thresholds and the quality of the input logs.

---

## Testing

The project includes automated tests for its main components.

### Parser Tests

The parser tests verify that Apache log entries are converted into the expected structured fields.

### Analyzer Tests

The analyzer tests verify the calculation of traffic statistics, error counts, and security-related results.

### Run All Tests

```powershell
python -m pytest
```

### Check Parsing Success

```powershell
python check_parser.py
```

The parser-check utility helps compare the total number of input lines with the number successfully parsed and the number that failed.

---

## Technologies Used

- **Python:** Core programming language
- **Streamlit:** Interactive dashboard
- **Regular Expressions:** Pattern-based log parsing
- **Collections:** Counting and grouping log information
- **JSON:** Structured report generation
- **Pytest:** Automated testing
- **Git:** Version control
- **GitHub:** Remote repository and project hosting

## Main Python Concepts Used

The project uses the following Python concepts:

- Functions
- Classes and objects
- Dictionaries
- Lists
- Sets
- Loops
- Conditional statements
- File handling
- Exception handling
- JSON handling
- String processing
- Sorting
- Command-line arguments

These concepts are used to read log files, parse entries, calculate statistics, generate reports, and present results.

---

## Git and GitHub

Git is used to track changes in the project, while GitHub hosts the remote repository.

**Repository:** https://github.com/jhaakash2006/apache-log-analyzer

Common Git commands used during development include:

Check the current repository status:

```powershell
git status
```

Stage changes:

```powershell
git add .
```

Commit changes:

```powershell
git commit -m "Update project documentation"
```

Push changes to GitHub:

```powershell
git push
```

For the first push of a new local branch, you may need:

```powershell
git push -u origin main
```

---

## Project Structure

The project directory is organized as follows:

```text
apache-log-analyzer/
│
├── akash.log
├── analyzer.py
├── check_parser.py
├── dashboard.py
├── main.py
├── parser.py
├── test_analyzer.py
├── test_parser.py
├── requirements.txt
├── README.md
├── project-flowchart.png
│
├── report.txt
└── report.json
```

**Note:** `report.txt` and `report.json` are generated by the analyzer. They may not exist until the project has been run. The flowchart image must also be present in the root directory for its README preview to work.

---

## Project Output

The project provides three main ways to view analysis results.

### 1. Terminal Output

Run:

```powershell
python main.py akash.log
```

The terminal displays the analysis produced from the selected input file.

### 2. Text and JSON Reports

The analyzer generates:

```text
report.txt
report.json
```

The text report is readable by humans, while the JSON report provides structured data for other applications.

### 3. Streamlit Dashboard

Run:

```powershell
python -m streamlit run dashboard.py
```

The dashboard provides an interactive view of traffic, HTTP errors, browser information, bots, and security-related statistics.

The dashboard also allows users to inspect detailed 4xx and 5xx error information, including IP addresses, URLs, status codes, and occurrence counts.

---

## Limitations and Future Scope

The project currently provides basic log parsing, statistical analysis, report generation, and dashboard visualization.

Possible future improvements include:

- Real-time log file monitoring
- Automated alerts for repeated failed login attempts
- More advanced suspicious activity detection
- Additional log formats and configurable input paths
- Exporting dashboard results to additional formats
- More extensive test coverage
- Improved dashboard filters and visualizations

These are possible enhancements and should not be considered implemented features unless they are added to the code.

---

## Conclusion

Apache Log Analyzer demonstrates a complete basic workflow for Apache web server log analysis.

It reads access logs, parses individual requests, analyzes traffic patterns, identifies HTTP errors, examines browser and bot activity, tracks failed login attempts, and classifies suspicious login activity using configurable project rules.

The project presents its results through terminal output, TXT and JSON reports, and an interactive Streamlit dashboard.

It also includes parser and analyzer tests using pytest and uses Git and GitHub for version control and project hosting.

Through this project, practical experience is gained in Python programming, file processing, data analysis, basic security monitoring, dashboard development, testing, and software project management.

---

## Author

**Jhaakash**

**GitHub:** https://github.com/jhaakash2006/apache-log-analyzer