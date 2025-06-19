import ply.lex as lex


# python lexer
# takes in a ps file contents as a string and lexes it into a series of tokens for a parser
# tokens are defined by t_ functions (convention of the ply.lex library)


def t_NUMBER(t):
    r"-?\d+(\.\d+)?"
    t.value = float(t.value) if "." in t.value else int(t.value)
    return t


def t_NEWLINE(t):
    r"\n+"
    t.lexer.lineno += len(t.value)
    # t.lexer.skip(1)


def t_INSCRIBE(t):
    r"mystical_unscaled"
    return t


def t_SHOW(t):
    r"showpage"
    return t


def t_TRANSLATE(t):
    r"translate"
    return t


def t_NULLOP(t):
    r"\b(rand|rrand)\b"
    return t


def t_SOFTSCALE(t):
    r"softscale"
    return t


def t_BINOP(t):
    r"\b(add|mul|sub|div|eq|lt|gt|and|or|not|xor)\b"
    return t


def t_RUN(t):
    r"\b(run)\b"
    return t


def t_INVOCATION(t):
    r"\b(exec|run)\b"
    return t


def t_PS(t):
    r"[pP][sS]"
    return t


def t_DEF(t):
    r"\bdef\b"
    return t


def t_LPAREN(t):
    r"\("
    return t


def t_RPAREN(t):
    r"\)"
    return t


def t_LARRAY(t):
    r"\["
    return t


def t_RARRAY(t):
    r"\]"
    return t


def t_LXARRAY(t):
    r"\{"
    return t


def t_RXARRAY(t):
    r"\}"
    return t


def t_PERIOD(t):
    r"\."
    return t


def t_SLASH(t):
    r"/"
    return t


def t_IDENTIFIER(t):
    r"[a-zA-Z_][a-zA-Z0-9_]*"
    return t


# List of token names
# This is required by ply.lex
tokens = (
    "BINOP",
    "NULLOP",
    "PS",
    "DEF",
    "INSCRIBE",
    "SHOW",
    "TRANSLATE",
    "SOFTSCALE",
    "RUN",
    "INVOCATION",
    "LPAREN",
    "RPAREN",
    "LARRAY",
    "RARRAY",
    "LXARRAY",
    "RXARRAY",
    "PERIOD",
    "NEWLINE",
    "SLASH",
    "IDENTIFIER",
    "NUMBER",
)

# Ignore Characters
t_ignore = " \t\r"
t_ignore_COMMENT = r"%.*"


# Error handling rule, note an illegal character and keep lexing
def t_error(t):
    print(
        f"Illegal character '{t.value[0]}' (ord: {ord(t.value[0])}) at line {t.lineno}"
    )
    t.lexer.skip(1)


# the lexer object we can import and use in other files
lexer = lex.lex()
