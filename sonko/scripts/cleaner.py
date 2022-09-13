def process(r):
    for k in r.keys():
        if r[k] and isinstance(r[k], str):
            r[k] = r[k].strip()
    return r