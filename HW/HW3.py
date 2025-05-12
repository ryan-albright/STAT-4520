import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

data = np.array([74.1, 74.5, 73.2, 70.7, 72, 72, 73.15, 72.7, 73.1, 73.5, 74.5, 76.65, 76.3, 76.5, 78.3, 79.1, 
                 80.3, 77.75, 78.05, 79.6, 80.1, 81.45, 83.15, 82.4, 84.55, 85.2, 85.35, 87, 87.95])

a_hat = np.mean(data)

t_bar = (len(data) + 1) / 2

b_num = 0
b_denom = 0
for i in range(1, len(data) + 1):
    b_num += (data[i - 1] - a_hat)*(i - t_bar)
    b_denom += (i - t_bar)**2

b_hat = b_num / b_denom

print(a_hat, b_hat)

# Calculation of Upper & Lower Confidence Intervals
Q = 0
for i in range(1, len(data) + 1):
    Q += (data[i - 1] - a_hat - b_hat*(i - t_bar))**2

var_epsilon = Q / (len(data) - 2)
N = len(data)
m = 5
alpha = 0.05 / 2

conf_int = lambda m: t.ppf(1 - alpha, N - 2)*np.sqrt(var_epsilon*(1 + 1/N + (N + m - t_bar)**2 / b_denom))

f = lambda x: b_hat*(x - t_bar) + a_hat
c1 = lambda x: b_hat*(x - t_bar) + a_hat + conf_int(x - N)
c2 = lambda x: b_hat*(x - t_bar) + a_hat - conf_int(x - N)

x1 = np.array([i for i in range(1, len(data) + 1)])
x2 = np.array([i for i in range(1, len(data) + 6)])
x3 = np.array([i for i in range(len(data) + 1, len(data) + 6)])

print(c1(x3), c2(x3))

plt.plot(x1, data, label = 'Data')
plt.plot(x2, f(x2), label = 'Linear Trend')
plt.plot(x3, c1(x3), label = 'Upper confidence Interval') # upper confidence interval
plt.plot(x3, c2(x3), label = 'Lower confidence Interval') # lower confidence interval
plt.legend()

plt.show()



