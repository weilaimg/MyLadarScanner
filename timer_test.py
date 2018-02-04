import threading
import time



def fun_timer():
    print('Hello Timer!')
    global timer
    timer = threading.Timer(0.200, fun_timer)
    timer.start()
    
timer = threading.Timer(0.200, fun_timer)
timer.start()