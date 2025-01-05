from Class.document import Read
from Class.lookup import lookup, FIELDS, joinData
from Others import *
from Others.search import ValueSearch

EXIT = ['c-m', None]

def search(title: str, data: list[str], index: int, keywords: list[str], dt: list):
    r = ValueSearch(data, index, keywords, dt)
    if len(r) == 1: raise Exception('Không tìm thấy kết quả nào khớp')
    cls(title, '\n', lookup(r), '\n', f'🔎 \033[36mTìm thấy {len(r)-1} kết quả khớp\033[0m\n')
    return r

def SearchAction(keywords: list[str], index: int = 0):
    title = bold('[5] Tìm kiếm thông tin học sinh')
    cls(title)
    DATA = joinData(Read())
    data = DATA.copy()
    dt = [0, 0, 1, 1]
    output1 = '    ' + '    '.join( list(map(lambda i: option(str(i[0]+1), i[1][0]), FIELDS.items())) )
    output2 = '    ' + '    '.join([
        option('1', 'Tìm kiếm với dữ liệu này'),
        option('2', 'Chỉnh sửa tất cả'),
        option('3', 'Xóa bỏ tất cả'),
        option('ctrl + c', 'Thoát', 43)
    ])
    while True:
        try:
            if not keywords:
                print(output1+ '    ' + option('ctrl + c', 'Trở về Menu', 43))
                index = query2('1 phương thức tìm kiếm', 1)
                if not (index.isnumeric() and (int(index)-1) in FIELDS):
                    print(clr(' \u2716  Đầu vào không hợp lệ: Chỉ chọn các lựa chọn đề xuất\n', 'fail'))
                    continue
                index = int(index)-1
                cls(bold(f'[5.{index+1}] Tìm kiếm thông tin học sinh với: {FIELDS[index][0]}'))
                tip('Sử dụng thêm các cú pháp phía trước mỗi từ khóa:' +
                    '\n       ==(đúng bằng), <<(nhỏ hơn), >>(lớn hơn), <=(nhỏ hơn bằng), >=(lớn hơn bằng)' +
                    ('' if dt[index] else '\n       *(thêm phía trước là kết thúc với), *(thêm phía sau là bắt đầu với)')
                    , 2)
                keywords = query1(f'các từ khóa/cú pháp tìm kiếm ' +
                    '(Cách nhau bằng "dấu phẩy", mặc định thêm "==")', 2).split(',')
            try:
                r = search(title, data, index, keywords, dt)
                while True:
                    print(output2)
                    c = query2('thao tác với dữ liệu tìm thấy', 1)
                    if c == '1':
                        data = r
                        break
                    elif c == '2': return ['c-u', [d[0] for d in r[1:]], ['c-s', keywords, index]]
                    elif c == '3': return ['c-r', [d[0] for d in r[1:]], ['c-s', keywords, index]]
                    else: print(clr('   \u2716  Đầu vào không hợp lệ: Chỉ chọn tùy chọn thao tác đề xuất\n', 'fail'))
            except KeyboardInterrupt:
                cls(title)
                data = DATA.copy()
            except Exception as e:
                print(clr('   \u2716  Tìm kiếm không thành công: ' + str(e) + '\n', 'fail'))
            keywords = None
        except KeyboardInterrupt:
            return EXIT