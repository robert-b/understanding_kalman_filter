import numpy as np
import matplotlib.pyplot as plt
import random
import scipy.io
class move_average_filter:

    def __init__(self, n=10):
        self.init=True
        self.number = n
        self.buf = []
        self.prevAgv = 0
        self.avg = 0
        pass

    def run(self, x):
        if self.init == True:
            [self.buf.append(x) for i in range(0, self.number)]
            self.prevAgv = x
            self.avg = x
            self.init = False

        self.buf.pop(0)
        self.buf.append(x)
        self.prevAgv = self.avg

        self.avg = self.prevAgv + (x - self.buf[0])/self.number

        return self.avg


# test moving_average_filter --------------------------------------------------------------------------------------------------

# Test시, n을 낮추면 낮출수록 Raw 데이터를 따라가야하는데,
# 재귀식의 영향으로 계산이 안됨.

class Alt:
    def __init__(self):
        self.init = True
        self.k = 0
        self.h = 0

    def get_sonar(self):
        if self.init == True:
            self.mat = scipy.io.loadmat('./SonarAlt.mat')
            self.init = False
        self.h = self.mat['sonarAlt'][0][self.k]
        self.k += 1

        return self.h


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

Nsample = 500
Xsaved = []
Xmsaved = []

alt =Alt()
filter = move_average_filter(10)
for i in range(0, Nsample):
    xm = alt.get_sonar()
    x = filter.run(xm)
    Xsaved.append(x)
    Xmsaved.append(xm)

dt = 0.02
t = frange(0, (Nsample * dt)-dt, dt)

plt.plot(t, Xmsaved)
plt.plot(t, Xsaved, 'ro')
plt.show()