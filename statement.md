Ransomware Behavior Detector

1. Problem Statement

Ransomware can cause unusual file activity by creating or modifying many files. This project provides a simple Python-based method to monitor a selected folder and detect such activity. It performs two scans 30 seconds apart, compares the files, and calculates a basic risk level.

2. Scope

The project can:

* Scan a selected folder.
* Detect new and modified files.
* Calculate a simple risk score.
* Display the risk level and warnings.
* Save results in log.txt.

It is an educational prototype and is not a replacement for professional antivirus software.

3. Target Users

* Students learning Python and cybersecurity.
* Beginners learning file monitoring.
* Users experimenting with basic ransomware behavior detection.

4. High-Level Features

* Folder Scanning – Collects file names and modification times.
* Change Detection – Finds new and modified files.
* Risk Analysis – Classifies activity as SAFE, SUSPICIOUS, or HIGH RISK.
* Alerts – Displays warnings for suspicious activity.
* Logging – Saves scan results to log.txt.

5. Technologies

* Python 3
* os module
* time module
* Functions, loops, dictionaries, and file handling
