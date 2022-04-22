from prettytable import PrettyTable

all_maps = dict()


def add_map():
    global all_maps
    name = input('введите имя роутера:\t')
    if name == 'exit':
        return 'exit'
    print('введите макет:')
    s = list(iter(input, ''))
    separator = '	'
    map_mtd = dict()

    for i in s:
        if '	' in i:
            i = i.split(separator)
            map_mtd['' if 'mtd' in i[0] else 'mtd' + i[0]] = ('0x' + i[1].lower(), '0x' + i[2].lower())

    x = PrettyTable()
    x.field_names = ['MTD', 'Start Address', 'Size Partition']
    for i in map_mtd:
        x.add_row([i, map_mtd[i][0], map_mtd[i][1]])

    print(x)
    # создать csv с именем name и построчно сделать map(,)
    b = input('Добавить макет(yes/no)  ').lower()
    while True:
        if b == 'yes' or b == 'no':
            break
    if b == 'yes':
        all_maps[name] = map_mtd.copy()

    print('Последний созданный макет:\n', map_mtd)
    print('Все макеты:\n', all_maps)



while True:
    try:
        if add_map() == 'exit':
            break
    except IndexError:
        print('Упс, ошибочка. Пожалуйста, продолжайте...')

print(all_maps)
