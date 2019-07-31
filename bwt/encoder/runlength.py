
def runlength_encode(w, b=False):
    """
    Returns the runlength encoded string of the string w.

    Arguments and keyword arguments:
        w -- Original string
        b -- If true, returns bytes (default: False)
    """
    last = ''
    count = 0
    encoded = []

    def push():
        nonlocal count
        while(count > 0):
            use = min(255, count)
            encoded.append(use)
            encoded.append(last)
            count -= use

    for wi in w:
        if wi != last:
            if count > 0:
                push()
            count = 1
        else:
            count += 1
        last = wi
    push()
    if b:
        encoded = bytes([ei if type(ei) == int else ord(ei) for ei in encoded])
    return encoded
