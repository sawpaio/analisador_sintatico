######## Implementação de um Analisador Léxico/Sintático
####### Prova 2
###### 05/06/2020
##### Author: Lucas Sampaio de Melo
#### Version: v1.2

import ply.yacc as yacc
import ply.lex as lex
import sys

# Lista das chaves que podem ser usadas na expressão númerica (operações e atributos).
tokens = [
    "INTEIRO",
    "FLOAT",
    "NOME",
    "ADICAO",
    "SUBTRACAO",
    "DIVISAO",
    "MULTIPLICACAO",
    "IGUALDADE"
]

t_SUBTRACAO = r'\-'
t_ADICAO = r'\+'
t_IGUALDADE = r'\='
t_DIVISAO = r'\/'
t_MULTIPLICACAO = r'\*'

# Variavel usada para ignorar os espaços vazios (caso contenha) quando o usuario digitar.
t_ignore = r' '

# Declaração de números floats (números com ponto ex: 0.125)
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

# Declaração de números inteiros
def t_INTEIRO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Declaração do recebimento de caracteres.
def t_NOME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = "NOME"
    return t

# Declaração de quando o programa recebe um caractere não usado,
# mas que o programa continua executando.
def t_error(t):
    print("caractere não usado, mas continuando o processo..")
    t.lexer.skip(1)

lexer = lex.lex()

# Declaração de regras da biblioteca do PLY, para que o programa
# não faça ações inesperadas com o recebimento de palavras maíusculas ou símbolos.
precedence = (
    ('left', 'ADICAO', 'SUBTRACAO'),
    ('left', 'MULTIPLICACAO', 'DIVISAO')
)


def p_calc(p):
    '''
    calculadora	:	expressao
            |	var_assign
            |	empty
    '''
    print("Resultado da expressão Matemática: {}".format((run(p[1]))))


def p_var_assign(p):
    '''
    var_assign	:	NOME IGUALDADE expressao
    '''
    p[0] = (p[2], p[1], p[3])


def p_empty(p):
    '''
    empty :
    '''
    p[0] = None


def p_expressao(p):
    '''
    expressao	:	expressao MULTIPLICACAO expressao
                |	expressao DIVISAO expressao
                |	expressao ADICAO expressao
                |	expressao SUBTRACAO expressao
    '''
    p[0] = (p[2], p[1], p[3])


def p_expressao_var(p):
    '''
    expressao	:	NOME
    '''
    p[0] = ('var', p[1])


def p_expressao_int_float(p):
    '''
    expressao	:	INTEIRO
                |	FLOAT
    '''
    p[0] = p[1]


def p_error(p):
    print("syntax error")


parser = yacc.yacc()

# dictionary of names
env = {}


def run(p):
    global env
    if (type(p) == tuple):
        if (p[0] == '+'):
            if type(p[1]) == int:
                print("Inteiro: {}".format(p[1]))
            if type(p[0]) == str:
                print("Symbol/Operador: {}".format(p[0]))
            if type(p[1]) == int:
                print("Inteiro: {}".format(p[2]))
            return run(p[1]) + run(p[2])
        elif (p[0] == '-'):
            if type(p[1]) == int:
                print("Inteiro: {}".format(p[1]))
            if type(p[0]) == str:
                print("Symbol/Operador: {}".format(p[0]))
            if type(p[1]) == int:
                print("Inteiro: {}".format(p[2]))
            return run(p[1]) - run(p[2])
        elif (p[0] == '*'):
            if type(p[1]) == int:
                print("Inteiro: {}".format(p[1]))
            if type(p[0]) == str:
                print("Symbol/Operador: {}".format(p[0]))
            if type(p[1]) == int:
                print("Inteiro: {}".format(p[2]))
            return run(p[1]) * run(p[2])
        elif (p[0] == '/'):
            if type(p[1]) == int:
                print("Inteiro: {}".format(p[1]))
            if type(p[0]) == str:
                print("Symbol/Operador: {}".format(p[0]))
            if type(p[1]) == int:
                print("Inteiro: {}".format(p[2]))
            return run(p[1]) / run(p[2])
        elif (p[0] == '='):
            if type(p[1]) == int:
                print("Inteiro: {}".format(p[1]))
            if type(p[0]) == str:
                print("Symbol/Operador: {}".format(p[0]))
            if type(p[1]) == int:
                print("Inteiro: {}".format(p[2]))
            env[p[1]] = run(p[2])
        # print(env)
        elif (p[0] == 'var'):
            if (p[1] not in env):
                print('Varchar: {}'.format(p[1]))
                exit(1)
            else:
                return env[p[1]]
    else:
        return p


while True:
    try:
        string = input('Digite sua expressão matemática: >>> ')
    except Exception as ar:
        print("Erro encontrado, nome do erro: {}".format(ar))
        break
    parser.parse(string)