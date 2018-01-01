# Experimental new language lexer and parser

from sys import *

def open_file(filename):
    data = open(filename,"r").read()
    return data

# lexer to create tokens
def lexer(filecontents):
    tokens = []
    token = {}
    c = 0
    for g in filecontents.split('\n'): #each line
        if g != '':
            tokens.append(g)

    for x in range(len(tokens)):
         # each command
         token[x] = {}
         for z in tokens[x].split(' '):
            if z == 'print':
                if 'command' not in token[x]:
                    token[x]['command'] = {}
                token[x]['command'][c] = z
            elif z.isdigit():
                if 'int' not in token[x]:
                    token[x]['int'] = {}
                token[x]['int'][c] = z
            elif z.isalpha:
                if '"' in tokens[x]:
                    z = z.replace('"','')
                    if 'str' not in token[x]:
                        token[x]['str'] = {}
                    token[x]['str'][c] = z
            else:
                break
            c += 1

    return token

# parse created token and print out
def parser(token):
    out = ''
    for x in token:
        if 'command' in token[x]:
            if 'print' in token[x]['command']:
                for z in token[x]['command']:
                    out += ''
        if 'int' in token[x]:
            for v in token[x]['int']:
                out += ' '+token[x]['int'][v]
        if 'str' in token[x]:
            for v in token[x]['str']:
                out += ' '+token[x]['str'][v]
        out += '\n'
    return out

def run():
    data = open_file('code.lany')
    tokens = lexer(data)
    print parser(tokens)

run()
