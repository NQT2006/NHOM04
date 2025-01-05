from Class.document import Read, Write, GetOptions
from Students.document import Read as ReadStudents
from Others import *

EXIT = ['c-m', None]

def remove(data: list, maLop: list, dsml: list, dskhl: list):
    for lop in maLop:
        if lop not in maLop:
            maLop.remove(lop)
            continue
        if lop in dskhl: raise Exception(f'Không thể xóa lớp {lop} (Đang có học sinh)')
        index = dsml.index(lop)
        data = data[:index] + data[index+1:]
    if not len(maLop): raise Exception('Không tìm thấy lớp nào')
    return [data, maLop]

def RemoveAction(maLop: list, then: list = None):
    title = bold('[4] Xóa bỏ thông tin lớp')
    cls(title)
    data = Read()
    dsml = [l[0] for l in data]
    dskhl = {l[6] for l in ReadStudents()}
    while True:
        try:
            if not maLop:
                maLop = [GetOptions(data, 0, True, 'những lớp cần xóa (Cách nhau bằng "dấu cách")', 1, '    ')]
            newData, maLop = remove(data, maLop, dsml, dskhl)
            save = input(f' 📣 Bạn chắc chắn muốn xóa {len(maLop)} lớp chứ ? ' +
                'Chọn Enter↵(có) hoặc n(không): ').strip()
            if not save:
                Write(newData)
                if then: return then
                print(clr(f' \u2702  Xóa thành công {len(maLop)} lớp\n', 'success'))
            if then: return then
            maLop = None
        except KeyboardInterrupt:
            if then: return then
            return EXIT
        except Exception as e:
            print(clr(' \u2716  Xóa không thành công: ' + str(e) + '\n', 'fail'))
            if then:
                try: input(' 📣 \033[33mEnter↵ để thoát\033[0m ')
                except: None
                return then