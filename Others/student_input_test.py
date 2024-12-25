from datetime import datetime
from Others.class_input_test import strip

def MaHocSinh(x):
    if not x: raise Exception('Chưa nhập mã học sinh')
    x = strip(x)
    if len(x) != 10: raise Exception('Mã học sinh phải có 10 kí tự')
    return x

def HoTen(x):
    if not x: raise Exception('Chưa nhập họ và tên')
    x = strip(x)
    if len(x) > 50: raise Exception('Họ và tên phải ít hơn 50 kí tự')
    x = x.split(' ')
    if (len(x) == 1): raise Exception('Phải nhập đầy đủ học và tên')
    return [' '.join(x[:-1]), x[-1]]

def Tuoi(x):
    if not x: raise Exception('Chưa nhập tuổi')
    x = strip(x)
    if not x.isnumeric(): raise Exception('Tuổi phải là số nguyên dương')
    else: return x

def NgaySinh(x):
    if not x: raise Exception('Chưa nhập ngày sinh')
    x = strip(x)
    try: datetime(*map(lambda x: int(x), x.split('-')))
    except: raise Exception('Ngày sinh không hợp lệ')
    return list(map(lambda x: ('0'+x) if len(x) == 1 else x , x.split('-')))

def SoDienThoai(x):
    if not x: raise Exception('Chưa nhập số điện thoại')
    x = strip(x)
    if not x.isnumeric(): raise Exception('Số điện thoại chỉ gồm số')
    elif len(x) != 10: raise Exception('Số điện thoại phải có 10 số')
    else: return x

def MaLop(x):
    if not x: raise Exception('Chưa nhập mã lớp')
    x = strip(x)
    if len(x) > 50: raise Exception('Mã lớp phải có 10 kí tự')
    return x

def TinhTuoi(nam: str|int, thang: int, ngay: int):
    NAM = datetime.now().year
    if NAM - 10 < nam: raise Exception('Năm sinh quá nhỏ')
    THANG = datetime.now().month
    NGAY = datetime.now().day
    if THANG > int(thang) or (THANG == int(thang) and NGAY >= int(ngay)):
        return NAM - int(nam) - 1
    return NAM - int(nam)