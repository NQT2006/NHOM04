from Points.document import Read
from Students.document import Read as ReadStudentDocs
from Class.document import ClassIdFilter
from Others.style import cls, clr, option, bold, header, query1, query2
from Others.sort import LimitSort
# from Class.lookup import ClassIdFilter

EXIT = ['p-m', None]
F5 = ['p-s', None]

FIELDS = {
    0: ['Mã học sinh', '\t', 12],
    1: ['Toán', '\t', 4],
    2: ['Lý', '    \t', 4],
    3: ['Hóa', '\t', 4],
    4: ['Anh', '\t', 5],
    5: ['Văn', '    \t', 5],
    6: ['Điểm TB', '\t', 6],
    7: ['Học kì', '\t', 6],
    8: ['Năm học', '\t', 8],
    9: ['Mã học kì', '\t', 7],
    10: ['Học lực', '\t', 9],
    11: ['Mã lớp', '\t', 11],
}

SELECTED_FIELDS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def lookup(data: list, fields: list = SELECTED_FIELDS):
    index = 1
    output = '\t' + '  '.join(list(map( lambda x: header(x, 1), [data[0][f] for f in fields] )))
    for doc in data[1:]:
        doc = list(map(lambda fi: ' '*(FIELDS[fi][2] - len(doc[fi])) + doc[fi], fields))
        if (index%2): output += f'\n     \033[1m{index}\033[0m\t' + '    '.join(doc) + '\033[0m'
        else: output += f'\n     \033[1;30;37m{index}\033[0m\t\033[30;37m{'    '.join(doc)}\033[0m'
        index += 1
    return output

def AlterColumn(*a):
    raise Exception('Tính năng đang phát triển')

def PointsSort(data: list, limit: bool, ft: dict):
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
        note = '  [!] Cú pháp: "<Tùy chọn> <Chiều: +(Tăng) hoặc -(Giảm)>"'
        if limit: note += ' <Giới hạn: Số>'
        print(clr(note, 'note'))
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
    desc = False if sort[1] == '+' else True
    if sort[0] == '11': desc = not desc
    data = LimitSort(data, int(sort[2]) if limit else 0, desc, lambda d: d[int(sort[0])-1])
    data = [dataHead] + data
    ft['histoty'].append('    \u268A  Sắp xếp điểm theo trường: ' + FIELDS[fields[int(sort[0])-1]][0] )
    ft['histoty'][-1] += ', ' + ('Tăng dần' if sort[1] == '+' else 'Giảm dần')
    if limit: ft['histoty'][-1] += ' (Giới hạn ' + sort[2] + ')'
    else: ft['histoty'][-1] += ' (Tất cả)'
    return [data, ft]

def joinData(data: list):
    if len(data[0]) == 10:
        data[0] += [' Học lực ', '   Mã lớp   ']
        sdata = ReadStudentDocs()
        dsmhs1 = [hs[0] for hs in sdata]
        dsmhs2 = [hs[0] for hs in data]
        for i in range(1, len(dsmhs2)):
            p = float(data[i][6])
            if p >= 8: data[i].append('Giỏi')
            elif p >= 6: data[i].append('Khá ')
            elif p >= 4: data[i].append('TB  ')
            else: data[i].append('Yếu ')
            index = dsmhs1.index(dsmhs2[i])
            data[i].append(sdata[index][6])
    return data

def LookupAction(data: list):
    title = bold('[1] Tra cứu thông tin điểm')
    DATA = data
    if not data: DATA = Read()
    DATA = joinData(DATA)
    
    data = DATA.copy()
    output0 = lookup(data)
    cls(title, '\n', output0)
    output1 = ''
    ft = { 'class': [], 'histoty': [' 📝 Lịch sử bộ lọc:'] }
    # DATA.sort(key= lambda l: l[0])
    FUNCTION = {
        '1': [AlterColumn, (None, 'Thay đổi cột dữ liệu')],
        '2': [ClassIdFilter, (11, 'Lọc theo mã lớp')],
        '3': [PointsSort, (False, 'Sắp xếp tất cả')],
        '4': [PointsSort, (True, 'Sắp xếp giới hạn')]
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
                else: cls(title, '\n', '\n'.join(ft['histoty']), '\n\n', output1)
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
            print(clr(' \u2716  Lọc không thành công: ' + str(e) + '\n    Hãy thử lại!', 'fail'))

'''def lookupAcion():
    l = Read()
    index = 1
    h = '\t' + ('\t').join(l[0][:7]) + '\t' + ('\t').join(l[0][7:])
    print(header(h, 1))
    nl = map(lambda x: x[:6] + [x[7]+'\t'] + x[7:9] + [x[9]], l[1:])
    for fields in nl:
        print(bold(index) + '\t ' + ('\t ').join(fields[:9]) + '\t  ' + fields[9])
        index += 1'''