from Students.document import Read, Write
from Points.document import Read as ReadPointDocs, Write as WritePointDocs
from Others.style import clr, cls, bold, query1
import Others.student_input_test as KiemTra

EXIT = ['s-m', None]

def remove(data: list, dshs: list, maHocSinh: list):
    for hs in maHocSinh:
        try: hs = KiemTra.MaHocSinh(hs)
        except Exception as e: raise Exception(f'{str(e)} (Mã học sinh {hs})')
        if hs not in dshs:
            maHocSinh.remove(hs)
            continue
        index = dshs.index(hs)
        data = data[:index] + data[index+1:]
    if not len(maHocSinh): raise Exception('Không tìm thấy học sinh nào')
    return data

def RemoveAction(maHocSinh: list):
    title = bold('[4] Xóa bỏ thông tin học sinh')
    cls(title)
    data = Read()
    dshs = [l[0] for l in data]
    pdata = ReadPointDocs()
    while True:
        try:
            if not maHocSinh:
                maHocSinh = query1('những mã học sinh cần xóa (Cách nhau bằng "dấu phẩy")', 1).split(',')
            else:
                print(f'    {len(maHocSinh)} mã học sinh cần xóa: {', '.join(maHocSinh[:7])+ (',...' if len(maHocSinh)>6 else '')}')
            data = remove(data, dshs.copy(), maHocSinh)
            q = input(f'Bạn chắc chắn muốn xóa {len(maHocSinh)} học sinh này không ? (Chọn Enter-có hoặc n-không): ').strip()
            if not q:
                pd = pdata.copy()
                Write(data)
                dsdhs = list(filter(lambda l: l[0] in maHocSinh, pd))
                for hs in dsdhs: pd.remove(hs)
                WritePointDocs(pd)
                print(clr(f' \u268a  Xóa thành công học sinh {', '.join(maHocSinh)}\n', 'success'))
            else: raise Exception('Hủy xóa')
        except KeyboardInterrupt:
            return EXIT
        except Exception as e:
            print(clr(' \u2716  Xóa không thành công: ' + str(e) + '\n', 'fail'))