from Students.document import Read, Add
from Class.document import ClassOptions, Read as ReadClassDoc
from Others.style import clr, cls, bold, quest1
import Others.student_input_test as KiemTra

MODE = {
    'exit': ['s-m', None],
    'f1':   ['s-l', None],
    'f3':   ['s-u', None],
    'f4':   ['s-r', None],
    'f5':   ['s-s', None]
}

def getInput(output: str, form: dict, index: int, alert: str, sub: str, test, ap = True):
    x = ''
    if not (form and len(form) > index):
        while True:
            try:
                x = test(quest1(alert + ((' '+sub) if sub else ''), 1))
                if form: form.append(x)
                break
            except Exception as e:
                print(clr(' ❌ Đầu vào không hợp lệ: '+ str(e) +'\nHãy thử lại!', 'fail'))
    if not form: return x
    if ap:
        output += '\n    ' + alert + ': \033[35m' + (x or form[index]) + '\033[0m'
        cls(output)
    return [output, form]

def AppendAction(form: list):
    title = bold('[2] Thêm mới Thông tin học sinh')
    cls(title)
    data = Read()
    classData = ReadClassDoc()
    dsmhs = [d[0] for d in data]
    if not form: form = []
    while True:
        output = '' + title
        try:
            if not len(form):
                maHocSinh = getInput(0, 0, 0, 'Mã học sinh cần thêm', 0, KiemTra.MaHocSinh)
                if maHocSinh in MODE: return MODE[maHocSinh]
                maHocSinh = maHocSinh.title()
                if maHocSinh in dsmhs:
                    maHocSinh = ''
                    raise Exception(f'Mã học sinh {maHocSinh} đã tồn tại')
                form.append(maHocSinh)
            output += '\n    Mã học sinh: \033[35m' + form[0] + '\033[0m'
            cls(output)
            
            if len(form) == 1:
                form += getInput(0, 0, 1, 'Họ và tên', 0, KiemTra.HoTen)
            output += f'\n    Họ và tên: \033[35m{form[1]} {form[2]}\033[0m'
            cls(output)
            form.append('')
            output, form = getInput(
                output, form,
                4, 'Ngày sinh',
                '(Định dạng: <Năm>-<Tháng>-<Ngày>)',
                KiemTra.NgaySinh, False
            )
            if True:
                nam, thang, ngay = form[4].split('-')
                tuoi = str(KiemTra.TinhTuoi(nam, thang, ngay))
                form[3] = tuoi
                output += f'\n    Tuổi: \033[35m{tuoi}\033[0m'
                output += f'\n    Ngày sinh: \033[35mNgày {ngay} tháng {thang} năm {nam}\033[0m'
                cls(output)
            output, form = getInput(
                output, form,
                5, 'Số điện thoại',
                '(10 chữ số)',
                KiemTra.SoDienThoai
            )
            maLop = ClassOptions(
                classData, 0, True,
                'Chọn lớp (Chỉ chọn 1 lớp)', 1, '    ', {
                'a': 'Thêm lớp mới'
            })
            # if maLop == 'a': return ['c-m', ['c-a', None, ['s-m', ['s-a', form]]]]
            form.append(maLop)
            Add(form)
            dsmhs.append(form[0])
            output += f'\n    Mã lớp: \033[35m{maLop}\033[0m'
            cls(output)
            print(clr(f'[+] Thêm học sinh mã {form[0]} hoàn tất!\n', 'green'))
            form = []
        except KeyboardInterrupt:
            print('', end='\033[0m')
            return MODE['exit']
        except Exception as e:
            print(clr(' ❌ Thêm không thành công: ' + str(e) + '\nHãy thử lại!', 'fail'))
            
            
