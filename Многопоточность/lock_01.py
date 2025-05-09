import time
import threading


value = 0
locker = threading.Lock()

def inc_value():
    global value
    while True:
        with locker:
            value += 1
            print(value)
            time.sleep(0.1)


for _ in range(5):
    threading.Thread(target=inc_value).start()