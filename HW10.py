import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, np.pi, 200)

# Question 1
y = (1 / (2*np.pi)) * 0.51 / (1.49 - 1.4*np.cos(x))

plt.plot(x, y)
plt.xlabel('Frequency')
plt.ylabel('Spectrum')
plt.show()

# Question 2
y = (1 / (2*np.pi)) * (1 + 0.81 + 1.8*np.cos(x)) / (1 + 0.81 - 1.8*np.cos(x))

plt.plot(x, y)
plt.xlabel('Frequency')
plt.ylabel('Spectrum')
plt.show()

# Question 3
y = (1 / (2*np.pi)) / (3.2581 - 4.482*np.cos(x) + 1.32*np.cos(2*x))

plt.plot(x, y)
plt.xlabel('Frequency')
plt.ylabel('Spectrum')
plt.show()

# Question 4
y = (1 / (2*np.pi)) / (1.3816 - 0.276*np.cos(x) - 1.08*np.cos(2*x))

plt.plot(x, y)
plt.xlabel('Frequency')
plt.ylabel('Spectrum')
plt.show()

# Question 5
y = (1 / (2*np.pi)) / (1.8125 + 0.01*np.cos(x) - 1.8*np.cos(2*x))

plt.plot(x, y)
plt.xlabel('Frequency')
plt.ylabel('Spectrum')
plt.show()

# Question 6
y = (1 / (2*np.pi)) / (4.4436 - 6.208*np.cos(x) + 1.88*np.cos(2*x))

plt.plot(x, y)
plt.xlabel('Frequency')
plt.ylabel('Spectrum')
plt.show()

# Question 7
y = (1 / (2*np.pi)) * (5.5125 - 7.41*np.cos(x) + 1.9*np.cos(2*x)) / (4.53 - 6.12*np.cos(x) + 1.6*np.cos(2*x))

plt.plot(x, y)
plt.xlabel('Frequency')
plt.ylabel('Spectrum')
plt.show()
