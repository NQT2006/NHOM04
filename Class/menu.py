import Class.module as Class
from Others.style import cls, clr, option

ACTION = {
    'c-l': Class.LookupAction,
    'c-a': Class.AppendAction,
    'c-u': Class.UpdateAction,
    'c-r': Class.RemoveAction,
    'c-s': Class.SearchAction,
}

def MenuAction(fn: list):
    if not fn:
        fn = ['c-m', None]
        cls()
        options = {
            '1': 'Tra cứu', '2': 'Thêm mới', '3': 'Chỉnh sửa',
            '4': 'Xóa bỏ', '5': 'Tìm kiếm'
        }
        pp = list(map(lambda k: '    ' + option(k, options[k]), options))
        print('    Quản lí Thông tin lớp học')
        print('   '.join(pp + ['    ' + option('ctrl + c', 'Trở về', 43)]))
        try:
            while True:
                n = input('Chọn chức năng cho Thông tin lớp học: ')
                if len(n) == 1 and '0' < n < '6':
                    fn[0] = list(ACTION.keys())[int(n)-1]
                    break
                else: print(clr('[x] Chỉ nhập số ứng với các chức năng trên. Hãy thử lại!', 'fail'))
        except KeyboardInterrupt:
            return ['exit']
    while fn[0] != 'c-m':
        fn = ACTION[fn[0]](*fn[1:])
    
    return fn