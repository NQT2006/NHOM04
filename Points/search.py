from Points.document import Read
from Points.lookup import lookup, FIELDS, EXIT, joinData
from Points.update import UpdateAction
from Points.remove import RemoveAction
from Others.style import clr, cls, bold, query1, query2, option, tip
from Others.search import ValueSearch


def search(title: str, data: list[str], index: int, keywords: list[str], dt: list):
    r = ValueSearch(data, index, keywords, dt)
    if len(r) == 1: raise Exception('Không tìm thấy kết quả nào khớp')
    output2 = lookup(r)
    cls(title, '\n', output2, '\n', f'🔎 \033[36mTìm thấy {len(r)-1} kết quả khớp\033[0m\n')
    return [r, output2]

def SearchAction(keywords: list[str], index: int = 0):
    title = bold('[5] Tìm kiếm thông tin điểm học sinh')
    cls(title)
    DATA = joinData(Read())
    data = DATA.copy()
    dt = [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
    fl = [UpdateAction, RemoveAction]
    output1 = '    ' + ('\t'.join(
            list(map(lambda i: option(str(i+1), FIELDS[i][0]) + ' '*(8-len(FIELDS[i][0])), range(7)))
        ) + '\n    ' + '\t'.join(
            list(map(lambda i: option(str(i+1), FIELDS[i][0]) + ' '*(8-len(FIELDS[i][0])), range(7,12)))
        ))
    while True:
        try:
            print(output1+ '    ' + option('ctrl + c', 'Trở về Menu', 43))
            q = query2('1 phương thức tìm kiếm', 1)
            if not (q.isnumeric() and (int(q)-1) in FIELDS):
                print(clr('   \u2716  Đầu vào không hợp lệ: Chỉ chọn các lựa chọn đề xuất\n', 'fail'))
                continue
            q = int(q)-1
            cls(bold(f'[5.{q+1}] Tìm kiếm thông tin học sinh với: {FIELDS[q][0]}'))
            tip('Sử dụng thêm các cú pháp phía trước mỗi từ khóa:' +
                '\n       ==(đúng bằng), <<(nhỏ hơn), >>(lớn hơn), <=(nhỏ hơn bằng), >=(lớn hơn bằng)' +
                ('' if dt[q] else '\n       *(thêm phía trước là kết thúc với), *(thêm phía sau là bắt đầu với)')
                , 2)
            if not keywords:
                keywords = query1(f'các từ khóa/cú pháp tìm kiếm ' +
                    '(Cách nhau bằng "dấu phẩy", mặc định thêm "==")', 2).split(',')
            try:
                r, output2 = search(title, data, q, keywords, dt)
            except Exception as e:
                print(clr('   \u2716  Tìm kiếm không thành công: ' + str(e) + '\n', 'fail'))
            # if not len(r): continue
            keywords = None
        except KeyboardInterrupt:
            return EXIT