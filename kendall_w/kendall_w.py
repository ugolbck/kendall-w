import warnings

def compute_w(arr):
    """ Computes kendall's W from a list of rating lists
    Arguments.
    0 indicates no agreement and 1 indicates unanimous agreement.
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
    assert isinstance(arr[0], list), "You must pass a list of python list, {} found".format(type(arr[0]))

    # Number of annotators
    m = len(arr[0])
    if m <= 2:
        warnings.warn("Kendall's W is adapted to the agreement measurement between more than two annotators. See Kendall's tau for more information")
    
    # Number of items
    n = len(arr)
    assert n > 1, "Kendall's W is irrevelent for only one item, try adding more sublists to argument 'arr'."

    # Compute sum of each item ranks
    sums = [sum(x) for x in arr]

    Rbar = sum(sums) / n
    S = sum([(sums[x] - Rbar) ** 2 for x in range(n)])
    W = (12 * S) / (m ** 2 * (n ** 3 - n))

    return W