from datetime import strptime
def _enrich_data(obj):
    obj = obj['vacancy']
    for k in ['@about', '@typeof']:
        if k in obj.keys():
            del obj[k]
    for k in ['profession', 'region', 'industry', 'organization']:
        if k in obj.keys():
            obj[k] = obj[k]['@resource'].rsplit('#')[-1]

    for k in ['title', 'responsibilities', 'datePosted']:
        if k in obj.keys():
            obj[k] = obj[k]['#text'].rsplit('#')[-1]

    for k in ['salaryMin', 'salaryMax']:
        if 'baseSalary' in obj.keys() and obj['baseSalary'] is not None:
            if k in obj['baseSalary'].keys():
                obj['baseSalary'][k] = float(obj['baseSalary'][k])

    for k in ['creationDate', ]:
        if k in obj.keys():
            obj[k] = strptime(obj[k], '%Y-%m-%d')

    if 'innerInfo' in obj.keys() and obj['innerInfo'] is not None:
        for k in ['dateModify', 'moderationTime']:
            if 'innerInfo' in obj.keys() and k in obj['innerInfo'].keys():
                obj['innerInfo'][k] = strptime(obj['innerInfo'][k], '%Y-%m-%d')
    return obj
