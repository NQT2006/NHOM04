from csv import reader
from Others.style import clr, option, quest2

def Read():
    file = open('csv_file/ds_lop_hoc.csv', 'r', encoding = 'utf-8')
    return list(reader(file))

def Add(data):
    file = open('csv_file/ds_lop_hoc.csv', 'a', encoding = 'utf-8')
    if type(data[0]) is list:
        for l in data:
            file.write('\n' + ','.join(l))
    else:
        file.write('\n' + ','.join(data))
    file.close()

def Write(data):
    file = open('csv_file/ds_lop_hoc.csv', 'w', encoding = 'utf-8')
    if type(data[0]) is list:
        newData = '\n'.join([','.join(l) for l in data])
        file.write(newData)
    else:
        raise Exception('data isn\'t list of list')
    file.close()

def ClassOptions(data: list, index: int, only: bool, alert: str, level: int, space = '      ', otherOptions = None):
    dataBody = data[1:]
    dsl = { str(i+1): dataBody[i][index] for i in range(0, len(dataBody)) }
    ol = list(map(lambda k: space + option(k, dsl[k]), dsl))
    if otherOptions:
        for k in otherOptions:
            ol.append(space + option(k, otherOptions[k], 45))
    ol.append(space + option('ctrl + c', 'Thoát', 43))
    for i in range(round(len(dsl) / 5 + .4)):
        print('\t'.join(ol[5*i:5*(i+1)]))
    while True:
        try:
            maLop = quest2(alert, level)
            if not maLop: raise Exception('Không có lớp nào được chọn')
            elif otherOptions and maLop in otherOptions: return maLop
            elif only and maLop in dsl: return dsl[maLop]
            maLop = maLop.split(' ')
            if only and len(maLop) > 1:
                raise Exception('Chỉ được chọn 1 lớp duy nhất')
            elif not only:
                maLop = list(filter(lambda x: x in dsl, maLop))
                if not len(maLop): raise Exception('Không có lớp nào được chọn')
                return list(map(lambda x: dsl[x], maLop))
            else: raise Exception('Không có lớp nào được chọn')
        except Exception as e:
            print(clr(' ❌ Đầu vào không hợp lệ: ' + str(e) + '\nHãy thử lại!', 'fail'))