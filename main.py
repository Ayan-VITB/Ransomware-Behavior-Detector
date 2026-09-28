import os
import time
import monitor
import analyzer
import alert
import logger
print("  RANSOMWARE BEHAVIOR DETECTOR")
print("--------------------------------")
while True:
    print("\n1. Scan for a folder path")
    print("2. Exit")
    choice = input("Enter 1 or 2 from the menu: ").strip()
    if choice == "1":
        folder = input("Please enter the folder path: ").strip()
        # checking whether the path exists, so we don't wait 30 sec for nothing
        if not os.path.isdir(folder):
            print("\nFolder is not found! Please check the path and try again.")
            continue
        print("\nTrying primary scan...")
        primary_scan = monitor.get_files(folder)
        print("Files found:", len(primary_scan))
        # users can add or edit files in the folder during this time and the program will detect it
        print("Monitoring the path location for 30 seconds...")
        time.sleep(30)
        print("\nTrying for secondary scan...")
        secondary_scan = monitor.get_files(folder)
        changed, new_count, risk, result = analyzer.analyze(primary_scan, secondary_scan)
        alert.show_alert(changed, new_count, risk, result)
        logger.save_log(result)
        print("\nResult are being saved in log.txt")
    elif choice == "2":
        print("\nProgram will be closed now.")
        break
    else:
        print("\nInvalid choice! Please enter 1 or 2 from the menu.")