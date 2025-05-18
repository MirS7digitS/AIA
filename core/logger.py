def log_event(event):
    with open("data/log.txt", "a") as f:
        f.write(f"{event}\n")
