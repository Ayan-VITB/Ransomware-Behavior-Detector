def analyze(old_files, new_files):
    changed = 0
    new_files_count = 0
    for file in new_files:
        if file not in old_files:
            new_files_count = new_files_count + 1
        elif new_files[file] != old_files[file]:
            changed = changed + 1
    risk = 0
    if changed >= 5:
        risk = risk + 2
    if new_files_count >= 1:
        risk = risk + 1
    if risk >= 2:
        result = "HIGH RISK"
    elif risk == 1:
        result = "SUSPICIOUS"
    else:
        result = "SAFE"
    return changed, new_files_count, risk, result