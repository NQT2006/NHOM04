from random import random

ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

COLOR = {
    0: '',
    'purple': '\033[35m',
    'blue': '\033[34m',
    'cyan': '\033[37m',
    'green': '\033[92m',
    'gray': '\033[2;37;39m',
    'fail': '\033[31m',
    'note': '\033[33m',
}

HEADER = {
    0: '',
    1: '\033[7;31;41m',
    2: '\033[7;37;44m',
    3: '\033[7;37;44m',
}

COLOR.get('')
# ✎
def cls(*text):
    print('\033[H\033[J', end='\033[H\033[J')
    print('\033[H\033[J', end='\033[53m\033[4m\033[94m ﹏𓊝﹏𓂁﹏ Chương Trình Quản Lý Học Sinh - Nhóm 4     🎄🎁\033[0m\n')
    if text: print(*text)

def quest1(alert: str, level: int):
    x = input(f'{'  '*(level-1)} \033[2;37;39m✎\033[0m  Nhập {alert}: \033[35m').strip()
    print('', end='\033[0m')
    return x

def quest2(alert: str, level: int):
    x = input(f'{'  '*(level-1)} \033[2;37;39m✎\033[0m  Chọn {alert}: \033[35m').strip()
    print('', end='\033[0m')
    return x

def option(key: str, name: str, keyCol: int = 29, nameCol: int = 39, borderCol: int = 39):
    return f'\033[7;{keyCol};{borderCol}m {key} \033[0m\033[4;{borderCol};{nameCol}m {name}\u2595\033[0m'

def clr(text: str, color: str = 0):
    return COLOR[color] + str(text) + ENDC
def printc(text: str, color: str = 0):
    print(COLOR[color] + str(text) + ENDC)

def bold(text: str, color: str = 0):
    return COLOR[color] + BOLD + str(text) + ENDC

def underline(text: str, color: str = 0):
    return COLOR[color] + UNDERLINE + str(text) + ENDC

def header(text: str, header: str = 0):
    return HEADER[header] + str(text) + ENDC