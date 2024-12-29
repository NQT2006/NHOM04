from Points.document import Read, Write
from Students.document import Read as ReadStudentDocs, Write as WriteStudentDocs
from Points.lookup import lookup, joinData
from Others.style import clr, cls, bold, query1
import Others.student_input_test as KiemTra


def remove(data: list, output: str):
    sd = ReadStudentDocs()
    dshs = [d[0] for d in sd]
    maHocSinh = query1('những mã học sinh cần xóa (Cách nhau bằng "dấu cách")', 1).split(' ')
    for hs in maHocSinh.copy():
        try: hs = KiemTra.MaHocSinh(hs)
        except Exception as e: raise Exception(f'{str(e)} (Mã học sinh {hs})')
        if hs not in dshs: maHocSinh.remove(hs)
    if not len(maHocSinh): raise Exception('Không tìm thấy học sinh nào')
    fl = list(filter( lambda d: d[0] in maHocSinh, data ))
    output += lookup(joinData([data[0]] + fl))
    cls(output)
    print(clr(' \u2716  Tìm thấy ' + str(len(fl)) + ' kết quả khớp', 'success'))
    pl = query1('các chỉ mục (số) của điểm cần xóa (Cách nhau bằng "dấu cách")', 1).split(' ')
    if pl[0] == 'a': pl = [i+1 for i in range(len(fl))]
    for i in pl.copy():
        if not (0 < int(i) <= len(fl)): pl.remove(i)
        else: data.remove(fl[int(i)-1])
    if not len(pl): raise Exception('Không có điểm nào được chọn')
    Write(data)
    print('Đã xóa thành công ' + str(len(pl)) + ' điểm học kì (' + ', '.join(pl) + ')')
    return data

def RemoveAction(data: list):
    title = bold('[4] Xóa bỏ thông tin điểm học sinh')
    cls(title)
    data = data or Read()
    while True:
        try:
            data = remove(data, title+'\n')
        except KeyboardInterrupt:
            return ['p-m', None]
        except Exception as e:
            print(clr(' \u2716  Xóa không thành công: ' + str(e) + '\n    Hãy thử lại!', 'fail'))