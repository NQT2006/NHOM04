from Class.document import Read, Write, GetOptions
from Others.style import clr, cls, header, option
import Others.class_input_test as KiemTra

EXIT = ['c-m', None]

def update(data, index, title):
    f = data[index]
    t = []
    pos = 0
    Test = [KiemTra.MaLop, KiemTra.TenLop, KiemTra.TongSoBan]
    while True:
        cls(title, '\n[!]\033[33mChú ý: Để bỏ qua các trường không muốn đổi, bấm Enter↵\033[0m',
            '\n', option('ctrl + c', 'Trở về Menu', 43))
        print('\t' + header(('\t').join(data[0]), 1))
        if len(f[1]) < 20: f[1] += ' '*(20 - len(f[1]))
        print('Từ:\t ' + '\t '.join(f))
        nt = list(map(lambda x: x if x[1] == '[' else ('\033[95m'+x+'\033[0m'), t)) + ['']
        value = input('Thành:\t ' + '\t '.join(nt) + '\033[95m').strip()
        print('', end='\033[0m')
        t.append(Test[pos](value) if value else ('\033[20;29m'+(' ')*len(f[pos])+'\033[0m'))
        if len(t) == 2 and len(t[1]) < 20: t[1] += ' '*(20 - len(t[1]))
        if pos == len(f) - 1: break
        else: pos += 1
    for i in range(len(t)):
        t[i] = t[i].strip() if not t[i][1] == '[' else f[i]
    return t

def UpdateAction(maLop):
    cls('\033[1m[3] Chỉnh sửa thông tin lớp\033[0m')
    data = Read()
    dsml = [l[0] for l in data]
    while True:
        try:
            if not maLop:
                maLop = GetOptions(data, 0, True, '1 lớp cần chỉnh sửa', 1, '    ')
            index = dsml.index(maLop)
            title = '\033[1m[3]\033[0m Chỉnh sửa thông tin lớp: \033[95m' + data[index][0] + '\033[0m'
            while True:
                newDoc = update(data, index, title)
                if newDoc == data[index]:
                    ext = input('[?] Bạn không chỉnh sửa gì. Muốn thoát chứ ? Enter↵(thoát) hoặc n(sửa lại): ')
                    if not ext:
                        cls(title)
                        print(clr(' \u2716  Cập nhật không thành công: Hủy chỉnh sửa.\nHãy thử lại!', 'fail'))
                        break
                    else: continue
                else:
                    ext = input('[?] Bạn muốn lưu lại chỉnh sửa này chứ ? Chọn Enter↵(lưu) hoặc n(sửa lại): ')
                    if not ext:
                        data[index] = newDoc
                        Write(data)
                        cls(title)
                        print(clr(' \u2795  Cập nhật thành công.\n', 'success'))
                        break
                    else: continue
            maLop = ''
        except KeyboardInterrupt:
            return EXIT
        except Exception as e:
            print(clr(' \u2716  Cập nhật không thành công: ' + str(e) + '.\nHãy thử lại!', 'fail'))