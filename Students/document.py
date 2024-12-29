from csv import reader

def Read():
    file = open('csv_file/ds_hoc_sinh.csv', 'r', encoding = 'utf-8')
    data = list(reader(file))
    data[0] = [' Mã học sinh ','        Họ đệm       ','     Tên     ',' Tuổi ','  Ngày sinh  ','     SĐT     ','   Mã lớp   ']
    return data

def Write(data: list):
    file = open('csv_file/ds_hoc_sinh.csv', 'w', encoding = 'utf-8')
    header = [['Mã học sinh','Họ đệm','Tên','Tuổi','Ngày sinh','Số điện thoại','Mã lớp']]
    if data == 'clear': data = header
    else:
        body = data[1:]
        body.sort(key=lambda d: d[0])
        data = header + body
    newData = '\n'.join([','.join(d) for d in data])
    file.write(newData)
    file.close()
