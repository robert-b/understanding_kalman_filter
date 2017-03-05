import numpy as np
import matplotlib.pyplot as plt
import random


class average_filter:

    def __init__(self):
        self.k = 1
        self.avg = 0

    def run(self, x):

        alpha = 1 - 1/ self.k
        self.k += 1
        self.avg = alpha * self.avg + (1 - alpha) * x
        return self.avg

# test average_filter --------------------------------------------------------------------------------------------------

def get_volt():
    w = 0 + random.gauss(0,4)
    return 14.4+w

def frange(start, end, step):
    list = []
    value = start
    while True:
        if(value >= end):
            break
        list.append(value)
        value += step

    list = ["%g" % x for x in list]
    return list

dt = 0.2
t = frange(0, 10, dt)
Nsample = len(t)
avgFilter = average_filter()

tracked_x = []
tracked_avg = []

for i in range(0, len(t)):
    x = get_volt()
    avgFilter.run(x)
    tracked_x.append(x)
    tracked_avg.append(avgFilter.avg)

plt.plot(t, tracked_x)
plt.plot(t, tracked_avg, 'ro')
plt.show()

print("Average : {}".format(avgFilter.avg))







