import threading 
import time 

def show(arg):
    time.sleep(arg)
    print('thread%d'%arg)

for i in range(10):
    t = threading.Thread(target = show , args=(i,))
    t.start()

print("main thread stop")