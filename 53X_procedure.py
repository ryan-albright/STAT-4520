import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('Final_Exam\Q2_data.txt', dtype=float)

l = 15 # 15 points on either side to create a moving average
N = len(data)

a_tilde_a = np.empty(N - 2*l)
# We effectively want to have a window of of 31 points as we loop through the data
for i in range(l, N - l): # we need l points before and after the current point
    a_tilde_a[i - l] = sum(data[i-l:i+l+1]) / (2*l + 1)

a_tilde_b = np.empty(N - 2*l - 8)
# We saw a couple outliers in the prior data set, so we can use the 53X method to eliminate their effects

# creation of Xt (median based on window of 5)
Xt = []
for i in range(2, N - 2):
    Xt.append(np.median(data[i - 2: i + 2 + 1]))

# creation of Yt (median based on window of 3)        
Yt = []
for i in range(1, N - 5):
    Yt.append(np.median(Xt[i - 1: i + 1 + 1]))

# creation of Zt (weighted average between the three values)
Zt = []
for i in range(1, N - 7):
    z = sorted(Yt[i - 1: i + 1 + 1])
    Zt.append(z[0]*0.25 + z[1]*0.5 + z[2]*0.25)

Zt = np.array(Zt)
for i in range(l, N - l - 8): # we need l points before and after the current point
    a_tilde_b[i - l] = sum(Zt[i-l:i+l+1]) / (2*l + 1)

x1 = np.array([i for i in range(1, N + 1)])
x2 = np.array([i for i in range(1 + 4, N + 1 - 4)])
x3 = np.array([i for i in range(l, N - l)])
x4 = np.array([i for i in range(l + 4,N - l - 4)])

plt.plot(x1, data, label = 'Data')
plt.plot(x2, Zt, label = 'Data after 53X Procedure')
plt.legend()
plt.show()

plt.plot(x1, data, label = 'Data')
plt.plot(x3, a_tilde_a, label = '1st Order Moving Average')
plt.plot(x4, a_tilde_b, label = '1st Order Moving Average from 53X')
plt.legend()
plt.show()