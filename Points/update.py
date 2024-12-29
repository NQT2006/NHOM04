from Points.document import Read, Write
from Points.lookup import FIELDS, joinData
from Others.style import clr, cls, header, option, query1, query2
import Others.point_input_test as KiemTra

EXIT = ['p-m', None]

SELECTED_FIELDS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def update(data, index, output0, Test ):
    f = data[index]
    t = [f[0]]
    pos = 1
    catch = ''
    output1 = 'Từ:\t' + '    '.join(list(map(lambda fi: ' '*(FIELDS[fi][2] - len(f[fi])) + f[fi], SELECTED_FIELDS)))
    output2 = 'Thành:\t\033[35m' + ' '*(FIELDS[0][2]+4)
    cls(output0)
    print(output1)
    while pos < 10:
        if catch: print(clr(f' \u2716  Cập nhật không thành công: {catch}\n     Hãy thử lại!', 'fail'))
        value = input(output2 + ('  ' if pos > 7 else '')).strip()
        print('', end='\033[0m')
        try:
            if not value:
                output2 += '\033[20;39;39m' + ' '*FIELDS[pos][2] + ' '*4 + '\033[35m'
                t.append(f[pos])
            else:
                value = Test[pos](value)
                t.append(value)
                output2 += ' '*(FIELDS[pos][2] - len(value)) + value + ' '*4
            pos += 1
            catch = ''
            if pos == 6:
                if f[1:6] == t[1:6]:
                    output2 += ' '*(FIELDS[pos][2] + 4)
                    t.append(f[pos])
                else:
                    ap = list(map(lambda x: float(x), t[1:6]))
                    ap = str(round((ap[0] + ap[1] + ap[2] + ap[3] + ap[4])/5, 2))
                    output2 += ' '*(FIELDS[pos][2] - len(ap)) + ap + ' '*4
                    t.append(ap)
                output2 += ' '*(FIELDS[pos+1][2] + 4)
                t.append(f[pos+1])
                pos += 2
            cls(output0)
            print(output1)
        except Exception as e:
            catch = str(e)
            continue
    data[index] = t
    print(output2+'\033[0m')
    return data

def UpdateAction(maHocSinh: list, then: list = None):
    title = '\033[1m[3] Chỉnh sửa thông tin lớp\033[0m'
    cls(title)
    data = Read()
    dsmhs = [l[0]+l[8]+l[7] for l in data]
    Test = [KiemTra.MaHocSinh] + [KiemTra.MonHoc]*6 + [KiemTra.HocKi, KiemTra.NamHoc, KiemTra.MaHocKi]
    output0 = ''.join([
        '    ', option('Enter↵', 'Không thay đổi', 46), '\t',
        option('ctrl + c', 'Thoát' if then else 'Trở về Menu', 43), '\n\n\t',
        '  '.join(list(map( lambda x: header(x, 1), [data[0][f] for f in SELECTED_FIELDS] )))
    ])
    while True:
        try:
            if not maHocSinh:
                output = ''+title
                maHocSinh = KiemTra.MaHocSinh(query1('mã học sinh cần sửa điểm', 1))
                output += f'\n    Mã học sinh: \033[35m{maHocSinh}\033[0m'
                cls(output)
                nd = list(filter(lambda d: d[0] == maHocSinh, data))
                nd1 = list(set(map(lambda d: d[8], nd)))
                nd1.sort()
                while True:
                    print('\n    ' + '    '.join(list(map(lambda i, y: option(str(i+1), y), range(len(nd1)), nd1 ))))
                    namHoc = query2('năm học', 1)
                    if namHoc.isnumeric() and int(namHoc) in range(1, len(nd1)+1):
                        namHoc = nd1[int(namHoc)-1]
                        maHocSinh += namHoc
                        output += f'\n    Năm học: \033[35m{namHoc}\033[0m'
                        cls(output)
                        break
                    print(clr(' \u2716  Đầu vào không hợp lệ: Chỉ chọn trong các tùy chọn đề xuất' +
                        '\n    Hãy thử lại', 'fail'))
                while True:
                    print('\n    ' + '    '.join([option('1', 'Học kì I'), option('2', 'Học kì II')]))
                    hocKi = query2('học kì', 1)
                    if hocKi in ['1', '2']:
                        maHocSinh += hocKi
                        break
                    print(clr(' \u2716  Đầu vào không hợp lệ: Chỉ chọn trong các tùy chọn đề xuất' +
                        '\n    Hãy thử lại', 'fail'))
                maHocSinh = [maHocSinh]
            ii = 0
            while ii < len(maHocSinh):
                index = dsmhs.index(maHocSinh[ii])
                o = (f'{title}: Học sinh mã \033[35m{maHocSinh[ii][:-5]}\033[0m -' +
                    f' Học kì \033[35m{'I' if maHocSinh[ii][-1] == '1' else 'II'}\033[0m -' +
                    f' Năm học\033[35m{maHocSinh[ii][-5:-1]}\033[0m\n\n{output0}')
                newData = update(data.copy(), index, o, Test)
                if newData == data:
                    ext = input(' \033[2;37;39m⊞\033[0m  Bạn không chỉnh sửa gì. ' +
                        'Muốn thoát chứ ? Chọn Enter↵(thoát) hoặc n(sửa lại): ')
                    if not ext:
                        print(clr(' \u2716  Cập nhật không thành công: Hủy chỉnh sửa', 'fail'))
                        ii += 1
                else:
                    data = newData
                    ext = input(' \033[2;37;39m⊞\033[0m  Bạn muốn lưu lại chỉnh sửa này chứ ?' +
                        ' Chọn Enter↵(lưu) hoặc n(sửa lại): ')
                    if not ext:
                        Write(data)
                        print(clr(' \u271a  Cập nhật thành công', 'success'))
                        ii += 1
            maHocSinh = None
        except KeyboardInterrupt:
            return EXIT
        except Exception as e:
            print(clr(f' \u2716  Cập nhật không thành công: {str(e)}\n    Hãy thử lại', 'fail'))