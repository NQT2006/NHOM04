from Class.menu import clr, option, MenuAction as ClassMenu
from Students.menu import cls, MenuAction as StudentsMenu
from Points.menu import MenuAction as PointsMenu

ACTION = {
    'c-m': ClassMenu,
    's-m': StudentsMenu,
    'p-m': PointsMenu
}

def MenuAction():
    M = ['c-m', 's-m', 'p-m']
    CT = ['Thông tin lớp học', 'Thông tin học sinh', 'Thông tin điểm học sinh']
    try:
        cls()
        print('\n    ' +
            '    '.join(list(map(lambda i: option(str(i+1), CT[i]), range(3)))) +
            '    ' + option('ctrl + c', 'Thoát', 43)
        )
        while True:
            n = input('    Chọn chương trình quản lí: ').strip()
            if len(n) == 1 and '0' < n < '4': break
            print(clr(' \u2716  Đầu vào không hợp lệ: Chỉ chọn các lựa chọn đề xuất', 'fail'))
        return [M[int(n)-1], None]
    except KeyboardInterrupt: return ['exit']

def MainMenu(fn: list = None):
    if not fn: fn = MenuAction()
    while fn[0] != 'exit':
        if fn[0] == 'm-m':
            fn = MenuAction()
            continue
        fn = ACTION[fn[0]](fn[1])
    print('exit')
    print(clr(' ❌ Đã thoát chương trình\033[0m', 'fail'))

if __name__ == '__main__':
    MainMenu()