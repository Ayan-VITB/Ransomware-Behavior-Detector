import os
def get_files(folder):
    files = {}
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        if os.path.isfile(path):
            files[file] = os.path.getmtime(path)
    return files