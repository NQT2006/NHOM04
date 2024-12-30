from Class.document import Read, Write
from Others.style import clr, cls, bold, query1, option
import Others.class_input_test as KiemTra

EXIT = ['c-m', None]

def getInput(output: str, alert: str, sub: str, test):
    x = ''
    while True:
        try:
            x = test(query1(alert + ((' '+sub) if sub else ''), 1))
            break
        except Exception as e:
            print(clr(' \u2716  Đầu vào không hợp lệ: '+ str(e) +'\nHãy thử lại!', 'fail'))
    output += '\n    ' + alert + ': \033[35m' + x + '\033[0m'
    cls(output)
    return [output, x]

def AppendAction(maLop: str = None, then: list = None):
    title = bold('[2] Thêm mới thông tin lớp')
    cls(title)
    data = Read()
    dsml = [l[0] for l in data]
    while True:
        output = title + '\n    ' + option('ctrl + c','Thoát' if then else 'Trở về Menu', 43)
        try:
            if not maLop:
                output, maLop = getInput(output, 'Mã lớp cần thêm', 0, KiemTra.MaLop)
                if maLop == 'exit': return EXIT
                if maLop in dsml:
                    maLop = ''
                    raise Exception(f'Mã lớp {maLop} đã tồn tại')
            else: print(f'    Mã lớp:  \033[35m{maLop}\033[0m' )

            output, tenLop = getInput(output, 'Tên lớp', 0, KiemTra.TenLop)
            output, tongSoBan = getInput(output, 'Tổng số bàn', '(Tối đa 40)', KiemTra.TongSoBan)
            
            data.append([maLop, tenLop, tongSoBan])
            data.sort(key=lambda d: d[0])
            Write(data)
            dsml.append(maLop)
            if then: return then
            data += [[maLop, tenLop, tongSoBan]]
            print(clr(f'[+] Thêm lớp mã {maLop} hoàn tất!\n', 'success'))
            maLop = ''
        except KeyboardInterrupt:
            if then: return then
            return EXIT
        except Exception as e:
            print(clr(' \u2716  Thêm không thành công: ' + str(e) + '\nHãy thử lại!', 'fail'))