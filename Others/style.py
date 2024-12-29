ENDC = '\033[0m'
BOLD = '\033[1m'

COLOR = {
    0: '',
    'success': '\033[92m',
    'fail': '\033[31m'
}

HEADER = {
    0: '',
    1: '\033[7;31;41m',
    2: '\033[7;34;44m',
    3: '\033[7;37;44m',
}

COLOR.get('')
def cls(*text):
    print('\033[H\033[J', end='\033[H\033[J')
    print('\033[H\033[J', end='\033[53m\033[4m\033[94m \ufe4f\U0001329D\ufe4f\U00013081\ufe4f ' +
    '\u0043h\u01b0\u01a1n\u0067 \u0054r\u00ecnh \u0051u\u1ea3n \u004c\u00fd \u0048\u1ecdc \u0053inh ' +
    '\u23af \u004eh\u00f3m \u0034     \U0001F384\U0001F381\033[0m\n')
    if text: print(*text)

def query1(alert: str, level: int):
    x = input(f'{'  '*(level-1)} \033[2;37;39m✎\033[0m  Nhập {alert}: \033[35m').strip()
    print('', end='\033[0m')
    return x

def query2(alert: str, level: int):
    x = input(f'{'  '*(level-1)} \033[2;37;39m⊞\033[0m  Chọn {alert}: \033[35m').strip()
    print('', end='\033[0m')
    return x

def tip(alert: str, level: int):
    print(f'{'  '*(level-1)} 📣 \033[33m{alert}\033[0m')

def option(key: str, name: str, keyCol: int = 29, nameCol: int = 39, borderCol: int = 39):
    return f'\033[7;{keyCol};{borderCol}m {key} \033[0m\033[4;{borderCol};{nameCol}m {name}\u2595\033[0m'

def clr(text: str, color: str = 0):
    return COLOR[color] + str(text) + ENDC

def bold(text: str, color: str = 0):
    return COLOR[color] + BOLD + str(text) + ENDC

def header(text: str, header: str = 0):
    return HEADER[header] + str(text) + ENDC