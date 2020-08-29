from threading import Thread
import time

def fun(i):
    print("Task {} started".format(i))
    for _ in range(100000000):
        pass
    print("Task {} finised".format(i))


t1 = time.time()
ts = []
for i in range(8):
    t = Thread(target=fun, args=(i,))
    t.start() 
    ts.append(t)

for t in ts:
    t.join()


print("Time Spend: {:.2f} s".format(time.time() - t1))

