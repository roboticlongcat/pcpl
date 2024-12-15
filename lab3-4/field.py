def field(items, *args):
    assert len(args) > 0
    values = []
    if len(args) == 1:
        for item in items:
            value = item[args[0]]
            if value is not None:
                values.append(value)
    else:
        for item in items:
            value = {arg: item[arg] for arg in args if item[arg] is not None}
            if value:
                values.append(value)
    return values

def main():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    values = field(goods, 'title')
    print(*values, sep=', ')
    values = field(goods, 'title', 'price')
    print(*values, sep=', ')
if __name__ == '__main__':
    main()
