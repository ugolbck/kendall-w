def conv_W(df, n, m):
    scores = []
    for i in range(df.shape[0]-(n-1)):
        for j in range(df.shape[1]-(m-1)):
            window = df.iloc[i:i+n, j:j+m]
            window['sum'] = [sum(window.iloc[k, :]) for k in range(window.shape[0])]
            Rbar = window.loc[:, 'sum'].mean(axis=0)
            S = sum([math.pow(window.iloc[l, -1] - Rbar, 2) for l in range(len(window['sum']))])
            W = (12 * S) / (math.pow(m,2) * (math.pow(n, 3) - n))
            print(W)
            scores.append(W)
    print('-----')
    conv_score = sum(scores)/len(scores)
    return conv_score, m * (n-1) * conv_score

def kendall_w(arr):

    m = len(arr[0])
    n = len(arr)

    sums = [sum(x) for x in arr]
    print(sums)
    Rbar = sum(sums) / len(arr)
    S = sum([(sums[x] - Rbar)**2 for x in range(len(sums))])
    W = (12 * S) / (m ** 2 * (n ** 3 - n))
    print(W)

# alte = [[2,2,2,2], [3,3,3,3], [4,4,4,4]]
# kendall_w(alte)