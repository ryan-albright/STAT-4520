import numpy as np
import matplotlib.pyplot as plt

def driver(part, dir):

    data = [-13.6370230118461,	6.3628727796189,	17.3826894982519,	-7.15165842046359,	-17.3689708890282,	16.4885052368306,	25.1857363884409,	-7.90132702142504,	2.83417658646008,	-16.5914716016542,	5.78399558126687,	-7.448339966683,	-3.76334890596327,	-4.39558303382188,	3.94867290401757,	33.9750146987563,	4.11262254945777,	16.5990660465274,	11.546474767198,	-10.0736601210488,	1.88727918898088,	16.5634777549087,	5.81313014031449,	-20.0725874538447,	-6.79252872816668,	20.0415429037837,	-9.32689287133895,	23.7627348202933,	-15.3197443380188,	11.3721303358535]

    n = len(data)
    
    if part == 'K':
        var_T = 2*(2*n + 5) / (9*n**2 - 9*n)
        sigma_T = np.sqrt(var_T)
        
        if dir == 'up':
            a = kend_coeff = 0
            while (kend_coeff / sigma_T) < 1.96:
                K = 0
                for i in range(n):
                    x_i = data[i] + a*(i + 1)
                    for j in range(i + 1, n):
                        x_j = data[j] + a*(j + 1)
                        if x_i < x_j:
                            K += 1
                        elif x_i == x_j:
                            K += 0.5
                
                a += 0.001
                kend_coeff =  4*K / (n**2 - n) - 1
                
            new_data = [a*(t + 1) + data_i for t, data_i in enumerate(data)]
            x = [i for i in range(1, n + 1)]
            print(f'The Kendall coefficient (T) is {kend_coeff:4f} and a is {a:.3f}')
            print(f'At 5% level of significance T / var_T^(1/2) = {kend_coeff / np.sqrt(var_T):.4f} which is absolutely greater than 1.96 so the test returns positive.')
            
            plt.plot(x, data, label = 'Original Data')
            plt.plot(x, new_data, label = f'Data with Upwards Trend (a = {a:.3f})')
            plt.legend()
            plt.plot()
            plt.show()

        elif dir == 'down':
            a = -0.89
            kend_coeff = 0
            while abs(kend_coeff / sigma_T) < 1.96:
                K = 0
                for i in range(n):
                    x_i = data[i] + a*(i + 1)
                    for j in range(i + 1, n):
                        x_j = data[j] + a*(j + 1)
                        if x_i < x_j:
                            K += 1
                        elif x_i == x_j:
                            K += 0.5
                a -= 0.001 
                kend_coeff =  4*K / (n**2 - n) - 1
                
            new_data = [a*(t + 1) + data_i for t, data_i in enumerate(data)]
            x = [i for i in range(1, n + 1)]
            print(f'The Kendall coefficient (T) is {kend_coeff:4f} and a is {a:.3f}')
            print(f'At 5% level of significance T / var_T^(1/2) = {kend_coeff / np.sqrt(var_T):.4f} which is absolutely greater than 1.96 so the test returns positive.')
            
            plt.plot(x, data, label = 'Original Data')
            plt.plot(x, new_data, label = f'Data with Downwards Trend (a = {a:.3f})')
            plt.legend()
            plt.plot()
            plt.show()

    elif part == 'S':
        var_S = 1 / n
        sigma_S = np.sqrt(var_S)
        
        if dir == 'up':
            a = 0.5
            spear_coeff = 0
            while abs(spear_coeff / sigma_S) < 1.96:
                ranks = []
                new_data = [a*(t + 1) + data_i for t, data_i in enumerate(data)]

                for x in new_data:
                    indices = [i for i, val in enumerate(sorted(new_data)) if val == x]
                    avg_rank = sum(i + 1 for i in indices) / len(indices)  # Average rank for ties
                    ranks.append(avg_rank)

                d_squared_sum = sum((r - (i + 1))**2 for i, r in enumerate(ranks))
                spear_coeff = 1 - (6 * d_squared_sum) / (n * (n**2 - 1)) 
                a += 0.001             
        
            x = [i for i in range(1, n + 1)]

            print(f'The Spearman Rank correlation is {spear_coeff:.4f} and a is {a:.3f}')
            print(f'At 5% level of significance T / var_S^(1/2) = {spear_coeff / sigma_S:4f} which is absolutely greater than 1.96 so the test returns positive.')

            plt.plot(x, data, label = 'Original Data')
            plt.plot(x, new_data, label = f'Data with Upwards Trend (a = {a:.3f})')
            plt.legend()
            plt.plot()
            plt.show()

        elif dir == 'down':
            a = 0
            spear_coeff = 0
            while abs(spear_coeff / sigma_S) < 1.96:
                ranks = []
                new_data = [a*(t + 1) + data_i for t, data_i in enumerate(data)]

                for x in new_data:
                    indices = [i for i, val in enumerate(sorted(new_data)) if val == x]
                    avg_rank = sum(i + 1 for i in indices) / len(indices)  # Average rank for ties
                    ranks.append(avg_rank)

                d_squared_sum = sum((r - (i + 1))**2 for i, r in enumerate(ranks))
                spear_coeff = 1 - (6 * d_squared_sum) / (n * (n**2 - 1)) 
                a -= 0.001                
                
            new_data = [a*(t + 1) + data_i for t, data_i in enumerate(data)]
            x = [i for i in range(1, n + 1)]
            
            print(f'The Spearman Rank correlation is {spear_coeff:.4f} and a is {a:.3f}')
            print(f'At 5% level of significance T / var_S^(1/2) = {spear_coeff / sigma_S:4f} which is absolutely greater than 1.96 so the test returns positive.')

            plt.plot(x, data, label = 'Original Data')
            plt.plot(x, new_data, label = f'Data with Downwards Trend (a = {a:.3f})')
            plt.legend()
            plt.plot()
            plt.show()

driver('S', 'up')