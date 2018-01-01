import random

def sucess(sec_num,howmany):
    print('Woow bravo you guess the number ({}) in {} times!'.format(sec_num,howmany))

def wrong(secret_num,mynum,howmany,leftnum):
    num = how_many_left(howmany,leftnum)
    print('Wrong. Try one more time! Number of left tryies is {}'.format(num))

    if secret_num > mynum:
        print ('\nYour number is less than secret number')
    else:
        print ('\nYour number is higher than secret number')

    return num

def how_many_left(howmany,leftnum):
    num = leftnum - howmany
    return num

def lose():
    print ('Sorry you loose!')
    v = input('\nWhana try again? (y/n) ')
    if v == 'y':
        main()
    else:
        return 'OVER!'

def main():
    howmany = 0
    leftnum = 5
    secret_num = random.randint(1,10)

    while True:
        howmany += 1

        if how_many_left(howmany,leftnum) < 1:
            lose()
            break

        num = input('Gues my secret number! ')

        if not num.isdigit():
            print('Sorry! This is not a number!')
            break

        if int(num) == secret_num:
            sucess(secret_num,howmany)
            break
        else:
            wrong(secret_num,int(num),howmany,leftnum)

main()
