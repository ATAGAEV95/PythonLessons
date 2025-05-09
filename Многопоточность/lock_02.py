import threading


locker = threading.Lock()


def inc_value():
    print('Блокируем поток')
    locker.acquire()
    print('Поток разблокирован')


t1 = threading.Thread(target=inc_value)
t2 = threading.Thread(target=inc_value)
t1.start()
t2.start()
# locker.release()