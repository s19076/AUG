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
)

# Tokens

t_SENTENCE = r'[a-zA-Z0-9]+(\s+[a-zA-Z0-9]*)*'

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

def p_statement_expr(t):
    '''statement : expression'''
    print(t[1])

def p_expression_sentence(t):
    '''expression : SENTENCE'''
    t[0] = t[1]

def p_error(t):
    print("Syntax error at '%s'" % t.value)

parser = yacc.yacc()

while True:
    # try:
    #     s = input('calc > ')
    # except EOFError:
    #     break
    parser.parse("ala")
    # parser.parse("ala + am^-1 + kota+bota", debug = True)
    # parser.parse("asdasd kamil nenta asdasd")
    # parser.parse("ala ma kota[0]", debug=True)

    break