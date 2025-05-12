import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('Final_Exam\Q8_data.txt', dtype = float)

N = len(data)
mu_x = np.mean(data)
M = 10

freq = np.linspace(0, np.pi, 200)

R = np.empty(N-1) # calculating autocovariance function
for k in range(N-1):
    R[k] = (1/N)*sum((data[:N-k] - mu_x)*(data[k:] - mu_x))

# Truncated Periodogram
f = (1 / (2 * np.pi)) * np.array([R[0] + 2 * np.sum([R[k] * np.cos(w * k) for k in range(1, M + 1)]) for w in freq])
plt.plot(freq, f)
plt.xlabel('Frequency')
plt.ylabel('Spectrum')
plt.show()

# Triangular Window
f = (1 / (2 * np.pi)) * np.array([R[0] + 2 * np.sum([(1 - k / M) * R[k] * np.cos(w * k) for k in range(1, M + 1)]) for w in freq])
plt.plot(freq, f)
plt.xlabel('Frequency')
plt.ylabel('Spectrum')
plt.show()

# Parzen Window
def lambda_k (x):
    if x <= 0.5:
        return 1 - 6*x**2 + 6*x**3
    elif x <= 1:
        return 2*(1 - x)**3
    else:
        return 0
f = (1 / (2 * np.pi)) * np.array([R[0] + 2 * np.sum([lambda_k(k / M) * R[k] * np.cos(w * k) for k in range(1, M + 1)]) for w in freq])
plt.plot(freq, f)
plt.xlabel('Frequency')
plt.ylabel('Spectrum')
plt.show()