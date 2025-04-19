import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('Data\project_data.txt', dtype=float)

plt.plot(data, label = 'Original Data')
plt.show()

