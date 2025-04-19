import numpy as np
import matplotlib.pyplot as plt

# Question 1
beta = lambda w: 0.0024 + 0.0032*np.cos(w) + 0.0008*np.cos(2*w)
alpha = lambda w: 3.846321 - 5.12008*np.cos(w) + 1.28*np.cos(2*w)

w = np.linspace(0, np.pi, 200)
T = beta(w) / alpha(w)
plt.plot(w, T, label = 'Transfer Function')
plt.show()

# Question 2
beta = lambda w: 0.057624 - 0.076832*np.cos(w) + 0.019208*np.cos(2*w)
alpha = lambda w: 2.000738 + 2.50604*np.cos(w) + 0.666*np.cos(2*w)

w = np.linspace(0.1, np.pi, 100)
T = beta(w) / alpha(w)
plt.plot(w, T, label = 'Transfer Function')
plt.show()

# Question 3
beta = lambda w: 0.12005 - 0.12005*np.cos(2*w)
alpha = lambda w: 1.628549 - 1.83214*np.cos(w) + 1.02*np.cos(2*w)

w = np.linspace(0, np.pi, 200)
T = beta(w) / alpha(w)
plt.plot(w, T, label = 'Transfer Function')
plt.show()

# # Question 4
beta = lambda w: 2.465851 + 3.4683*np.cos(w) + 1.36125*np.cos(2*w)
alpha = lambda w: 2.525802 + 3.466298*np.cos(w) + 1.298*np.cos(2*w)

w = np.linspace(0, np.pi, 200)
T = beta(w) / alpha(w)
plt.plot(w, T, label = 'Transfer Function')
plt.show()