def bwt(w):
    """
    Returns Bullows-Wheeler Transform of the string w.

    Return value will be the tuple of the transformed string and the starting index.

    NOTE: This is not O(n) implementation.
    """
    s = sorted([(w*2)[i:i + len(w)] for i in range(len(w))])
    return "".join([v[-1] for v in s]), s.index(w)


def bwt_inv(l, index):
    """
    Inverse tranform of bwt()
    
    Arguments:
        l -- Transformed string
        index -- Starting index
    """
    raise NotImplementedError()
