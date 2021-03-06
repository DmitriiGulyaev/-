import os

dict_maps = {
    'Pro': {'mtd1': ('0x0', '0x100000'),
            'mtd2': ('0x100000', '0x200000'),
            'mtd3': ('0x200000', '0x1600000'),
            'mtd4': ('0x1600000', '0x1700000'),
            'mtd5': ('0x1700000', '0x1b00000'),
            'mtd6': ('0x1b00000', '0x1f00000'),
            'mtd7': ('0x1f00000', '0x3d00000'),
            'mtd8': ('0x3d00000', '0x5b00000'),
            'mtd9': ('0x5b00000', '0x8d00000'),
            'mtd10': ('0x8d00000', '0xbf00000'),
            'mtd11': ('0xbf00000', '0xfb00000'),
            'mtd12': ('0xfb00000', '0xfc00000')},
    'WiFire S1500.NBN': {'mtd1': ('0x0', '0x100000'),
                         'mtd2': ('0x100000', '0x200000'),
                         'mtd3': ('0x200000', '0x1600000'),
                         'mtd4': ('0x1600000', '0x1700000'),
                         'mtd5': ('0x1700000', '0x1b00000'),
                         'mtd6': ('0x1b00000', '0x1f00000'),
                         'mtd7': ('0x1f00000', '0x4d00000'),
                         'mtd8': ('0x4d00000', '0x7b00000'),
                         'mtd9': ('0x7b00000', '0x7c00000'),
                         'mtd10': ('0x7c00000', '0x7f80000')},
    'Beeline SmartBox GIGA': {'mtd0': ('0x0', '0x100000'),
                              'mtd1': ('0x100000', '0x200000'),
                              'mtd2': ('0x200000', '0x300000'),
                              'mtd3': ('0x300000', '0x400000'),
                              'mtd4': ('0x400000', '0xa00000'),
                              'mtd5': ('0xa00000', '0x1000000'),
                              'mtd6': ('0x1000000', '0x2800000'),
                              'mtd7': ('0x2800000', '0x4000000'),
                              'mtd8': ('0x4000000', '0x4800000'),
                              'mtd9': ('0x4800000', '0x5400000'),
                              'mtd10': ('0x5400000', '0x7c00000')},
    'TURBO+': {'mtd0': ('0x0', '0x100000'),
               'mtd1': ('0x100000', '0x200000'),
               'mtd2': ('0x200000', '0x300000'),
               'mtd3': ('0x300000', '0x400000'),
               'mtd4': ('0x400000', '0xa00000'),
               'mtd5': ('0xa00000', '0x1000000'),
               'mtd6': ('0x1000000', '0x3000000'),
               'mtd7': ('0x3000000', '0x5000000'),
               'mtd8': ('0x5000000', '0x6400000'),
               'mtd9': ('0x6400000', '0x7f80000'),
               'mtd10': ('0x7f80000', '0x8000000')},
    'TURBO': {'mtd0': ('0x0', '0x100000'),
              'mtd1': ('0x100000', '0x200000'),
              'mtd2': ('0x200000', '0x300000'),
              'mtd3': ('0x300000', '0x400000'),
              'mtd4': ('0x400000', '0xa00000'),
              'mtd5': ('0xa00000', '0x1000000'),
              'mtd6': ('0x1000000', '0x3000000'),
              'mtd7': ('0x3000000', '0x5000000'),
              'mtd8': ('0x5000000', '0x6400000'),
              'mtd9': ('0x6400000', '0x7e00000'),
              'mtd10': ('0x8000000', '0xfc00000')},
    'S3Eti': {'mtd0': ('0x0', '0x100000'),
              'mtd1': ('0x100000', '0x200000'),
              'mtd2': ('0x200000', '0x300000'),
              'mtd3': ('0x300000', '0x400000'),
              'mtd4': ('0x400000', '0xa00000'),
              'mtd5': ('0xa00000', '0x1000000'),
              'mtd6': ('0x1000000', '0x3000000'),
              'mtd7': ('0x3000000', '0x5000000'),
              'mtd8': ('0x5000000', '0x6400000'),
              'mtd9': ('0x6400000', '0x7f80000')},
    'RT-FE-1': {'mtd0': ('0x0', '0x100000'),
                'mtd1': ('0x100000', '0x200000'),
                'mtd2': ('0x200000', '0x300000'),
                'mtd3': ('0x300000', '0x400000'),
                'mtd4': ('0x400000', '0xa00000'),
                'mtd5': ('0xa00000', '0x1000000'),
                'mtd6': ('0x1000000', '0x3000000'),
                'mtd7': ('0x3000000', '0x5000000'),
                'mtd8': ('0x5000000', '0x6400000'),
                'mtd9': ('0x6400000', '0x7e00000'),
                'mtd10_hz': ('0x7e00000', '0x7f80000')},
    'Beeline SmartBox Flash (Arcadyan WG443223)': {'mtd0': ('0x0', '0x7f80000'),
                                                   'mtd1': ('0x0', '0x100000'),
                                                   'mtd2': ('0x100000', '0x200000'),
                                                   'mtd3': ('0x200000', '0x300000'),
                                                   'mtd4': ('0x300000', '0x2300000'),
                                                   'mtd5': ('0x720000', '0x2300000'),
                                                   'mtd6': ('0x2300000', '0x4300000'),
                                                   'mtd7': ('0x2720000', '0x4300000'),
                                                   'mtd8': ('0x4300000', '0x4500000'),
                                                   'mtd9': ('0x4500000', '0x4600000'),
                                                   'mtd10': ('0x4600000', '0x4800000'),
                                                   'mtd11': ('0x4800000', '0x4900000'),
                                                   'mtd12': ('0x4900000', '0x7f80000')},
    '?????? (Arcadyan WG430223)': {'mtd0': ('0x0', '0x7f80000'),
                                'mtd1': ('0x0', '0x100000'),
                                'mtd2': ('0x100000', '0x200000'),
                                'mtd3': ('0x200000', '0x300000'),
                                'mtd4': ('0x300000', '0x2300000'),
                                'mtd5': ('0x720000', '0x2300000'),
                                'mtd6': ('0x2300000', '0x4300000'),
                                'mtd7': ('0x2720000', '0x4300000'),
                                'mtd8': ('0x4300000', '0x4500000'),
                                'mtd9': ('0x4500000', '0x4600000'),
                                'mtd10': ('0x4600000', '0x4800000'),
                                'mtd11': ('0x4800000', '0x4900000'),
                                'mtd12': ('0x4900000', '0x7f80000')}
}


def mid_just(st, maxi, char=' '):
    st = st.rjust((maxi - len(st)) // 2 + len(st), char)
    return st.ljust(maxi, char)


def print_map(key):
    global dict_maps
    mapa = dict_maps[key]
    w = 0
    for y in mapa.keys():
        if len(y) > w:
            w = len(y)
    print('router: ' + key)
    print('', mid_just('MTD', w + 3), mid_just('START', 12), mid_just('Size', 12), '', sep='|')
    for y in mapa.keys():
        print('', mid_just(y, w + 3), mid_just(mapa[y][0], 12), mid_just(mapa[y][1], 12), '', sep='|')


def make_dir(name):  # ?????????????? ???????????????????? ?? ?????????????????? ?? ??????
    if name == '':
        name = 'mtds'
    lst = [j for j in range(15)]
    for j in lst:
        s = name + ('' if j == 0 else str(j))
        if not os.path.isdir(s):
            os.mkdir(s)
            print('?????????????? ????????????????????: ' + os.getcwd() + ('\\' if '\\' in os.getcwd() else '/') + s)
            return s


def cut_a_block(file, start, end, new_file):
    global save_dir
    with open(file, "rb") as file:
        file.seek(int(start, 16), 0)
        size = int(end, 16) - int(start, 16)
        # print(size)
        byte = file.read(size)
        new_file = open(save_dir + ('\\' if '\\' in os.getcwd() else '/') + new_file + '.bin', 'wb')
        new_file.write(byte)
        new_file.close()


def make_mtds(data, mp):
    for j in mp:
        cut_a_block(data, mp[j][0], mp[j][1], j)
        print(j + ' ready')


def print_lst(lst):
    j = 0
    for z in lst:
        print(j * ' ' + str(j) + '. ' + z)
        j += 1


source_dir = os.getcwd()

num_name = dict()
k = 0
for i in dict_maps:
    num_name[str(k)] = i
    k += 1
while True:
    turn = False
    while True:
        print('?????????????????? ???????????? ????????????????:')
        print_lst(dict_maps.keys())
        mapper = input('?????????????? ?????????? ?????????????? ????????????:\t\t')
        try:

            if int(mapper) in range(len(dict_maps.keys())):
                break
            else:
                print('???????????????????????? ???????? ???????????????????? ??????????')
        except ValueError:
            print('???????????????????????? ???????? ???????????????????? ??????????')

    print_map(num_name[mapper])
    print('???????????? ?????????????????(yes/no)', end='\t\t')
    while True:
        q = input().lower()
        if q == 'yes':
            turn = True
            break
        elif q == 'no':
            break
        else:
            print('???????????????????????? ????????, ???????????????????? ?????????? (yes/no)', end='\t\t')
    if turn:
        break

print('???????????????? ???????? ???????????? ???????????????????? ?? ?????? ???? ????????????????????, ?????? ?? ?????????????????????? ????????????')

while True:
    print('?????????? ?????????????? ????????????????????:')
    print_lst(os.listdir())
    source = input('?????????????? ?????????? ?????????????????? ??????????\t\t')
    try:
        if int(source) in range(len(os.listdir())):
            break
        else:
            print('???????????????????????? ???????? ???????????????????? ??????????')
    except ValueError:
        print('???????????????????????? ???????? ???????????????????? ??????????')

name_dir = input('?????????????? ?????? ??????????(???????? ???????????????? ???????????? ?????????? ?????????? mtd*)\t\t')
save_dir = make_dir(name_dir)
make_mtds(os.listdir()[int(source)], dict_maps[num_name[mapper]])
