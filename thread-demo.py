import threading
from time import sleep

def print_msg(N,delay):
    for i in range(100):
        print '----> This is a message from %s'%N
        sleep(delay)

for i in range(2,5):
    threading.Thread(target=print_msg,args=(i,i)).start()


