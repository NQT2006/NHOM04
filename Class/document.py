from csv import reader
from Others.style import clr, option, query2

def Read():
    file = open('csv_file/ds_lop_hoc.csv', 'r', encoding = 'utf-8')
    data = list(reader(file))
    data[0] = ['    Mã lớp    ','        Tên lớp       ',' Tổng số bàn ']
    return data

def Write(data):
    file = open('csv_file/ds_lop_hoc.csv', 'w', encoding = 'utf-8')
    header = [['Mã lớp','Tên lớp','Tổng số bàn']]
    if data == 'clear': data = header
    else:
        body = data[1:]
        body.sort(key=lambda d: d[0])
        data = header + body
    newData = '\n'.join([','.join(d) for d in data])
    file.write(newData)
    file.close()

def GetOptions(data: list, index: int, only: bool, alert: str, level: int, space = '      ', otherOptions = None):
    ds = list({ d[index] for d in data[1:] })
    ds.sort()
    cl = { str(i+1): ds[i] for i in range(0, len(ds)) }
    ol = list(map(lambda k: space + option(k, cl[k]), cl))
    if otherOptions:
        for k in otherOptions:
            ol.append(space + option(k, otherOptions[k], 45))
    ol.append(space + option('ctrl + c', 'Thoát', 43))
    for i in range(round(len(cl) / 5 + .4)):
        print('\t'.join(ol[5*i:5*(i+1)]))
    while True:
        try:
            fl = query2(alert, level)
            if not fl: raise Exception('Không có lớp nào được chọn')
            elif otherOptions and fl in otherOptions: return fl
            elif only and fl in cl: return cl[fl]
            fl = fl.split(' ')
            if only and len(fl) > 1:
                raise Exception('Chỉ được chọn 1 lớp duy nhất')
            elif not only:
                fl = list(filter(lambda x: x in cl, fl))
                if not len(fl): raise Exception('Không có lớp nào được chọn')
                return list(map(lambda x: cl[x], fl))
            else: raise Exception('Không có lớp nào được chọn')
        except Exception as e:
            print(clr(' ❌ Đầu vào không hợp lệ: ' + str(e) + '\nHãy thử lại!', 'fail'))

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