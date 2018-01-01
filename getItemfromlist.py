list1 = ['tomato', 'onion', 'butter', 'bread']
list2 = ['candy', 'icecream', 'lolipop', 'snikers']
list3 = ['tomato', 'onion', 'butter', 'bread']
while True:
  print('Todays our shop have:\n')
  print('List of items 1:\n')
  for x in list1: print(x)
  print('\n')
  print('List of items 2:\n')
  for x in list2: print(x)
  print('\n')
  print('List of items 3:\n')
  for x in list3: print(x)
  print('\n')
  g = input('From which list you wanna take item??(Give number): ')
  print('\n')
  g = int(g)
  if g == 1:
    get = list1
  elif g == 2:
    get = list2
  else:
    get = list3

  try:
    w = get.pop()
  except IndexError:
    print('\n')
    print('There is no more item in this list nr {}'.format(g))
    print('\n')
  else:
    print('\n')
    print('Here is your item {}'.format(w))
    print('\n')
  
