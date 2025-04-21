import numpy as np
import matplotlib.pyplot as plt

# Question 1
w_0 = np.pi / 20
A = np.tan(w_0 /2 )

b0 = A**2
b1 = 2*A**2
b2 = A**2

a0 = 1 + np.sqrt(2)*A + A**2
a1 = -2*(1 - A**2)
a2 = 1 - np.sqrt(2)*A + A**2

X = np.loadtxt('Data/5-2-1-data.txt', dtype=float)
Y = np.zeros(X.size)

for t in range(2, X.size):
    rhs = b0 *X[t] + b1*X[t-1] + b2*X[t-2]
    Y[t] = (rhs - a1*Y[t-1] - a2*Y[t-2]) / a0

# plt.plot(X, label = 'Original Data')
plt.plot(Y, label = 'Filtered Data')
# plt.legend()
plt.show()

# Question 2
w_0 = 19 * np.pi / 20
C = 1 / np.tan(w_0 / 2)

b0 = C**2
b1 = -2*C**2
b2 = C**2

a0 = 1 + np.sqrt(2)*C + C**2
a1 = -2*(C**2 - 1)
a2 = 1 - np.sqrt(2)*C + C**2

X = np.loadtxt('Data/5-2-2-data.txt', dtype=float)
Y = np.zeros(X.size)

for t in range(2, X.size):
    rhs = b0 *X[t] + b1*X[t-1] + b2*X[t-2]
    Y[t] = (rhs - a1*Y[t-1] - a2*Y[t-2]) / a0

# plt.plot(X, label = 'Original Data')
plt.plot(Y, label = 'Filtered Data')
# plt.legend()
plt.show()

# Question 3
w_0 = 5 * np.pi / 6
B = np.pi / 20

D = np.cos(w_0) / np.cos(B)
E = np.tan(B)

b0 = E
b2 = -E

a0 = E + 1
a1 = -2*D
a2 = 1 - E

X = np.loadtxt('Data/5-2-3-data.txt', dtype=float)
Y = np.zeros(X.size)

for t in range(2, X.size):
    rhs = b0 *X[t] + b2*X[t-2]
    Y[t] = (rhs - a1*Y[t-1] - a2*Y[t-2]) / a0

# plt.plot(X, label = 'Original Data')
plt.plot(Y, label = 'Filtered Data')
# plt.legend()
plt.show()

# Question 4
w_0 = np.pi / 3
B = np.pi / 10

D = np.cos(w_0) / np.cos(B)
E = np.tan(B)

b0 = 1
b1 = -2*D
b2 = 1

a0 = E + 1
a1 = -2*D
a2 = 1 - E

X = np.loadtxt('Data/5-2-4-data.txt', dtype=float)
Y = np.zeros(X.size)

for t in range(2, X.size):
    rhs = b0 *X[t] + b1*X[t-1] + b2*X[t-2]
    Y[t] = (rhs - a1*Y[t-1] - a2*Y[t-2]) / a0

# plt.plot(X, label = 'Original Data')
plt.plot(Y, label = 'Filtered Data')
plt.ylim(-2, 2)
# plt.legend()
plt.show()