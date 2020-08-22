import time
class ProgressBar:
    def __init__(self, N):
        """ setup maximum value """
        self.N = N
        self.n = 0
    def update(self, n):
        """ update value and print """
        self.n += n
        precent = self.n / self.N * 100
        if precent >= 100:
            end = '\n'
        else:
            end = '\r'
        print("Progress: {:.2f}%".format(precent), end=end)
        # time.sleep(0.1)


if __name__ == '__main__':
    pb = ProgressBar(100000)
    for i in range(100000):
        pb.update(1)


