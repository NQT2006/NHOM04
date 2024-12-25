from Class.document import Read, Add
from Others.style import clr, cls, bold, quest1
import Others.class_input_test as KiemTra

MODE = {
    'exit': ['c-m', None],
    'f1':   ['c-l', None],
    'f3':   ['c-u', None],
    'f4':   ['c-r', None],
    'f5':   ['c-s', None]
}

def getInput(output: str, alert: str, sub: str, test):
    x = ''
    while True:
        try:
            x = test(quest1(alert + ((' '+sub) if sub else ''), 1))
            break
        except Exception as e:
            print(clr(' ❌ Đầu vào không hợp lệ: '+ str(e) +'\nHãy thử lại!', 'fail'))
    output += '\n    ' + alert + ': \033[35m' + x + '\033[0m'
    cls(output)
    return [output, x]

def AppendAction(maLop: str = None, then: list = None):
    title = bold('[2] Thêm mới thông tin lớp')
    cls(title)
    data = Read()
    dsml = [l[0] for l in data]
    while True:
        output = '' + title
        try:
            if not maLop:
                output, maLop = getInput(output, 'Mã lớp cần thêm', 0, KiemTra.MaLop)
                if maLop == 'exit': return MODE['exit']
                else: maLop = maLop.upper()
                if maLop in dsml:
                    maLop = ''
                    raise Exception(f'Mã lớp {maLop} đã tồn tại')
            else:
                print(f'    Mã lớp:  \033[35m{maLop}\033[0m' )

            output, tenLop = getInput(output, 'Tên lớp', 0, KiemTra.TenLop)
            output, tongSoBan = getInput(output, 'Tổng số bàn', '(Tối đa 40)', KiemTra.TongSoBan)
            
            Add([maLop, tenLop.title(), tongSoBan])
            dsml.append(maLop)
            if then: return then
            data += [[maLop, tenLop.title(), tongSoBan]]
            print(clr(f'[+] Thêm lớp mã {maLop} hoàn tất!\n', 'green'))
            maLop = ''
        except KeyboardInterrupt:
            print('', end='\033[0m')
            return MODE['exit']
        except Exception as e:
            print(clr(' ❌ Thêm không thành công: ' + str(e) + '\nHãy thử lại!', 'fail'))