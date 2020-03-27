def kendall_w(arr):
    """ Computes kendall's W from a list of rating lists
    Arguments
    ---------

    arr : list
        List of list with shape (n_items * n_annotators)

    Return
    ---------

    W : float
        Kendall's W [0:1] 
    """

    m = len(arr[0])
    n = len(arr)

    sums = [sum(x) for x in arr]
    print('sums', sums)
    Rbar = sum(sums) / len(arr)
    print('Rbar', Rbar)
    S = sum([(sums[x] - Rbar) ** 2 for x in range(len(sums))])
    print('S', S)
    W = (12 * S) / (m ** 2 * (n ** 3 - n))
    print('W', W)

# alte = [[2,2,2,2], [3,3,3,3], [4,4,4,4]]
# kendall_w(alte)