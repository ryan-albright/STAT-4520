import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t
# This script contains the creation of a simple linear model as well as confidence intervals for the predictions of the next 5 data points

# Data Set & Other Calculated Parameters
data = np.array([74.1, 74.5, 73.2, 70.7, 72, 72, 73.15, 72.7, 73.1, 73.5, 74.5, 76.65, 76.3, 76.5, 78.3, 79.1, 
                 80.3, 77.75, 78.05, 79.6, 80.1, 81.45, 83.15, 82.4, 84.55, 85.2, 85.35, 87, 87.95])

N = len(data)

# Calculation of a hat and b hat
a_hat = np.mean(data)

t_bar = (len(data) + 1) / 2

b_num = 0
b_denom = 0
for i in range(1, len(data) + 1):
    b_num += (data[i - 1] - a_hat)*(i - t_bar)
    b_denom += (i - t_bar)**2

b_hat = b_num / b_denom

# Calculation of Upper & Lower Confidence Intervals
Q = 0
for i in range(1, N + 1):
    Q += (data[i - 1] - a_hat - b_hat*(i - t_bar))**2

var_epsilon = Q / (N - 2)
alpha = 0.05 / 2 # hypothesis testing input
m = 5 # number of points being predicted into the future

conf_int = lambda m: t.ppf(1 - alpha, N - 2)*np.sqrt(var_epsilon*(1 + 1/N + (N + m - t_bar)**2 / b_denom)) 

# Initializing Functions for various lines
f = lambda x: b_hat*(x - t_bar) + a_hat
upper_f = lambda x: b_hat*(x - t_bar) + a_hat + conf_int(x - N)
lower_f = lambda x: b_hat*(x - t_bar) + a_hat - conf_int(x - N)

# Plotting of Data, f(x), and lower & upper bounds
x1 = np.array([i for i in range(1, N + 1)])
x2 = np.array([i for i in range(1, N + m + 1)])
x3 = np.array([i for i in range(N + 1, N + m + 1)])

plt.plot(x1, data, label = 'Data')
plt.plot(x2, f(x2), label = 'Linear Trend')
plt.plot(x3, upper_f(x3), label = 'Upper confidence Interval') # upper confidence interval
plt.plot(x3, lower_f(x3), label = 'Lower confidence Interval') # lower confidence interval
plt.legend()
plt.show()