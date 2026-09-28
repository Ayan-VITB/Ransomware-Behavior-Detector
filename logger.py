def save_log(result):
    file = open("log.txt", "a")
    file.write(result + "\n")
    file.close()