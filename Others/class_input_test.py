KEY = ['f1', 'f2', 'f3', 'f4', 'f5', 'exit']

def strip(text: str):
    i = text.find('  ')
    while i != -1:
        text = text[:i] + text[i+2:]
        i = text.find('  ')
    return text.strip()

def MaLop(x):
    if not x: raise Exception('Chưa nhập mã lớp')
    elif x.lower() in KEY: return x.lower()
    x = strip(x)
    if len(x) == 10: return x
    else: raise Exception('Mã lớp không hợp lệ, phải có 10 kí tự')

def TenLop(x):
    if not x: raise Exception('Chưa nhập tên lớp')
    elif x in KEY: return x
    x = strip(x)
    if len(x) < 10: raise Exception('Tên lớp không hợp lệ, ít hơn 10 kí tự')
    elif len(x) <= 20: return x
    else: raise Exception('Tên lớp không hợp lệ, vượt quá 20 kí tự')

def TongSoBan(x):
    if not x: return 0
    elif x in KEY: return x
    x = strip(x)
    if not x.isnumeric(): raise Exception('Tổng số bàn phải là số nguyên')
    elif int(x) > 40: raise Exception('Tổng số bàn không được lớn hơn 40')
    else: return x
