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
    try:
        cls()
        ct = ['Thông tin lớp học', 'Thông tin học sinh', 'Thông tin điểm học sinh']
        print('\n    ' +
            '    '.join(list(map(lambda i: option(str(i+1), ct[i]), range(3)))) +
            '    ' + option('ctrl + c', 'Thoát', 43)
        )
        n = input('    Chọn chương trình quản lí: ')
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