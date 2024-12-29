from Class.document import Read, Write, GetOptions
from Students.document import Read as ReadStudents
from Others.style import clr, cls, bold

MODE = {
    'exit': ['c-m', None],
    'f1':   ['c-l', None],
    'f2':   ['c-a', None],
    'f3':   ['c-u', None],
    'f5':   ['c-s', None]
}

def remove(data: list, ucl: list):
    dsml = [l[0] for l in data]
    maLop = GetOptions(data, 0, True, 'những lớp cần xóa (Cách nhau bằng "dấu cách"): ', 1, '    ')
    for lop in maLop.copy():
        if lop not in maLop:
            maLop.remove(lop)
            continue
        if lop in ucl: raise Exception('Không thể xóa lớp đang có học sinh')
        index = dsml.index(lop)
        data = data[:index] + data[index+1:]
    if not len(maLop): raise Exception('Không tìm thấy lớp nào')
    Write(data)
    print(clr(f'[-] Xóa thành công lớp {', '.join(maLop)}\n', 'success'))
    return data

def RemoveAction(maLop):
    title = bold('[4] Xóa bỏ thông tin lớp')
    cls(title)
    data = Read()
    ucl = {l[6] for l in ReadStudents()}
    while True:
        try:
            data = remove(data, ucl)
        except KeyboardInterrupt:
            return MODE['exit']
        except Exception as e:
            print(clr(' \u2716   Xóa không thành công: ' + str(e) + '\n', 'fail'))

#
'''def RemoveAction(maLop):
    cls(bold('[4] Xóa bỏ thông tin lớp'))
    options = {
        'f1': 'Tra cứu', 'f2': 'Thêm mới', 'f3': 'Chỉnh sửa',
        'f5': 'Tìm kiếm', 'ctrl + c': 'Trở về Menu'
    }
    pp = list(map(lambda k: '    ' + option(k, options[k]), options))
    print('   '.join(pp))
    while True:
        try:
            maLop = KiemTra.MaLop(input('[?] Nhập mã lớp cần xóa: '))
            if maLop in MODE: return MODE[maLop]
            data = Read()
            dsml = [l[0] for l in data]
            if not maLop in dsml: raise Exception(f'Mã lớp {maLop} không tồn tại')
            else:
                ds = {l[6] for l in ReadStudents()}
                if maLop in ds: raise Exception('Không thể xóa lớp đang có học sinh')
            index = dsml.index(maLop)
            newData = data[:index] + data[index+1:]
            Write(newData)
            print(clr(f'[-] Xóa thành công lớp {maLop}\n', 'success'))
        except KeyboardInterrupt:
            return MODE['exit']
        except Exception as e:
            print(clr('[!] Xóa không thành công: ' + str(e) + '\n', 'fail'))'''