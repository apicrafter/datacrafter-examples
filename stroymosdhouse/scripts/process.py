def process(obj):
    obj['latitude'], obj['longitude'] = obj['coords'].strip(']').strip('[').split(',')
    obj['longitude'] = float(obj['longitude'].strip())
    obj['latitude'] = float(obj['latitude'])
    del obj['coords']
    return obj