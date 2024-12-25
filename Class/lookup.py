from Class.document import Read, ClassOptions
from random import random
from Students.document import Read as ReadStudentDocs
from Others.style import cls, clr, bold, header, option, quest2
from Others.sort import LimitSort

MODE = {
    'exit': ['c-m', None],
    'f2':   ['c-a', None],
    'f3':   ['c-u', None],
    'f4':   ['c-r', None],
    'f5':   ['c-s', None]
}

def lookup(data: list):
    index = 1
    output = '\t' + header(('\t').join(data[0]), 1)
    for doc in data[1:]:
        doc[1] = ' '*(22 - len(doc[1])) + doc[1]
        doc[2] = ' '*(14 - len(doc[2])) + doc[2]
        nd = doc[:3] + [' '*(6 - len(doc[3])) + doc[3]]
        output += '\n     ' + bold(index) + '\t    ' + ('\t').join(nd)
        index += 1
    return output

def ClassIdFilter(data: list, index: int, ft: dict):
    dataHead = data[0]
    while True:
        try:
            ft['maLop'] = ClassOptions(data, 0, False, 'những lớp được hiển thị (Cách nhau bằng "dấu cách")', 2, '      ')
            dataBody = list(filter(lambda d: d[index] in ft['maLop'], data[1:]))
            data = [dataHead] + dataBody
            ft['histoty'].append('    ✔️  Có mã lớp: ' + ', '.join(ft['maLop']))
            break
        except Exception as e:
            print(clr(f'[x] Lọc không thành công: {e}. Hãy chọn lại!', 'fail'))
    return [data, ft]

def ClassSort(data: list, limit: bool, ft: dict):
    dataHead = data[0]
    data = data[1:]
    od = {
        '1': 'Mã lớp',
        '2': 'Tên lớp',
        '3': 'Tổng số bàn',
        '4': 'Sĩ số',
        '5': 'Điểm trung bình'
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


def LookupAction(data: list[list]):
    title = bold('[1] Tra cứu thông tin lớp')
    output = ''
    if not data: data = Read()
    sdocs = ReadStudentDocs()
    for doc in data[1:]:
        ss = len(list(filter(lambda d: d[6] == doc[0], sdocs)))
        doc.append(str(ss))
    data[0] += [' Sĩ số ', ' Điểm trung bình ']
    cd = data.copy()
    ft = {'maLop': [], 'histoty': [' 📝 Lịch sử bộ lọc:'], 'sort': ''}
    FUNCTION = {
        '1': [ClassIdFilter, (0, 'Lọc theo mã lớp')],
        '2': [ClassSort, (False, 'Sắp xếp tất cả theo trường')],
        '3': [ClassSort, (True, 'Sắp xếp giới hạn theo trường')]
    }
    ol = [
        option('1', FUNCTION['1'][1][1]),
        option('2', FUNCTION['2'][1][1]),
        option('3', FUNCTION['3'][1][1])
    ]
    while True:
        if not output:
            output = lookup(cd)
            cls(title, '\n', output)
        try:
            print('\n    ' + '   '.join(
                ol + [option('ctrl + c', 'Xóa bộ lọc' if len(ft['histoty']) > 1 else 'Trở về Menu', 43)]
            ))
            fn = quest2('1 chức năng', 1)
            if fn in MODE: return MODE[fn]
            elif fn in FUNCTION:
                cls(title, '\n', output)
                print(f'[1.{fn}] {FUNCTION[fn][1][1]}')
                cd, ft = FUNCTION[fn][0](cd, FUNCTION[fn][1][0], ft)
                cls(title, '\n', '\n'.join(ft['histoty']), '\n', lookup(cd))
            else: print(clr(' ❌ Chỉ nhập số ứng với các chức năng trên.\n    Hãy thử lại!', 'fail'))
        except KeyboardInterrupt:
            print('', end='\033[0m')
            if len(ft['histoty']) > 1:
                cls(title, '\n', output)
                cd = data.copy()
                ft = {'maLop': [], 'histoty': [' 📝 Lịch sử bộ lọc:'], 'sort': ''}
                continue
            return MODE['exit']
