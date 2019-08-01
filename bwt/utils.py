def cyclic_group(w):
    for i in range(len(w)):
        yield w
        w = w[-1] + w[:-1]
