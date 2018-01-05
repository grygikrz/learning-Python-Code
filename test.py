def squared(arg):
    if isinstance(arg,int):
        return arg * arg
    elif arg.isdigit():
        arg = int(arg)
        return arg * arg
    else:
        return arg * len(arg)

#print(squared(5))
#print(squared("2"))
#print(squared("tim"))


#practice packing and unpacking dictionary
def pack(name=None, **kwargs):
    print(kwargs)

def unpack(firstname=None,lastname=None):
    if firstname and lastname:
        print('Hi there {} {}'.format(firstname,lastname))
    else:
        print('There is no firstname or lastname')

pack(name='Krzysztof',praca = 'administrator',lubi = 'muzyke')
unpack(**{'firstname':'Krzysztof','lastname':'Grawa'})

template = "Hi, I'm {name} and I love to eat {food}!"

def string_factory(values):
    lista = []
    for x in values:
        lista.append(template.format(name=x["name"],food=x["food"]))
    return lista

print(string_factory([{"name": "Michelangelo", "food": "PIZZA"}, {"name": "Garfield", "food": "lasagna"}]))

import collections

def word_count(words):
    dic = collections.OrderedDict()
    words = words.lower().split(' ')
    for w in words:
        if w in dic:
            dic[w] += 1
        else:
            dic[w] = 1
    return dic

print(word_count("I do not like it Sam I Am"))


TILES = ('-', ' ', '-', ' ', '-', '||',
         '_', '|', '_', '|', '_', '|', '||',
         '&', ' ', '_', ' ', '||',
         ' ', ' ', ' ', '^', ' ', '||'
)

for x in TILES:
    if x == '||':
        print('\n')
    else:
        print(x, end='')
