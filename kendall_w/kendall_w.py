# TODO:
# - Perform series of tests to make compute_w robust
# - Add possibility to compute from pd.DataFrame:
#       - Separate function that allows a DataFrame
#       - Force DataFrame in args[0] of compute_w
#       - Check type of args[0] of compute_w and convert DataFrame to matrix
#       - Check type of args[0] of compute_w and write additionnal code adapted to pandas.DataFrame
# - Check that all elements of args[0] are lists and all elements of sublists are integers:
#       -> Exception
# - Check that items are RANKED for each annotator:
#       -> Exception or Warning ?


import warnings

def compute_w(arr):
    """ Computes kendall's W from a list of rating lists.
    0 indicates no agreement and 1 indicates unanimous agreement.
    
    Arguments
    ---------

    arr : list
        List of lists with shape (n_items * n_annotators)

    Return
    ---------

    W : float
        Kendall's W [0:1]
    
    Example
    ---------

    annotations = [
        [1, 1, 1, 2], # item 1
        [2, 2, 2, 3], # item 2
        [3, 3, 3, 1], # item 3
    ]
    # Annotator #4 disagrees with the other annotators
    # Annotators #1, #2, #3 agree

    W = kendall_w(annotations)
    # output: 0.4375
    """
    
    assert isinstance(arr, list), "You must pass a python list, {} found".format(type(arr))
    assert all(isinstance(x, list) for x in arr), "You must pass a list of python lists as input." # To test
    assert all(isinstance(x[y], int) for x in arr for y in range(len(x))), "You must pass a list of integer lists." # To test

    # Number of annotators
    m = len(arr[0])
    if m <= 2:
        warnings.warn("Kendall's W is adapted to measure agreement between more than two annotators. The results might not be reliable in this case.")
    
    # Number of items
    n = len(arr)
    assert n > 1, "Kendall's W is irrevelent for only one item, try adding more sublists to argument 'arr'."

    # Sum of each item ranks
    sums = [sum(x) for x in arr]
    # Mean of ranking sums
    Rbar = sum(sums) / n
    # Sum of squared deviations from the mean
    S = sum([(sums[x] - Rbar) ** 2 for x in range(n)])

    W = (12 * S) / (m ** 2 * (n ** 3 - n))

    return W