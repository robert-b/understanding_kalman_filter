import numpy as np
import matplotlib.pyplot as plt
import random


class kalman_filter:

    def __init__(self):
        self.A = 1
        self.H = 1
        self.Q = 0
        self.R = 4
        self.x = 14
        self.P = 6

    def run(self, z):

        xp = np.dot(self.A, self.x)

        Pp = np.dot(np.dot(self.A, self.P), self.A) + self.Q
        K = np.dot(np.dot(np.dot(Pp, self.H), self.A), 1/(np.dot(np.dot(self.H, Pp), self.H) + self.R))
        self.x = xp + K*(z - self.H*xp)
        self.P = Pp - K * self.H * Pp

        volt = self.x

        return volt

# test kalman_filter --------------------------------------------------------------------------------------------------

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
kalmanFilter = kalman_filter()

tracked_x = []
tracked_avg = []

for i in range(0, len(t)):
    z = get_volt()
    kalmanFilter.run(z)
    tracked_x.append(z)
    tracked_avg.append(kalmanFilter.x)

plt.plot(t, tracked_x)
plt.plot(t, tracked_avg, 'r')

plt.show()








