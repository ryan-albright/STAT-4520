import numpy as np
import matplotlib.pyplot as plt

# Question 1.1.2.5
def driver_1(part = 'all'):
    data = np.array([8.6739477736341,	7.32941581613292,	6.85347437257891,	7.73104723839682,	7.08595340132114,	5.9121348183291,	5.71035699165132,	6.39769108041147,	5.09135671911971,	3.83318033824577,	4.6321002310859,	4.72521025204203,	4.1600127784735,	3.4575597957603,	2.65730123978381,	2.9389058770241,	3.37281537249588,	4.45219878107514,	3.47930974184288,	5.12180643492648,	4.48771929671481,	4.83634213422479,	20.6144776784077,	5.55541841674259,	6.82835244347364,	6.34550860546533,	-0.78682331970222,	8.2634347643117,	7.90359247942296,	7.96273668022748,	6.6534336601849,	8.02688591760068,	7.82234803810664,	7.45197735797292,	7.78072259957531,	6.89419805491178,	7.55785050379655,	6.436439266567,	6.50058729355999,	5.72307786123133,	24.5885810442768,	5.45486840907091,	6.56191364621257,	5.52867117091127,	6.23489527209597,	6.28538292786205,	6.48764320820407,	6.36467900015359,	6.9993303272327,	7.78884506251896,	8.01191503816807,	8.77146703930671,	8.54476554543156,	8.82067339085284,	9.64838616434454,	9.93651743982284,	17.5402026449148,	3.54091288253641,	9.58012915095719,	10.8435445829426,	11.1561606075999,	11.0324069505427,	10.4307409816417,	10.414648082791,	9.04505998785268,	8.4116905167418,	7.4806207996167,	26.5409128825364,	7.48744382815361,	6.59267383439759,	5.36356224397378,	6.16309824253722,	5.72159242909306,	5.766048185178,	5.4225546850315,	6.06331041957025,	5.47856598605704,	5.84660723435887,	7.13549280916258,	7.16628130415842,	8.34404497076416,	8.30719166636838,	8.23488361790501,	9.71303619040266,	10.3020020951636,	10.5389888253983,	10.4692400707525,	10.9576486609834,	11.4975043585211,	11.6463691470284])

    l = 15
    N = len(data)

    if part == 'a':
        a_tilde = np.empty(N - 2*l)
        # We effectively want to have a window of of 31 points as we loop through the data
        for i in range(l, N - l): # we need l points before and after the current point
            a_tilde[i - l] = sum(data[i-l:i+l+1]) / (2*l + 1)

        x1 = np.array([i for i in range(1, N + 1)])
        x2 = np.array([i for i in range(l, N - l)])

        plt.plot(x1, data, label = 'Data')
        plt.plot(x2, a_tilde, label = '1st Order Moving Average')
        plt.legend()
        plt.show()
    elif part == 'b':
        a_tilde = np.empty(N - 2*l - 8)
        # We saw a couple outliers in the prior data set, so we can use the 53X method to eliminate their effects
        Xt = []
        # creation of Xt (median based on window of 5)
        for i in range(2, N - 2):
            Xt.append(np.median(data[i - 2: i + 2 + 1]))
        Yt = []
        # creation of Yt (median based on window of 3)
        for i in range(1, N - 5):
            Yt.append(np.median(Xt[i - 1: i + 1 + 1]))
        Zt = []
        for i in range(1, N - 7):
            z = sorted(Yt[i - 1: i + 1 + 1])
            Zt.append(z[0]*0.25 + z[1]*0.5 + z[2]*0.25)

        Zt = np.array(Zt)
        # We effectively want to have a window of of 31 points as we loop through the data
        for i in range(l, N - l - 8): # we need l points before and after the current point
            a_tilde[i - l] = sum(Zt[i-l:i+l+1]) / (2*l + 1)

        x1 = np.array([i for i in range(1, N + 1)])
        x2 = np.array([i for i in range(1 + 4, N + 1 - 4)])
        x3 = np.array([i for i in range(l,N - l - 8)])
        
        plt.plot(x1, data, label = 'Data')
        plt.plot(x2, Zt, label = 'Data after 53X Procedure')
        plt.plot(x3, a_tilde, label = '1st Order Moving Average')
        plt.legend()
        plt.show()
    else:
        a_tilde_a = np.empty(N - 2*l)
        # We effectively want to have a window of of 31 points as we loop through the data
        for i in range(l, N - l): # we need l points before and after the current point
            a_tilde_a[i - l] = sum(data[i-l:i+l+1]) / (2*l + 1)

        a_tilde_b = np.empty(N - 2*l - 8)
        # We saw a couple outliers in the prior data set, so we can use the 53X method to eliminate their effects
        
        # creation of Xt (median based on window of 5)
        Xt = []
        for i in range(2, N - 2):
            Xt.append(np.median(data[i - 2: i + 2 + 1]))

        # creation of Yt (median based on window of 3)        
        Yt = []
        for i in range(1, N - 5):
            Yt.append(np.median(Xt[i - 1: i + 1 + 1]))
        
        # creation of Zt (weighted average between the three values)
        Zt = []
        for i in range(1, N - 7):
            z = sorted(Yt[i - 1: i + 1 + 1])
            Zt.append(z[0]*0.25 + z[1]*0.5 + z[2]*0.25)

        Zt = np.array(Zt)
        for i in range(l, N - l - 8): # we need l points before and after the current point
            a_tilde_b[i - l] = sum(Zt[i-l:i+l+1]) / (2*l + 1)

        x1 = np.array([i for i in range(1, N + 1)])
        x2 = np.array([i for i in range(1 + 4, N + 1 - 4)])
        x3 = np.array([i for i in range(l, N - l)])
        x4 = np.array([i for i in range(l + 4,N - l - 4)])
        
        plt.plot(x1, data, label = 'Data')
        plt.plot(x2, Zt, label = 'Data after 53X Procedure')
        plt.plot(x3, a_tilde_a, label = '1st Order Moving Average')
        plt.plot(x4, a_tilde_b, label = '1st Order Moving Average from 53X')
        plt.legend()
        plt.show()

# driver_1()

# Question 1.1.3.4
def driver_2():
    data = np.array([10.2436854823499,	9.78168365921842,	8.88631001778969,	8.30873696448217,	9.6789698374961,	8.52462354399394,	8.49040393774566,	9.05917728066278,	9.42504548952814,	7.47020951348205,	9.36193965243921,	10.4966026536653,	8.8366007645583,	9.59029630878452,	9.40715611083808,	7.44893350344503,	7.66538644781101,	6.56713062760779,	6.29630344064784,	5.03954635277918,	5.08898580038775,	4.60612131906525,	3.99162659018348,	5.20997179329743,	6.43723033850951,	5.9713041051224,	7.10337265154697,	7.68306821353612,	6.60363986981335,	8.37533124791158,	8.56235752902047,	7.16973887510893,	7.91262121142034,	5.93985634036995,	4.67596978362886])

    alpha = 0.1
    N = len(data)

    # zero order
    X_n_0 = np.empty(N)
    X_n_0[0] = a_hat_0 = data[0]
    for i in range(1, N):
        e_n = data[i] - X_n_0[i - 1]
        a_hat_0 = a_hat_0 + alpha*e_n
        X_n_0[i] = a_hat_0
    
    # first order
    X_n_1 = np.empty(N)
    a_hat_1 = data[0]
    b_hat_1 = 0
    X_n_1[0] = a_hat_1 + b_hat_1
    for i in range(1, N):
        e_n = data[i] - a_hat_1 - b_hat_1
        a_hat_1 = a_hat_1 + b_hat_1 +(2*alpha - alpha**2)*e_n
        b_hat_1 = b_hat_1 + alpha**2*e_n
        X_n_1[i] = a_hat_1 + b_hat_1

    # second order
    X_n_2 = np.empty(N)
    a_hat_2 = data[0]
    b_hat_2 = 0
    c_hat_2 = 0
    X_n_2[0] = a_hat_2 + b_hat_2 + c_hat_2
    for i in range(1, N):
        e_n = data[i] - a_hat_2 - b_hat_2 - c_hat_2
        a_hat_2 = a_hat_2 + b_hat_2 + c_hat_2 + alpha*(3 - 3*alpha - alpha**2)*e_n
        b_hat_2 = b_hat_2 + 2*c_hat_2 + 3*alpha**2*(1 - alpha/2)*e_n
        c_hat_2 = c_hat_2 + 0.5*alpha**3*e_n
        X_n_2[i] = a_hat_2 + b_hat_2 + c_hat_2

    x1 = np.array([i for i in range(1, N + 1)])
    x2 = np.array([i for i in range(2, N + 2)])

    plt.plot(x1, data, label = 'Data')
    plt.plot(x2, X_n_0, label = 'Zero Order Exponential Smoothing')
    plt.plot(x2, X_n_1, label = 'First Order Exponential Smoothing')
    plt.plot(x2, X_n_2, label = 'Second Order Exponential Smoothing')
    plt.legend()
    plt.show()

driver_2()

# Question 1.1.4.3
def driver_3():
    data = [305, 286, 325, 306, 307, 316, 322, 328, 304, 310, 328, 300, 286, 310, 337, 362, 374, 356, 356, 322]

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
    print(f'The Kendall coefficient (T) is {kend_coeff}')
    print(f'At 5% level of significance T / var_T^(1/2) = {kend_coeff / np.sqrt(var_T):4f} which is greater than 1.96 so the test returns positive.')

    var_S = 1 / n
    ranks = []
    
    for x in data:
        indices = [i for i, val in enumerate(sorted(data)) if val == x]
        avg_rank = sum(i + 1 for i in indices) / len(indices)  # Average rank for ties
        ranks.append(avg_rank)

    d_squared_sum = sum((r - (i + 1))**2 for i, r in enumerate(ranks))
    spear_coeff = 1 - (6 * d_squared_sum) / (n * (n**2 - 1))
    print(f'The Spearman Rank correlation is {spear_coeff:2f}')
    print(f'At 5% level of significance T / var_S^(1/2) = {spear_coeff / np.sqrt(var_S):4f} which is greater than 1.96 so the test returns positive.')
    
    plt.plot(data)
    plt.show()
# driver_3()