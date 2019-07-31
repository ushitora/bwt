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


def bwt_verbose(w):
    s = [(w*2)[i:i + len(w)] for i in range(len(w))]
    print('Cyclic strings')
    print('\n'.join(['  ' + si for si in s]))
    s = sorted(s)
    print('Sort cyclic strings')
    print('\n'.join(['  ' + si for si in s]))
    return "".join([v[-1] for v in s]), s.index(w)