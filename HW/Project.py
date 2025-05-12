import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('Data/project_data.txt', dtype=float)

def low_pass_filter(X, w_0):
    A = np.tan(w_0 / 2)

    b0 = A**2
    b1 = 2*A**2
    b2 = A**2

    a0 = 1 + np.sqrt(2)*A + A**2
    a1 = -2*(1 - A**2)
    a2 = 1 - np.sqrt(2)*A + A**2

    Y = np.zeros(X.size)

    for t in range(2, X.size):
        rhs = b0 *X[t] + b1*X[t-1] + b2*X[t-2]
        Y[t] = (rhs - a1*Y[t-1] - a2*Y[t-2]) / a0

    return Y
    
def high_pass_filter(X, w_0):
    C = 1 / np.tan(w_0 / 2)

    b0 = C**2
    b1 = -2*C**2
    b2 = C**2

    a0 = 1 + np.sqrt(2)*C + C**2
    a1 = -2*(C**2 - 1)
    a2 = 1 - np.sqrt(2)*C + C**2

    Y = np.zeros(X.size)

    for t in range(2, X.size):
        rhs = b0 *X[t] + b1*X[t-1] + b2*X[t-2]
        Y[t] = (rhs - a1*Y[t-1] - a2*Y[t-2]) / a0

    return Y

def band_pass_filter(X, w_0, B):
    D = np.cos(w_0) / np.cos(B)
    E = np.tan(B)

    b0 = E
    b2 = -E

    a0 = E + 1
    a1 = -2*D
    a2 = 1 - E

    Y = np.zeros(X.size)

    for t in range(2, X.size):
        rhs = b0 *X[t] + b2*X[t-2]
        Y[t] = (rhs - a1*Y[t-1] - a2*Y[t-2]) / a0

    return Y
    
def band_reject_filter(X, w_0, B):
    D = np.cos(w_0) / np.cos(B)
    E = np.tan(B)

    b0 = 1
    b1 = -2*D
    b2 = 1

    a0 = E + 1
    a1 = -2*D
    a2 = 1 - E

    Y = np.zeros(X.size)

    for t in range(2, X.size):
        rhs = b0 *X[t] + b1*X[t-1] + b2*X[t-2]
        Y[t] = (rhs - a1*Y[t-1] - a2*Y[t-2]) / a0

    return Y

def trunc_periodogram(M):
    N = len(data)
    mu_x = np.mean(data)

    freq = np.linspace(0, np.pi, 200)

    R = np.empty(N-1)
    for k in range(N-1):
        R[k] = (1/N)*sum((data[:N-k] - mu_x)*(data[k:] - mu_x))

    f = (1 / (2 * np.pi)) * np.array([R[0] + 2 * np.sum([R[k] * np.cos(w * k) for k in range(1, M + 1)]) for w in freq])
    plt.plot(freq, f)
    plt.xlabel('Frequency')
    plt.ylabel('Spectrum')
    plt.show()
  
def driver(w_0, B = None, type = 'Low Pass', second_pass = False, show_orig = True):
    X = data
    X_prime = np.flip(X)
    if show_orig:
        plt.plot(X, label = 'Original Data')

    if type == 'Low Pass':
        print('Second Order Low Pass Filter Applied')
        Y = low_pass_filter(X, w_0)
        if second_pass:
            Y1 = low_pass_filter(X_prime, w_0)[::-1]
            Y = (Y + Y1) / 2

    elif type == 'High Pass':
        print('Second Order High Pass Filter Applied')
        Y = high_pass_filter(X, w_0)
        if second_pass:
            Y1 = high_pass_filter(X_prime, w_0)[::-1]
            Y = (Y + Y1) / 2

    elif type == 'Band Pass':
        print('Second Order Band Pass Filter Applied')
        Y = band_pass_filter(X, w_0, B)
        if second_pass:
            Y1 = band_pass_filter(X_prime, w_0, B)[::-1]
            Y = (Y + Y1) / 2

    elif type == 'Band Reject':
        print('Second Order Band Reject Filter Applied')
        Y = band_reject_filter(X, w_0, B)
        if second_pass:
            Y1 = band_reject_filter(X_prime, w_0, B)[::-1]
            Y = (Y + Y1) / 2

    plt.plot(Y, label = 'Filtered Data')
    if show_orig:
        plt.legend()
    plt.show()

# driver(29 * np.pi / 30, type = 'High Pass', show_orig = False, second_pass= True)

# driver(np.pi / 60, type = 'Low Pass', show_orig = False, second_pass= True)

# driver(np.pi / 3, B = np.pi / 60, type = 'Band Pass', show_orig = False, second_pass= True)
# driver(np.pi / 2, B = np.pi / 60, type = 'Band Pass', show_orig = False, second_pass= True)
# driver(np.pi / 6, B = np.pi / 60, type = 'Band Pass', show_orig = False, second_pass= True)
# driver(np.pi / 1.7, B = np.pi / 60, type = 'Band Pass', show_orig = False, second_pass= True)
# driver(np.pi / 1.5, B = np.pi / 60, type = 'Band Pass', show_orig = False, second_pass= True)
driver(np.pi / 1.34, B = np.pi / 60, type = 'Band Pass', show_orig = False, second_pass= True)

# trunc_periodogram(200)