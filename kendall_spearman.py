import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('Final_Exam\Q4_data.txt', dtype = float)
n = len(data)

var_T = 2*(2*n + 5) / (9*n**2 - 9*n)

K = 0
for i in range(n):
    x_i = data[i]
    for j in range(i + 1, n):
        x_j = data[j]
        if x_i < x_j:
            K += 1
        elif x_i == x_j:
            K += 0.5

kend_coeff =  4*K / (n**2 - n) - 1
print(f'The Kendall coefficient (T) is {kend_coeff:.4f}')
print(f'At 5% level of significance T / var_T^(1/2) = {kend_coeff / np.sqrt(var_T):.4f} which is less than 1.96 so the test returns negative.')

var_S = 1 / n
ranks = []

for x in data:
    indices = [i for i, val in enumerate(sorted(data)) if val == x]
    avg_rank = sum(i + 1 for i in indices) / len(indices)  # Average rank for ties
    ranks.append(avg_rank)

d_squared_sum = sum((r - (i + 1))**2 for i, r in enumerate(ranks))
spear_coeff = 1 - (6 * d_squared_sum) / (n * (n**2 - 1))
print(f'The Spearman Rank correlation is {spear_coeff:.4f}')
print(f'At 5% level of significance S / var_S^(1/2) = {spear_coeff / np.sqrt(var_S):.4f} which is greater than 1.96 so the test returns positive.')