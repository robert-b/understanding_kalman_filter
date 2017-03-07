import numpy as np
import matplotlib.pyplot as plt
import random
import scipy.io

class LPF:

    def __init__(self, alpha):
        ''' alpha range should be (0 < alpha < 1)'''
        self.prevX = 0
        self.alpha = alpha
        self.init = True

    def run(self, x):
        if self.init == True:
            self.prevX = x
            self.init = False

        xlpf = self.alpha * self.prevX + (1-self.alpha)*x

        self.prevX = xlpf

        return self.prevX

# test average_filter --------------------------------------------------------------------------------------------------

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

lpf = LPF(0.7)
for i in range(0, Nsample):
    xm = alt.get_sonar()
    x = lpf.run(xm)
    Xsaved.append(x)
    Xmsaved.append(xm)

dt = 0.02
t = frange(0, (Nsample * dt)-dt, dt)

plt.plot(t, Xmsaved)
plt.plot(t, Xsaved, 'r')
plt.show()
