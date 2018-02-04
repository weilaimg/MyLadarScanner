import threading
import time



def fun_timer():
    global timer
    timer = threading.Timer(0.200, fun_timer)
    timer.start()
    print('Hello Timer!')
    
timer = threading.Timer(0.200, fun_timer)
timer.start()

time.sleep(3) # 15秒后停止定时器
timer.cancel()