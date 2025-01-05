from Students.document import Read, Write
from Students.lookup import FIELDS, SELECTED_FIELDS
from Class.document import Read as ReadClassDocs
from Others import *
import Others.student_input_test as KiemTra

EXIT = ['s-m', None]

def update(data, index, output0, Test, dsml: list):
    f = data[index]
    t = [f[0]]
    pos = 1
    catch = ''
    output1 = 'Từ:\t' + '\t'.join(list(map(lambda fi: ' '*(FIELDS[fi][2] - len(f[fi])) + f[fi], SELECTED_FIELDS)))
    output2 = 'Thành:\t\033[35m' + ' '*FIELDS[0][2] + '\t'
    cls(output0)
    print(output1)
    while pos < 7:
        if catch: print(clr(f' \u2716  Cập nhật không thành công: {catch}\n     Hãy thử lại!', 'fail'))
        value = input(output2 + ' ').strip()
        print('', end='\033[0m')
        try:
            if not value:
                output2 += ' '*FIELDS[pos][2] + '\t'
                t.append(f[pos])
            else:
                value = Test[pos](value)
                if pos == 6 and value not in dsml:
                    raise Exception('Không tồn tại mã lớp ' + value)
                t.append(value)
                output2 += ('  ' if pos == 3 else '') + ' '*(FIELDS[pos][2] - len(value)) + value + '\t'
            if pos == 3:
                if f[pos] == t[pos]:
                    output2 += ' '*FIELDS[pos+1][2] + '\t'
                    t.append(f[pos+1])
                else:
                    tuoi = str(KiemTra.TinhTuoi(*(t[pos].split('-'))))
                    output2 += ' '*(FIELDS[pos][2] - len(tuoi)) + tuoi + '\t'
                    t.append(t[pos])
                    t[pos] = tuoi
                pos += 1
            pos += 1
            catch = ''
            cls(output0)
            print(output1)
        except Exception as e:
            catch = str(e)
            continue
    data[index] = t
    print(output2+'\033[0m')
    return data

def UpdateAction(maHocSinh: list, then: list = None):
    title = '\033[1m[3] Chỉnh sửa thông tin học sinh\033[0m'
    cls(title)
    data = Read()
    dsmhs = [d[0] for d in data]
    dsml = [d[0] for d in ReadClassDocs()]
    Test = [KiemTra.MaHocSinh, KiemTra.HoDem, KiemTra.Ten, 
        KiemTra.NgaySinh, None, KiemTra.SoDienThoai, KiemTra.MaLop]
    output0 = ''.join([
        '    ', option('Enter↵', 'Không thay đổi', 46), '\t',
        option('ctrl + c', 'Thoát' if then else 'Trở về Menu', 43), '\n\n\t',
        '\t'.join(list(map( lambda x: header(x, 1), [data[0][f] for f in SELECTED_FIELDS] )))
    ])
    while True:
        try:
            if not maHocSinh:
                maHocSinh = [KiemTra.MaHocSinh(query1('mã học sinh cần chỉnh sửa', 1))]
                if maHocSinh[0] not in dsmhs:
                    maHocSinh = None
                    raise Exception('Mã học sinh không tồn tại')
            ii = 0
            while ii < len(maHocSinh):
                index = dsmhs.index(maHocSinh[ii])
                o = f'{title}: \033[35m{maHocSinh[ii]}\033[0m\n{output0}'
                newData = update(data.copy(), index, o, Test, dsml)
                if newData == data:
                    ext = input(' 📣 Bạn không chỉnh sửa gì. ' +
                        'Muốn thoát chứ ? Chọn Enter↵(thoát) hoặc n(sửa lại): ')
                    if not ext:
                        print(clr(' \u2716  Cập nhật không thành công: Hủy chỉnh sửa', 'fail'))
                        ii += 1
                else:
                    data = newData
                    ext = input(' 📣 Bạn muốn lưu lại chỉnh sửa này chứ ?' +
                        ' Chọn Enter↵(lưu) hoặc n(sửa lại): ')
                    if not ext:
                        Write(data)
                        print(clr(' \u271a  Cập nhật thành công', 'success'))
                        ii += 1
            if then: return then
            maHocSinh = None
        except KeyboardInterrupt:
            if then: return then
            return EXIT
        except Exception as e:
            print(clr(f' \u2716  Cập nhật không thành công: {str(e)}\n    Hãy thử lại', 'fail'))
            if then:
                try: input(' 📣 \033[33mEnter để thoát\033[0m ')
                except: None
                return then