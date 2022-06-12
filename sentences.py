# -----------------------------------------------------------------------------
# sentences.py
#
# A simple calculator with sentences -- all in one file.
# -----------------------------------------------------------------------------
import ply.yacc as yacc
import ply.lex as lex
import utils as ut

tokens = (
    "SENTENCE",
    "CONCAT",
    "REVERSE",
    "LENGTH",
    "FIRST",
    "LAST"
)

# Tokens

t_SENTENCE = r'[a-zA-Z0-9]+(\s+[a-zA-Z0-9]*)*'
t_CONCAT = r'\+'
t_REVERSE = r'\^-1'
t_LENGTH = r'\#'
t_FIRST = r'\[0\]'
t_LAST = r'\[-1\]'

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Parsing rules
precedence = (
    ('left', 'LENGTH'),
    ('left', 'CONCAT'),
    ('left', 'FIRST', 'LAST'),
    ('left', 'REVERSE'),
)

def p_statement_expr(t):
    '''statement : expression
                 | length'''
    print(t[1])

def p_expression_sentence(t):
    '''expression : SENTENCE'''
    t[0] = t[1]

def p_expression_expression_concat_expression(t):
    '''expression : expression CONCAT expression'''
    t[0] = t[1] + t[3]

def p_expression_reverse(t):
    '''expression : expression REVERSE'''
    t[0] = ut.reverse_sentence(t[1])

def p_length_expression(t):
    '''length : expression LENGTH'''
    t[0] = len(t[1])

def p_expression_expression_first_LAST(t):
    '''expression : expression FIRST
                  | expression LAST'''
    if t[2] == "[0]":
        t[0] = t[1].split()[0]
    elif t[2] == "[-1]":
        t[0] = t[1].split()[-1]

def p_error(t):

    print("Syntax error at '%s'" % t.value)

parser = yacc.yacc()

while True:
    # try:
    #     s = input('calc > ')
    # except EOFError:
    #     break
    parser.parse("ala ma kota asdasd")
    parser.parse("ala+ma+kota+kot ma ale+asdasd")
    parser.parse("testa am^-1 + kota+bota")
    parser.parse("kamil^-1+kamil^-1 + kot#")
    parser.parse("alan^-1+ ma kota[-1]#")

    break