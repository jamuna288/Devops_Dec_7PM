def is_ready(status):
    global attempts
    attempts=0
    print("attempts=",attempts)
    return status=="ready"
status="not ready"
while not is_ready(status) and attempts<5:
    attempts+=1
    if attempts==3:
        break