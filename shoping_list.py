items = []
def add_to_SL(item):
    global items
    items.append(item)
    print('Item added to the list! You have {} items in list'.format(len(items)))
    return items

def show_list():
    if items:
        print('\n'+'Here is your Shopping list:')
        for p in items: print(p)
        print('\n')
    else:
        print('Nothing here!')

def show_help():
    print('\n\n***Type "SHOW" show your items***\n\n')

def main():
    n = ''
    print('Welcome to your shoping list.\nTo read more type "HELP"\n')
    v = input('Add new item to the shopping list: ')
    if v in items:
        print('Item is already in the list')
    elif v == 'HELP':
        show_help()
    elif v == 'SHOW':
        show_list()
    elif v == 'DONE':
        print('Nothing was added. OVER!')
    elif v:
        add_to_SL(v)
    else:
        n = 'nothing'
        print('Nothing was added')

    if v != 'DONE' and n != 'nothing':
        while True:
            m = input('Add another(leave to over or type "DONE") ?: ')
            if not m:
                print ('Over')
                break
            elif m == 'DONE':
                break
            elif m == 'SHOW':
                show_list()
            elif m == 'HELP':
                show_help()
            elif m in items:
                print('Item is already in the list')
            else:
                add_to_SL(m)

    print('\n'+'Here is your Shopping list:')
    for p in items: print(p)

main()
