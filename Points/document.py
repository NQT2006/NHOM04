from csv import reader

def Read():
    file = open('csv_file/ds_diem.csv', 'r', encoding = 'utf-8')
    return list(reader(file))

def Add(data):
    file = open('csv_file/ds_diem.csv', 'a', encoding = 'utf-8')
    if type(data[0]) is list:
        for l in data:
            file.write('\n' + ','.join(l))
    else:
        file.write('\n' + ','.join(data))
    file.close()

def Write(data):
    file = open('csv_file/ds_diem.csv', 'w', encoding = 'utf-8')
    if type(data[0]) is list:
        newData = '\n'.join([','.join(l) for l in data])
        file.write(newData)
    else:
        raise Exception('data isn\'t list of list')
    file.close()
