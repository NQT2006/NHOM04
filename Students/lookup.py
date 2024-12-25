from Students.document import Read
from Others.style import cls, clr, option, bold, header
from Others.sort import LimitSort

MODE = {
    'exit': ['s-m', None],
    'f2':   ['s-a', None],
    'f3':   ['s-u', None],
    'f4':   ['s-r', None],
    'f5':   ['s-s', None]
}

def lookup(data: list):
    index = 1
    print('\t' + header(('\t').join(data[0]), 1))
    for doc in data[1:]:
        doc[1] = ' '*(21 - len(doc[1])) + doc[1]
        doc[2] = ' '*(13 - len(doc[2])) + doc[2]
        doc[3] = ' ' + doc[3]
        doc[4] = '  ' + doc[4]
        if (index%2): print(f'     \033[1m{index}\033[0m\t  ' + ('\t ').join(doc))
        else: print(f'     \033[1;30;37m{index}\033[0m\t  \033[30;37m{('\t ').join(doc)}\033[0m')
        index += 1

def StudentsSort(data: list, limit: bool, ft: dict):
    dataHead = data[0]
    data = data[1:]
    od = {
        '1': 'Mã học sinh',
        '2': 'Họ đệm',
        '3': 'Tên',
        '4': 'Tuổi',
        '5': 'Ngày sinh',
        '6': 'Số điện thoại',
        '7': 'Mã lớp'
    }
    ol = list(map(lambda k: '\t' + option(k, od[k]), od)) + [option('Enter↵', 'Mặc định')]
    for i in range(round(len(od) / 3 + .4)):
        print('\t'.join(ol[3*i:3*(i+1)]))
    sort = ''
    while True:
        note = '[!] Cú pháp: "<Tùy chọn> <Chiều: +(Tăng) hoặc -(Giảm)>"'
        if limit: note += ' <Giới hạn: Số>'
        print(clr(note, 'note'))
        sort = input(f'[?] Sắp xếp lớp theo trường (Mặc định: \033[35m{'1 + 10' if limit else '1 +'}\033[0m): ')
        if not sort:
            sort = ['1', '+', '10'] if limit else ['1', '+']
            break
        sort = sort.split(' ')
        if ((len(sort) == 2 and not limit) or (len(sort) == 3 and limit)
            ) and (sort[0].strip() in od and sort[1].strip() in ['+', '-']):
            break
        else:
            print(clr(' ❌ Lọc không thành công: Cú pháp không hợp lệ.\nHãy chọn lại!', 'fail'))
    ft['sort'] = sort
    data = LimitSort(data, int(sort[2]) if limit else 0, int(sort[1]+'1'), lambda d: d[int(sort[0]) - 1])
    data = [dataHead] + data
    ft['histoty'].append(f'    ✔️  Sắp xếp lớp theo trường: {od[sort[0]]}, {'Tăng dần' if sort[1] == '+' else 'Giảm dần'}')
    if limit: ft['histoty'][-1] += ', Giới hạn ' + sort[2]
    else: ft['histoty'][-1] += ', Tất cả'
    return [data, ft]


def LookupAction(data: list = None):
    title = bold('[1] Tra cứu thông tin lớp')
    data = Read()
    cdata = data.copy()
    ft = {'maLop': [], 'histoty': [' 📝 Lịch sử bộ lọc:'], 'sort': ''}
    # data.sort(key= lambda l: l[0])
    FUNCTION = {
        '1': [None, (0, 'Lọc theo mã lớp')],
        '2': [StudentsSort, (False, 'Sắp xếp tất cả theo trường')],
        '3': [StudentsSort, (True, 'Sắp xếp giới hạn theo trường')]
    }
    ol = [
        option('1', FUNCTION['1'][1][1]),
        option('2', FUNCTION['2'][1][1]),
        option('3', FUNCTION['3'][1][1])
    ]
    while True:
        cls(title + (('\n'.join(ft['histoty']) + '\n') if len(ft['histoty']) > 1 else ''))
        lookup(cdata)
        try:
            print('\n    ' + '   '.join(
                ol + [option('ctrl + c', 'Xóa bộ lọc' if len(ft['histoty']) > 1 else 'Trở về Menu', 43)]
            ))
            fn = input('[?] Chọn chức năng: ')
            if fn in MODE: return MODE[fn]
            elif fn in FUNCTION:
                print(f'[1.{fn}] {FUNCTION[fn][1][1]}')
                cdata, ft = FUNCTION[fn][0](cdata, FUNCTION[fn][1][0], ft)
            else: print(clr(' ❌ Chỉ nhập số ứng với các chức năng trên.\n    Hãy thử lại!', 'fail'))
        except KeyboardInterrupt:
            if len(ft['histoty']) > 1:
                cdata = data.copy()
                ft = {'maLop': [], 'histoty': [' 📝 Lịch sử bộ lọc:'], 'sort': ''}
                continue
            return MODE['exit']