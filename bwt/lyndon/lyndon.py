def longest_lyndon_prefix(w):
    """
    Returns the tuple of the longest lyndon prefix length and the number of repitition for the string w.

    Examples:
        abbaa -> Returns (3, 1)
        abbabb -> Returns (3, 2)
    """
    i = 0
    j = 1
    while j < len(w) and w[i] <= w[j]:
        if w[i] == w[j]:
            i += 1
            j += 1
        else:
            i = 0
            j += 1
    return j - i, j // (j - i)


def is_lyndon(w):
    """Returns true iff the string w is the lyndon word"""
    return longest_lyndon_prefix(w)[0] == len(w)


def lyndon_break_points(w):
    """Returns lyndon breakpoints sequence of the string w"""
    start = 0
    while start < len(w):
        pref, rep = longest_lyndon_prefix(w[start:])
        for _ in range(rep):
            start += pref
            yield start


def lyndon_factorize(w):
    """
    Returns lyndon factorization sequence of the string w

    Examples:
        abbaba -> abb, ab, a
    """
    start = 0
    for bp in lyndon_break_points(w):
        yield w[start: bp]
        start = bp
