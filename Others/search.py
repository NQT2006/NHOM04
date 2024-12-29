from Others.student_input_test import strip

def someValue(f, l: list):
    for v in l:
        if f(v): return True
    return False

def ss(v, k, t):
    if k[0] not in ['*', '<', '=', '>']: k = '=='+k
    if t:
        if not k[2:].replace('.','',1).isdigit(): return False
        v = float(v)
    else:
        v = v.lower()
        k = k.lower()
    s = None
    d = k[:2]
    if not t and k[0] == '*': s = lambda a, b: a.endswith(b[1:])
    elif d == '==': s = lambda a, b: a == (float(b[2:]) if t else b[2:])
    elif d == '<<': s = lambda a, b: a < (float(b[2:]) if t else b[2:])
    elif d == '<=': s = lambda a, b: a <= (float(b[2:]) if t else b[2:])
    elif d == '>>': s = lambda a, b: a > (float(b[2:]) if t else b[2:])
    elif d == '>=': s = lambda a, b: a >= (float(b[2:]) if t else b[2:])
    elif not t and k[-1] == '*': s = lambda a, b: a.startswith(b[2:-1])

    return s(v, k)

def ValueSearch(data: list[str], index: int, keywords: list[str], dt: list):
    result = list(filter(lambda d: someValue(lambda k: ss(d[index], strip(k), dt[index]), keywords), data[1:]))
    result.sort(key=lambda d: d[index])
    return [data[0]] + result