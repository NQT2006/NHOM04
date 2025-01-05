import Students as Students
from Others import *

ACTION = {
    's-l': Students.LookupAction,
    's-a': Students.AppendAction,
    's-u': Students.UpdateAction,
    's-r': Students.RemoveAction,
    's-s': Students.SearchAction,
}

def MenuAction(fn: list):
    if not fn:
        fn = ['s-m', None]
        cls()
        options = {
            '1': 'Tra cứu', '2': 'Thêm mới', '3': 'Chỉnh sửa',
            '4': 'Xóa bỏ', '5': 'Tìm kiếm'
        }
        pp = list(map(lambda k: '    ' + option(k, options[k]), options))
        print(' 🪪  Quản lí Thông tin học sinh')
        print('   '.join(pp + ['    ' + option('ctrl + c', 'Trở về', 43)]))
        try:
            while True:
                n = input('Chọn chức năng cho Thông tin học sinh: ')
                if len(n) == 1 and '0' < n < '6':
                    fn[0] = list(ACTION.keys())[int(n)-1]
                    break
                else: print(clr(' \u2716  Chỉ nhập số ứng với các chức năng trên. Hãy thử lại!', 'fail'))
        except KeyboardInterrupt:
            return ['m-m']
    while fn[0] != 's-m' and fn[0] in ACTION:
        fn = ACTION[fn[0]](*fn[1:])
    
    return fn