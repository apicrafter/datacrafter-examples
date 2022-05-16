KEYS = ['CN', 'C', 'S', 'L', 'O', 'E', 'ОГРН', 'ИНН', 'STREET']
def cert_to_dict(text):
    result = {}
    for k in KEYS:
        pos = text.find(k + '=')
        if pos > -1:
            result[k] = text[pos+len(k)+1:].split(',', 1)[0]
    return result


def process(obj):
    obj['certInfo']['issuerdata'] = cert_to_dict(obj['certInfo']['issuer'])
    obj['certInfo']['subjectdata'] = cert_to_dict(obj['certInfo']['subject'])
    return obj