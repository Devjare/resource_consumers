sizes = {
        "KB": 1024,
        "MB": 1048576,
        "GB": 1073741824,
        "GB2": 2147483648,
        "GB3": 3221225472,
        "GB4": 4294967296,
        "GB5": 5368709120,
        "GB6": 6442450944,
        "GB9": 9663676416,
        "GB10": 10737418240,
        "GB15": 16106127360,
        "GB20": 21474836480,
        "GB10": 10737418240,
        "GB50": 53687091200
    }

def bytesto(_bytes, b_size=1024, round_to=2):
    """convert bytes to megabytes, etc.
       sample code:
           print('mb= ' + str(bytesto(314575262000000, 'm')))
       sample output: 
           mb= 300002347.946
    """
    _a = { 'K' : 1, 'M': 2, 'G' : 3, 'T' : 4, 'P' : 5, 'E' : 6 }

    _to = "K"
    if _bytes < sizes['MB']:
        _to = 'K'
    elif _bytes < sizes['GB']:
        _to = 'M'
    else:
        _to = 'G'

    _r = float(_bytes)
    for _i in range(_a[_to]):
        _r = _r / b_size

    return round(_r, round_to), _to
