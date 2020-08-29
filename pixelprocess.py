from multiprocessing import Process, Array
import time

image = Array('i', range(0))
image = []

def fun(pixels, i):
    print("Task {} started".format(i))
    for _ in range(100000000):
        pass
    print("Task {} finised".format(i))
    pixels[i] = 1


for j in range(3):
    pixels = Array('i', range(8))
    t1 = time.time()
    ts = []
    for i in range(8):
        t = Process(target=fun, args=(pixels, i))
        t.start() 
        ts.append(t)

    for t in ts:
        t.join()
    print("j : {}", format(j))
    image.append(pixels[:])



print("Time Spend: {:.2f} s".format(time.time() - t1))
print(pixels[:])

