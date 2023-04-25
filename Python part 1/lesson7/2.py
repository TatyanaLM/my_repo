
d = {1: 'a', 2: 'b'}
def update_dictionary(d, key, value):
    if key in d.keys():
        d[key].append(value)
    else:
        if 2*key  in d.keys():
            d[2*key].append(value)
        else:
            d[2 * key] = [value]
    return d


print(update_dictionary(d, 3, "F"))