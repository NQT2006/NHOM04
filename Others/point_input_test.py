from Others.student_input_test import MaHocSinh
from datetime import datetime

def MonHoc(x):
    if not x: raise Exception('Chưa nhập điểm')
    try: x = float(x.strip())
    except: raise Exception('Điểm phải là số thập phân')
    if not ( 0 <= x <= 10): raise Exception('Điểm phải nằm trong khoảng từ 0 đến 10')
    return str(round(x, 2))

def HocKi(x):
    if not x: raise Exception('Chưa nhập học kì')
    x = x.strip()
    if x in ['1', '2']: return x
    raise Exception('Học kì phải là 1 hoặc 2')

def NamHoc(x):
    if not x: raise Exception('Chưa nhập năm học')
    x = x.strip()
    if x.isnumeric() and 1000 < int(x) < datetime.now().year: return x
    raise Exception('Năm học không hợp lệ')

def MaHocKi(x):
    if not x: raise Exception('Chưa nhập mã học kì')
    return x.strip()
