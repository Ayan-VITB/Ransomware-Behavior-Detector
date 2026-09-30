# Ransomware Behavior Detector

## 1. About the Project

This is my Python project which checks a selected folder for unusual file activity.

This program will takes two scans of the folder with a 30-second gap between them. It will checking for files that are newly created or modified and then calculates a risk score based on the changes.

## 2. How It Works

1. The user enter the folder path.
2. The program take the first scan.
3. It wait for 30 seconds.
4. The program takes the second scan.
5. Both scans are compared.
6. The risk score is calculated.
7. The result is displayed.
8. The result is also saved in `log.txt`.

## 3. Risk Calculation

The program uses some simple rules to calculate the risk:

* 5 or more changed files → **+2 points**
* 1 or more new files → **+1 point**

The final result is:

* **0 points → SAFE**
* **1 point → SUSPICIOUS**
* **2 or more points → HIGH RISK**

For example, if 5 files are changed and 1 new file is created, the risk score will be 3. In this case, the result will be **HIGH RISK**.

## 4. Project Files

```text
VITYARTHIProject/

│
├── main.py
├── monitor.py
├── analyzer.py
├── alert.py
├── logger.py
├── test.py
├── README.md
└── test_folder/
```

### main.py

Runnings the main program. It will takes the folder path from the user, performs the two scans and displays the result.

### monitor.py

Scans the selected folder and stores the file names and their last modified times.

### analyzer.py

Compares the two scans and calculates the risk score.

### alert.py

Displays the scan result and shows a warning according to the risk level.

### logger.py

Saves the scan result in `log.txt`.

## 5. Technologies Used

* Python
* `os` module
* `time` module
* Functions
* Loops
* Dictionaries
* File handling

## 6. Requirements

* Python 3

# 7. Note 
This is for my VITYARTHI project
