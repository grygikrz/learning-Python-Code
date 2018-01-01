# Experimental new language lexer and parser

from sys import *

def open_file(filename):#prepare data
    data = open(filename,"r").read()
    return data

# lexer to create tokens
def readLines(filecontents):#prepare data
    tok = []
    for g in filecontents.split('\n'): #each line
        if g != '':
            tok.append(g)
    return tok

def splitTextToList(text): #prepare data
    tokens = []
    for x in text:
        split = x.split(' ')
        tokens.append(split)
    return tokens

def lexer(tok): #analize data
    token = []
    for x in tok:
        if x == 'print':
            token.append('PRINT')
        elif x == '==':
            token.append('EQEQ')
        elif x == 'return':
            token.append('RETURN')
        elif x == 'if':
            token.append('IF')
        elif x == 'endif':
            token.append('ENDIF')
        elif x.isdigit():
            token.append('INT')
        elif x.isalpha:
            token.append('STR')
    return token

def getTokens(tok): #get data
    tokens = []
    for c in tok:
        tokens.append(lexer(c))
    return tokens

def parser(tokens,raw): #parse data
    out = ''
    add = 0
    for x in range(len(tokens)):
        for y in range(len(tokens[x])):
            if 'PRINT' in tokens[x]:
                if 'INT' in tokens[x]:
                    out += ' '+raw[x][1]
                if 'STR' in tokens[x]:
                    out += ' '+raw[x][1]
            if 'IF' in tokens[x]:
                if 'INT' in tokens[x]:
                    number1 = raw[x][1]
                    for n in range(x, len(tokens[x])):
                        if 'INT' == tokens[x][n]:
                            number2 = raw[x][n]
                if 'EQEQ' in tokens[x]:
                    eqeq = raw[x][1]
                if 'RETURN' in tokens[x]:
                    ret = raw[x][1]
                if 'ENDIF' in tokens[x]:
                    end = raw[x][1]
                if number1 and number2 and eqeq and ret and end:
                    if number1 == number2:
                        out += 'true'
                    else:
                        out += 'false'
                else:
                    error('syntax error in if statement')
            out += '\n'
            break
    return out

def error(msg):
    raise Exception(msg)

def run():
    rawdata = open_file('code2.lany')
    data = readLines(rawdata)
#    print data
    listdata = splitTextToList(data)
#    print listdata
    tokens = getTokens(listdata)
#    print tokens
    print parser(tokens,listdata)


run()
