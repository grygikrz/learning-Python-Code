import random
import os

words = ['apple','island','monkey','chest']
word = random.choice(words)
bad = []
good = []
number_of_tries = 3

def show_guess_board(word,good=[]):
    out = []
    for x in word:
      out.append('_')

    for x in range(len(word)):
        for z in range(len(good)):
            if word[x] == good[z]:
                out[x] = good[z]

    print(' '.join(out)+'\n')

    return out

def tryagain():
    global word
    q = input('Wanna try again (y)?')
    if q == 'y':
        main(word)
    else:
        print('Good Bye!')

def word_list_info(good,bad):
    print('Your list of good letters:\n')
    for x in good: print(x)
    print('\n')
    print('Your list of missed letters:\n')
    for x in bad: print(x)
    print('\n')

def wrong(good,bad):
    global number_of_tries
    print('\n---------------\n     Wrong\n--------------\n')
    print('\nYour number of tries: {}'.format(number_of_tries)+'\n')
    word_list_info(good,bad)
    number_of_tries -= 1
    if number_of_tries == 0:
      print('Sorry you lose!')
      return 'Over'
    tryagain()

def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

def success(good,bad):
    print('\n--------------------\n     Success\n--------------------\n')
    word_list_info(good,bad)
    main(word)

def main(word):
    global words
    global bad
    global good
    global number_of_tries

    clear()
    print('list of words:\n')
    for x in words: print(x)
    print('\n')

    s = show_guess_board(word,good)
    if word == ''.join(s):
      print('Congratulations You Won!')
      return 'Over'

    w = input('Guess the one letter of words from list:\n')

    if w in good or w in bad:
        print('You already entered this letter\n')
        tryagain()

    if w in word:
        good.append(w)
        success(good,bad)
    else:
        bad.append(w)
        wrong(good,bad)


main(word)
