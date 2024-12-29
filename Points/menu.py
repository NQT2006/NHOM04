import Points
from Others.style import cls, clr, option

ACTION = {
    'p-l': Points.LookupAction,
    'p-u': Points.UpdateAction,
    'p-r': Points.RemoveAction,
    'p-s': Points.SearchAction,
}

def MenuAction(fn: list):
    if not fn:
        fn = ['p-m', None]
        cls()
        options = { '1': 'Tra cứu', '2': 'Chỉnh sửa', '3': 'Xóa bỏ', '4': 'Tìm kiếm' }
        pp = list(map(lambda k: '    ' + option(k, options[k]), options))
        print(' 📋 Quản lí Thông tin điểm')
        print('   '.join(pp + ['    ' + option('ctrl + c', 'Trở về', 43)]))
        try:
            while True:
                n = input('Chọn chức năng cho Thông tin điểm: ')
                if len(n) == 1 and '0' < n < '6':
                    fn[0] = list(ACTION.keys())[int(n)-1]
                    break
                else: print(clr(' \u2716  Chỉ nhập số ứng với các chức năng trên. Hãy thử lại!', 'fail'))
        except KeyboardInterrupt: return ['m-m']
    while fn[0] != 'p-m' and fn[0] in ACTION:
        fn = ACTION[fn[0]](*fn[1:])
    
    return fn