import threading

def say_sth(str):
  print (str)
  t = threading.Timer(2.0, say_sth,[str])
  t.start()

if __name__ == '__main__':
  timer = threading.Timer(2.0,say_sth,['i am here too.'])
  timer.start()