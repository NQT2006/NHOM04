from Students.document import Read
from Class.document import ClassIdFilter
from Others import *
from Others.sort import LimitSort

EXIT = ['s-m', None]
F5 = ['s-s', None]

FIELDS = {
    0: ['Mã học sinh', '\t', 12],
    1: ['Họ đệm', '\t', 20],
    2: ['Tên', '\t', 12],
    3: ['Tuổi', '\t', 4],
    4: ['Ngày sinh', '\t', 12],
    5: ['SĐT', '  \t', 12],
    6: ['Mã lớp', '\t', 11]
}
SELECTED_FIELDS = [0, 1, 2, 4, 3, 5, 6]

def lookup(data: list):
    index = 1
    output = '\t' + header('\t'.join([data[0][f] for f in SELECTED_FIELDS]), 1)
    for doc in data[1:]:
        doc = list(map(lambda fi: ' '*(FIELDS[fi][2] - len(doc[fi])) + doc[fi], SELECTED_FIELDS))
        if (index%2): output += f'\n     \033[1m{index}\033[0m\t' + ('\t').join(doc) + '\033[0m'
        else: output += f'\n     \033[1;30;37m{index}\033[0m\t\033[30;37m{('\t').join(doc)}\033[0m'
        index += 1
    return output

def StudentsSort(data: list, limit: bool, ft: dict):
    dataHead = data[0]
    data = data[1:]
    fields = SELECTED_FIELDS
    ol = []
    for i in range(len(fields)):
        fi = fields[i]
        ol.append(option(str(i+1), FIELDS[fi][0]) + FIELDS[fi][1])
    ol.append(option('Enter↵', 'Mặc định', 46))
    ol.append(option('ctrl + c', 'Thoát', 43))
    for i in range(round(len(ol) / 5 + .4)):
        print('      ' + '\t'.join(ol[5*i:5*(i+1)]))
    sort = ''
    while True:
        note = 'Cú pháp: "<Tùy chọn> <Chiều: +(Tăng) hoặc -(Giảm)>"'
        if limit: note += ' <Giới hạn: Số>'
        tip(note, 1)
        sort = query1(f'cú pháp sắp xếp (Mặc định: \033[35m{'1 + 10' if limit else '1 +'}\033[0m)', 2)
        if not sort:
            sort = ['1', '+', '10'] if limit else ['1', '+']
            break
        sort = sort.split(' ')
        if ((len(sort) == 2 and not limit) or (len(sort) == 3 and limit)
            ) and ((0 < int(sort[0]) <= len(fields)) and sort[1].strip() in ['+', '-']):
            break
        else: print(clr(' ❌ Lọc không thành công: Cú pháp không hợp lệ.\nHãy chọn lại!', 'fail'))
    ft['sort'] = sort
    data = LimitSort(data, int(sort[2]) if limit else 0, False if sort[1] == '+' else True, lambda d: d[int(sort[0])-1])
    data = [dataHead] + data
    ft['histoty'].append('    ✔️  Sắp xếp lớp theo trường: ' + FIELDS[fields[int(sort[0])-1]][0] )
    ft['histoty'][-1] += ', ' + ('Tăng dần' if sort[1] == '+' else 'Giảm dần')
    if limit: ft['histoty'][-1] += ' (Giới hạn ' + sort[2] + ')'
    else: ft['histoty'][-1] += ' (Tất cả)'
    return [data, ft]

def AlterColumn(data, n, ft):
    return [data, ft]

def LookupAction(data: list):
    title = bold('[1] Tra cứu thông tin lớp')
    DATA = data
    if not data:
        DATA = Read()

    data = DATA.copy()
    output0 = lookup(data)
    cls(title, '\n', output0)
    output1 = ''
    ft = { 'class': [], 'histoty': [' 📝 Lịch sử bộ lọc:'] }
    # DATA.sort(key= lambda l: l[0])
    FUNCTION = {
        '1': [AlterColumn, (None, 'Cấu trúc lại bảng')],
        '2': [ClassIdFilter, (6, 'Lọc theo mã lớp')],
        '3': [StudentsSort, (False, 'Sắp xếp tất cả')],
        '4': [StudentsSort, (True, 'Sắp xếp giới hạn')]
    }
    ol = [
        option('1', FUNCTION['1'][1][1]),
        option('2', FUNCTION['2'][1][1]) + '\t',
        option('3', FUNCTION['3'][1][1]),
        option('4', FUNCTION['4'][1][1]),
        option('5', 'Chuyển sang Tìm kiếm')
    ]
    while True:
        if not output0:
            output0 = lookup(data)
            cls(title, '\n', output0)
        print('\n    ' + '\t'.join(ol[:3]))   
        print('    ' + '\t'.join(
            ol[3:] + [option('ctrl + c', 'Xóa bộ lọc' if len(ft['histoty']) > 1 else 'Trở về Menu', 43)]
        ))
        try:
            fn = query2('1 chức năng', 1)
            if fn == '5': return F5
            elif fn in FUNCTION:
                if len(ft['histoty']) == 1: cls(title, '\n', output0)
                else: cls(title, '\n', '\n'.join(ft['histoty']), '\n', output1)
                print(bold(f'[1.{fn}] {FUNCTION[fn][1][1]}'))
                try:
                    data, ft = FUNCTION[fn][0](data, FUNCTION[fn][1][0], ft)
                    output1 = lookup(data)
                except KeyboardInterrupt: continue
                finally:
                    if len(ft['histoty']) == 1: cls(title, '\n', output0)
                    else: cls(title, '\n', '\n'.join(ft['histoty']), '\n\n', output1)
            else: print(clr(' \u2716  Chỉ nhập số ứng với các chức năng trên.\n    Hãy thử lại!', 'fail'))
        except KeyboardInterrupt:
            if len(ft['histoty']) > 1:
                cls(title, '\n', output0)
                data = DATA.copy()
                ft = { 'class': [], 'histoty': [' 📝 Lịch sử bộ lọc:'] }
                output1 = ''
                continue
            return EXIT
        except Exception as e:
            print(clr(' \u2716  Lọc không thành công: ' + str(e), 'fail'))