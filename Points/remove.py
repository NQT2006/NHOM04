from Points.document import Read, Write
from Students.document import Read as ReadStudentDocs, Write as WriteStudentDocs
from Points.lookup import lookup, joinData
from Others.style import clr, cls, bold, query1
import Others.student_input_test as KiemTra

EXIT = ['p-m', None]

def remove(data: list, dshs: list, maHocSinh: list, title: str):
    for hs in maHocSinh:
        try: hs = KiemTra.MaHocSinh(hs)
        except Exception as e: raise Exception(f'{str(e)} (Mã học sinh {hs})')
        if hs not in dshs: maHocSinh.remove(hs)
    if not len(maHocSinh): raise Exception('Không tìm thấy học sinh nào')
    fl = list(filter( lambda d: d[0] in maHocSinh, data ))
    cls( title + '\n' + lookup(joinData([data[0]] + fl)) )
    print(clr(' \u2716  Tìm thấy ' + str(len(fl)) + ' kết quả khớp', 'success'))
    pl = query1('các chỉ mục (số) của điểm cần xóa (Cách nhau bằng "dấu cách")', 1).split(' ')
    if pl[0] == 'a': pl = [i+1 for i in range(len(fl))]
    for i in pl.copy():
        if not (0 < int(i) <= len(fl)): pl.remove(i)
        else: data.remove(fl[int(i)-1])
    if not len(pl): raise Exception('Không có điểm nào được chọn')
    return [data, pl]

def RemoveAction(maHocSinh: list, then: list = None):
    title = bold('[4] Xóa bỏ thông tin điểm học sinh')
    cls(title)
    data = Read()
    sd = ReadStudentDocs()
    dshs = [d[0] for d in sd]
    while True:
        try:
            if not maHocSinh:
                maHocSinh = query1('những mã học sinh cần xóa (Cách nhau bằng "dấu cách")', 1).split(' ')
            data, pl = remove(data, dshs, maHocSinh, title)
            q = input(f' 📣 Bạn chắc chắn muốn xóa {len(pl)} điểm học kì này không ? (Chọn Enter-có hoặc n-không): ').strip()
            if not q:
                Write(data)
                if then: return then
                print(clr(f' \u2702  Xóa thành công {len(pl)} điểm học kì ({(', ').join(pl)})', 'success'))
            else: raise Exception('Hủy xóa')
        except KeyboardInterrupt:
            if then: return then
            return EXIT
        except Exception as e:
            print(clr(' \u2501  Xóa không thành công: ' + str(e) + '\n    Hãy thử lại!', 'fail'))
            if then:
                try: input(' 📣 \033[33mEnter để thoát\033[0m ')
                except: None
                return then