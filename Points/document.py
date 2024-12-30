from csv import reader

def Read():
    file = open('csv_file/ds_diem.csv', 'r', encoding = 'utf-8')
    data = list(reader(file))
    data[0] = [' Mã học sinh ',' Toán ','  Lý  ','  Hóa  ','  Anh  ','  Văn  ',' Điểm TB ',' Học kì ', ' Năm học ',' Mã học kì ']
    return data

def Add(*data):
    file = open('csv_file/ds_diem.csv', 'a', encoding = 'utf-8')
    for l in data:
        file.write('\n' + ','.join(l))
    file.close()

def Write(data):
    file = open('csv_file/ds_diem.csv', 'w', encoding = 'utf-8')
    header = [['Mã học sinh','Toán','Lý','Hóa','Anh','Văn','Điểm trung bình','Học kì','Năm học','Mã học kì']]
    if data == 'clear': data = header
    else:
        body = data[1:]
        body.sort(key=lambda d: d[0])
        data = header + body
    newData = '\n'.join([','.join(d[:10]) for d in data])
    file.write(newData)
    file.close()
