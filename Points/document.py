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
    data[0] = ['Mã học sinh','Toán','Lý','Hóa','Anh','Văn','Điểm trung bình','Học kì','Năm học','Mã học kì']
    newData = '\n'.join([','.join(d) for d in data])
    file.write(newData)
    file.close()
