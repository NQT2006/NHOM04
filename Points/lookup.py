from Points.document import Read
from Others.style import bold, header

def lookupAcion():
    l = Read()
    index = 1
    h = '\t' + ('\t').join(l[0][:7]) + '\t' + ('\t').join(l[0][7:])
    print(header(h, 1))
    nl = map(lambda x: x[:6] + [x[7]+'\t'] + x[7:9] + [x[9]], l[1:])
    for fields in nl:
        print(bold(index) + '\t ' + ('\t ').join(fields[:9]) + '\t  ' + fields[9])
        index += 1