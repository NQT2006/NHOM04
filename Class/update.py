from Class.document import Read, Write, GetOptions
from Class.lookup import FIELDS, joinData
from Others.style import clr, cls, header, option
import Others.class_input_test as KiemTra

EXIT = ['c-m', None]

SELECTED_FIELDS = [0, 1, 2]

def update(data, index, output0, Test):
    f = data[index]
    t = [f[0]]
    pos = 1
    catch = ''
    output1 = 'Từ:\t' + '    '.join(list(map(lambda fi: ' '*(FIELDS[fi][2] - len(f[fi])) + f[fi], SELECTED_FIELDS)))
    output2 = 'Thành:\t\033[35m' + ' '*(FIELDS[0][2]+4)
    cls(output0)
    print(output1)
    while pos < 3:
        if catch: print(clr(f' \u2716  Cập nhật không thành công: {catch}\n     Hãy thử lại!', 'fail'))
        value = input(output2).strip()
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
            cls(output0)
            print(output1)
        except Exception as e:
            catch = str(e)
            continue
    data[index] = t
    print(output2+'\033[0m')
    return data

def UpdateAction(maLop: list, then: list = None):
    title = '\033[1m[3] Chỉnh sửa thông tin lớp\033[0m'
    cls(title)
    data = Read()
    dsml = [l[0] for l in data]
    Test = [KiemTra.MaLop, KiemTra.TenLop, KiemTra.TongSoBan]
    output0 = ''.join([
        '    ', option('Enter↵', 'Không thay đổi', 46), '\t',
        option('ctrl + c', 'Thoát' if then else 'Trở về Menu', 43), '\n\n\t',
        '  '.join(list(map( lambda x: header(x, 1), [data[0][f] for f in SELECTED_FIELDS] )))
    ])
    while True:
        try:
            if not maLop:
                maLop = [GetOptions(data, 0, True, '1 lớp cần chỉnh sửa', 1, '    ')]
            ii = 0
            while ii < len(maLop):
                index = dsml.index(maLop[ii])
                o = f'{title}: \033[35m{maLop[ii]}\033[0m\n\n{output0}'
                newData = update(data.copy(), index, o, Test)
                if newData == data:
                    save = input(' 📣 Bạn không chỉnh sửa gì. ' +
                        'Muốn thoát chứ ? Chọn Enter↵(thoát) hoặc n(sửa lại): ')
                    if not save:
                        print(clr(' \u2716  Cập nhật không thành công: Hủy chỉnh sửa', 'fail'))
                        ii += 1
                else:
                    data = newData
                    save = input(' 📣 Bạn muốn lưu lại chỉnh sửa này chứ ?' +
                        ' Chọn Enter↵(lưu) hoặc n(sửa lại): ')
                    if not save:
                        Write(data)
                        print(clr(' \u271a  Cập nhật thành công', 'success'))
                        ii += 1
            if then: return then
            maLop = None
        except KeyboardInterrupt:
            if then: return then
            return EXIT
        except Exception as e:
            print(clr(' \u2716  Cập nhật không thành công: ' + str(e) + '.\nHãy thử lại!', 'fail'))
            if then:
                try: input(' 📣 \033[33mEnter↵ để thoát\033[0m ')
                except: None
                return then