from csv import reader

def Read():
    file = open('csv_file/ds_hoc_sinh.csv', 'r', encoding = 'utf-8')
    data = list(reader(file))
    data[0] = [' Mã học sinh ','        Họ đệm       ','     Tên     ',' Tuổi ','  Ngày sinh  ','     SĐT     ','   Mã lớp   ']
    return data

def Add(*data):
    file = open('csv_file/ds_hoc_sinh.csv', 'a', encoding = 'utf-8')
    for l in data: file.write('\n' + ','.join(l))
    file.close()

def Write(data):
    file = open('csv_file/ds_hoc_sinh.csv', 'w', encoding = 'utf-8')
    data[0] = ['Mã học sinh','Họ đệm','Tên','Tuổi','Ngày sinh','Số điện thoại','Mã lớp']
    newData = '\n'.join([','.join(data[i]) for i in range(7)])
    file.write(newData)
    file.close()
