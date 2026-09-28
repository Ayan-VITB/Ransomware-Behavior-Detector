def show_alert(changed, new_files, risk, result):

    print("   SCAN RESULT")
    print("-------------------")
    print("Changed files :", changed)
    print("New files     :", new_files)
    print("Risk score    :", risk)
    print("Risk level    :", result)
    if result == "HIGH RISK":
        print("\nWARNING!")
        print("Suspicious file activity detected.")
    elif result == "SUSPICIOUS":
        print("\nCAUTION!")
        print("Some unusual activity was detected.")
    else:
        print("\nFolder appears normal.")