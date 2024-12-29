from Class.document import Read, GetOptions
from Students.document import Read as ReadStudentDocs
from Others.style import cls, clr, bold, header, option, query2, tip
from Others.sort import LimitSort

EXIT = ['c-m', None]
F5 = ['c-s', None]

FIELDS = {
    0: ['Mã lớp', '\t', 12],
    1: ['Tên lớp', '\t', 21],
    2: ['Tổng số bàn', '\t', 11],
    3: ['Sĩ số', '\t', 5]
}

SELECTED_FIELDS = [0, 1, 2, 3]

def lookup(data: list):
    index = 1
    output = '\t' + header(('\t').join([data[0][f] for f in SELECTED_FIELDS]), 1)
    for doc in data[1:]:
        doc = list(map(lambda fi: ' '*(FIELDS[fi][2] - len(doc[fi])) + doc[fi], SELECTED_FIELDS))
        if (index%2): output += f'\n     \033[1m{index}\033[0m\t' + ('\t').join(doc) + '\033[0m'
        else: output += f'\n     \033[1;30;37m{index}\033[0m\t\033[30;37m{('\t').join(doc)}\033[0m'
        index += 1
    return output

def ClassIdFilter(data: list, index: int, ft: dict):
    while True:
        try:
            ft['class'] = GetOptions(data, index, False, 'những lớp được hiển thị (Cách nhau bằng "dấu cách")', 2, '      ')
            data = [data[0]] + list(filter(lambda d: d[index] in ft['class'], data[1:]))
            ft['histoty'].append('    ✔️  Có Mã lớp là: ' + ', '.join(ft['class']))
            break
        except Exception as e:
            print(clr(f' ✖  Lọc không thành công: {e}. Hãy chọn lại!', 'fail'))
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
        note = 'Cú pháp: "<Tùy chọn> <Chiều: +(Tăng) hoặc -(Giảm)>"'
        if limit: note += ' <Giới hạn: Số>'
        tip(note, 1)
        sort = input(f'[?] Sắp xếp lớp theo trường (Mặc định: \033[35m{'1 + 10' if limit else '1 +'}\033[0m): ')
        if not sort:
            sort = ['1', '+', '10'] if limit else ['1', '+']
            break
        sort = sort.split(' ')
        if ((len(sort) == 2 and not limit) or (len(sort) == 3 and limit)
            ) and (sort[0].strip() in od and sort[1].strip() in ['+', '-']):
            break
        else:
            print(clr(' \u2716  Lọc không thành công: Cú pháp không hợp lệ.\nHãy chọn lại!', 'fail'))
    ft['sort'] = sort
    data = LimitSort(data, int(sort[2]) if limit else 0, False if sort[1] == '+' else True, lambda d: d[int(sort[0]) - 1])
    data = [dataHead] + data
    ft['histoty'].append(f'    ✔️  Sắp xếp lớp theo trường: {od[sort[0]]}, {'Tăng dần' if sort[1] == '+' else 'Giảm dần'}')
    if limit: ft['histoty'][-1] += ', Giới hạn ' + sort[2]
    else: ft['histoty'][-1] += ', Tất cả'
    return [data, ft]

def joinData(data: list):
    sdata = ReadStudentDocs()
    if len(data[0]) == 3:
        data[0] += [' Sĩ số ', ' Điểm TB ']
        for doc in data[1:]:
            ss = len(list(filter(lambda d: d[6] == doc[0], sdata)))
            doc.append(str(ss))
    return data

def LookupAction(data: list[list]):
    title = bold('[1] Tra cứu thông tin lớp')
    output0 = ''
    output1 = ''
    DATA = data or Read()
    DATA = joinData(DATA)
    data = DATA.copy()
    ft = {'class': [], 'histoty': [' 📝 Lịch sử bộ lọc:']}
    FUNCTION = {
        '1': [ClassIdFilter, (0, 'Lọc theo mã lớp')],
        '2': [ClassSort, (False, 'Sắp xếp tất cả')],
        '3': [ClassSort, (True, 'Sắp xếp giới hạn')],
    }
    ol = [
        option('1', FUNCTION['1'][1][1]),
        option('2', FUNCTION['2'][1][1]) + '\t',
        option('3', FUNCTION['3'][1][1]),
        option('4', 'Chuyển sang Tìm kiếm')
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
                finally: cls(title, '\n', '\n'.join(ft['histoty']), '\n', output1)
            else: print(clr(' \u2716  Chỉ nhập số ứng với các chức năng trên.\n    Hãy thử lại!', 'fail'))
        except KeyboardInterrupt:
            if len(ft['histoty']) > 1:
                cls(title, '\n', output0)
                data = DATA.copy()
                ft = {'class': [], 'histoty': [' 📝 Lịch sử bộ lọc:']}
                output1 = ''
                continue
            return EXIT
        except Exception as e:
            print(clr(f' \u2716  Tra cứu không thành công: {e}\n', 'fail'))
