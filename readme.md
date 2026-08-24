Apache Log Analyzer

This project is a simple Python based Apache log analyzer.

It reads an Apache access log file and shows useful information about website traffic, errors and basic security activity.

What this project does

The program reads the access.log file line by line and analyzes each request.

It shows:

Total number of requests
Unique IP addresses
HTTP methods
HTTP status codes
Total response size
Average response size
Top IP addresses
Most requested URLs
Browser information
Bot information
Hourly traffic
Busiest hour
4xx and 5xx errors
Failed login attempts
Suspicious IP addresses
Security risk levels

Project files

main.py
This is the main file used to run the analyzer. It prints the complete analysis and also saves the result in report.txt.

parser.py
This file reads each Apache log line and converts it into useful information such as IP address, request method, URL, status code, response size, referer and browser.

analyzer.py
This file processes the parsed records and calculates the different statistics used in the report.

check_parser.py
This file is used to test the parser and check how many log lines were successfully parsed.

dashboard.py
This file is used for the Streamlit dashboard.

access.log
This is the Apache access log file used as input.

report.txt
This contains the readable text version of the analysis.

report.json
This contains the analysis results in JSON format.

How to run

Open PowerShell in the project folder.

Run:

python main.py access.log

The program will analyze the log file and display the results in the terminal.

It also creates:

report.txt

report.json

Parser testing

To check whether all log lines are being parsed correctly, run:

python check_parser.py

The current log file contains 42131 lines and the parser successfully processes all 42131 lines.

Dashboard

The project also contains a Streamlit dashboard.

Run:

streamlit run dashboard.py

Then open the local address shown by Streamlit in the browser.

Technologies used

Python
Regular Expressions
Collections
JSON
Streamlit

Project result

The analyzer can process the Apache access log and provide a complete overview of website traffic, common requests, errors, bots and suspicious login activity.