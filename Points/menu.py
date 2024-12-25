import Class.module as Class
from Others.style import cls, clr

ACTION = {
    'c-l': Class.LookupAction,
    'c-a': Class.AppendAction,
    'c-u': Class.UpdateAction,
    'c-r': Class.RemoveAction,
    'c-s': Class.SearchAction,
}

def MenuAction():
    fn = ''
    cls()
    print('1. Tra cứu\t2. Thêm mới\t3. Chỉnh sửa\t4. Xóa bỏ\t5. Tìm kiếm\t0. Trở về')
    while True:
        n = int(input('Chọn chức năng: \033[35m'))
        print('', end='\033[0m')
        if not n: return 'exit' # 'm-m'
        elif 0 < n < 6:
            fn = list(ACTION.keys())[n-1]
            break
        else: print(clr('[x] Chỉ nhập số ứng với các chức năng trên. Hãy thử lại!', 'fail'))

    while fn != 'c-m':
        fn = ACTION[fn]()
    
    return fn