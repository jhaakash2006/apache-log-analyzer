# Apache Log Analyzer

Apache Log Analyzer is a Python-based project that reads an Apache access log file and analyzes website traffic, errors, client information, and basic security activity.

The project can process thousands of log requests and generate useful statistics in the terminal, text report, JSON report, and an interactive Streamlit dashboard.

GitHub: https://github.com/jhaakash2006/apache-log-analyzer


## Project Overview

The analyzer reads the Apache `access.log` file line by line.

Each log line is parsed and converted into structured information such as:

- IP address
- Timestamp
- HTTP method
- Requested URL
- HTTP status code
- Response size
- Referer
- User-Agent

The parsed information is then processed by the analyzer to calculate different traffic, error, client, and security statistics.


## Project Workflow

The complete project flow is:

Apache Access Log
        ↓
main.py
        ↓
Read Log File Line by Line
        ↓
parser.py
        ↓
Parse Log Entry
        ↓
Parsed Log Record
        ↓
analyzer.py
        ↓
Analyze Traffic, Errors, Clients and Security
        ↓
Generate Final Results
        ↓
 ┌───────────────────┬─────────────────────┐
 │                   │                     │
 ▼                   ▼                     ▼
report.txt       report.json       Streamlit Dashboard
                                      ↓
                               4xx / 5xx Details
                                      ↓
                              IP + URL + Status
                                   + Count

Testing is done using pytest and the project is managed using Git and GitHub.

![Apache Log Analyzer Project Flowchart](project-flowchartt.png)


## What This Project Does

The project provides the following analysis:

### Basic Analysis

- Total number of requests
- Unique IP addresses
- HTTP methods
- HTTP status codes
- Total response size
- Average response size

### Traffic Analysis

- Top IP addresses
- Most requested URLs
- Requests by hour
- Busiest hour of the day

### Error Analysis

- 4xx errors
- 5xx errors
- Error counts by IP
- Detailed 4xx error information
- Detailed 5xx error information
- IP, URL, status code and occurrence count for errors

### Security Analysis

- Failed login attempts
- Suspicious IP addresses
- Failed login count by IP
- Security risk classification

Risk levels are classified as:

- LOW
- MEDIUM
- HIGH

### Client Analysis

- Browser information
- Bot detection
- Bot types
- Python Requests
- curl
- Other detected bots


## Project Files

### main.py

This is the main file used to run the analyzer.

It:

- Takes the log file name from the command line
- Reads the log file
- Sends each line to the parser
- Sends valid records to the analyzer
- Displays the complete analysis
- Creates `report.txt`
- Creates `report.json`

Run it using:

    python main.py access.log


### parser.py

This file is responsible for parsing Apache log lines.

It extracts information such as:

- IP address
- Timestamp
- HTTP method
- URL
- Status code
- Response size
- Referer
- User-Agent

It also handles invalid or unusual log entries so that the analyzer can continue processing the remaining log file.


### analyzer.py

This file contains the main `LogAnalyzer` class.

It processes the parsed records and calculates:

- Request counts
- Unique IPs
- Top IPs
- Top URLs
- HTTP methods
- Status codes
- Response sizes
- 4xx errors
- 5xx errors
- Failed login attempts
- Suspicious IPs
- Security risk levels
- Browsers
- Bots
- Hourly traffic
- Busiest hour

The final results are returned as a dictionary and are used by both the reports and dashboard.


### dashboard.py

This file contains the Streamlit dashboard.

The dashboard provides a visual way to view the analysis.

It displays:

- Summary information
- Traffic analysis
- Security information
- Browser information
- Bot information
- 4xx errors
- 5xx errors

The 4xx and 5xx error summaries can be opened to view detailed error information including:

- IP address
- URL
- Status code
- Number of occurrences


### check_parser.py

This file is used to check the parser.

It reads the complete log file and shows:

- Total log lines
- Successfully parsed lines
- Failed lines

For the current log file:

- Total Lines: 42131
- Parsed Lines: 42131
- Failed Lines: 0


### test_parser.py

This file contains pytest tests for the log parser.

It checks whether log lines are correctly converted into structured records.


### test_analyzer.py

This file contains pytest tests for the analyzer.

It checks whether the analyzer correctly calculates statistics and security-related results.


### access.log

This is the Apache access log file used as input for the project.

The current log file contains 42,131 requests.


### report.txt

This file contains the analysis results in a readable text format.

It includes sections for:

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


### report.json

This file contains the analysis results in JSON format.

JSON makes the results easier to use with other programs or applications.


### requirements.txt

This file contains the Python package required for the Streamlit dashboard.

Current requirement:

    streamlit


## How to Run the Project

### Step 1: Open the Project

Open the project folder in VS Code.

Open PowerShell or the VS Code terminal inside the project folder.


### Step 2: Install Requirements

Run:

    pip install -r requirements.txt


### Step 3: Run the Analyzer

Run:

    python main.py access.log

The program will read the log file and display the analysis in the terminal.


### Step 4: Check the Parser

Run:

    python check_parser.py

This checks how many log lines were successfully parsed.


### Step 5: Run the Dashboard

Run:

    streamlit run dashboard.py

Streamlit will provide a local address.

Open that address in the browser to view the dashboard.


### Step 6: Run Tests

Run:

    pytest

This runs the parser and analyzer tests.

The project contains:

- `test_parser.py`
- `test_analyzer.py`


## Generated Reports

After running the analyzer, two report files are generated:

    report.txt
    report.json

`report.txt` is useful for reading the results easily.

`report.json` stores the same analysis results in a structured JSON format.


## Current Analysis Result

The current Apache log contains 42,131 requests.

Some of the main results are:

- Total Requests: 42,131
- Unique IPs: 139
- Total Response Size: 844,976,114 bytes
- Average Response Size: 20,055.92 bytes
- 4xx Errors: 2,161
- 5xx Errors: 32
- Failed Login Attempts: 94
- Busiest Hour: 15:00
- Requests During Busiest Hour: 6,899

The analyzer also detects suspicious login activity and assigns risk levels based on failed login attempts.


## Security Analysis

The project includes a basic security monitoring system.

HTTP `401` responses are treated as failed login attempts.

The project classifies login risk using the following rules:

- 20 or more failed logins → HIGH
- 5 to 19 failed logins → MEDIUM
- Less than 5 failed logins → LOW

The dashboard and reports can show suspicious login IPs and their failed login counts.

This security classification is a project-level rule used for log analysis and is not a replacement for a professional security monitoring system.


## Technologies Used

- Python
- Streamlit
- Regular Expressions
- Collections
- JSON
- Pytest
- Git
- GitHub


## Main Python Concepts Used

The project uses several basic Python concepts:

- Functions
- Classes
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


## Git and GitHub

Git is used to manage changes in the project.

The project is stored on GitHub:

https://github.com/jhaakash2006/apache-log-analyzer

Basic Git commands used in the project include:

    git status
    git add .
    git commit -m "Commit message"
    git push


## Project Output

The final project provides three main ways to view the analysis:

1. Terminal Output

   The complete analysis is displayed after running:

       python main.py access.log

2. Text and JSON Reports

       report.txt
       report.json

3. Streamlit Dashboard

   The dashboard provides an interactive view of traffic, errors, bots, browsers, and security information.


## Project Structure

    apache-log-analyzer/
    │
    ├── access.log
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


## Project Result

This project provides a complete basic workflow for Apache log analysis.

It can read a large Apache access log, parse individual requests, analyze traffic patterns, identify errors, detect bots, monitor failed login attempts, classify suspicious activity, and present the results through terminal output, reports, and a Streamlit dashboard.

The project also includes parser and analyzer tests using pytest and uses Git/GitHub for version control.


## Author

Jhaakash

GitHub:
https://github.com/jhaakash2006/apache-log-analyzer