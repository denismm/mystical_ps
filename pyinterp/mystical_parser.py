from ast import AST
from math import e
import ply.yacc as yacc
from pyinterp.mystical_lexer import tokens
import pyinterp.mystical_ASTTypes as ASTTypes

# Rules that the parser will use to convert the list of lexed tokens into an Abstract Syntax Tree (AST)


def find_column(input_text, lexpos):
    last_cr = input_text.rfind("\n", 0, lexpos)
    if last_cr < 0:
        last_cr = -1
    return lexpos - last_cr


# the whole PS file is a spell and it's made up of a series of statements
def p_spell(p):
    """spell : statements"""
    p[0] = ASTTypes.Spell(
        body=p[1],
        lineno=p.lineno(1),
        colno=find_column(p.lexer.lexdata, p.lexpos(1)),
        lexpos=p.lexpos(1),
    )


# allows you to peal off a statement from a list of statements
def p_statements_multiple(p):
    """statements : statements statement"""
    if p[2] is not None:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = p[1]


# allows you to have a single statement in the list of statements
def p_statements_single(p):
    """statements : statement"""
    print(f"p_statements_single: {p[1]}")
    if p[1] is not None:
        p[0] = [p[1]]
    else:
        p[0] = []


# An Invocation describes HOW a Spell Is Cast (i.e. print result? save to files?)
# It goes in an executable array, I'm thinking at the end of an inscription? Though that's not enforced right now
# So the last sigil in an inscription would be {exec} to print the result.
def p_invoke(p):
    """invoke : LXARRAY INVOCATION RXARRAY"""
    p[0] = ASTTypes.Invocation(
        invokeType=p[2],
        lineno=p.lineno(1),
        colno=find_column(p.lexer.lexdata, p.lexpos(1)),
        lexpos=p.lexpos(1),
    )


# an array is a list of statements
def p_array(p):
    """array : LARRAY statements RARRAY"""
    p[0] = ASTTypes.Array(
        p[2],
        lineno=p.lineno(1),
        colno=find_column(p.lexer.lexdata, p.lexpos(1)),
        lexpos=p.lexpos(1),
    )


# nullary operators are operators that don't take any arguments, like `rand`
def p_nullop(p):
    """nullop : NULLOP"""
    p[0] = ASTTypes.NullOp(
        op=p[1],
        lineno=p.lineno(1),
        colno=find_column(p.lexer.lexdata, p.lexpos(1)),
        lexpos=p.lexpos(1),
    )


# an executable array is a list of statements that can be executed
def p_xarray(p):
    """xarray : LXARRAY statements RXARRAY"""
    p[0] = ASTTypes.XArray(
        sigils=p[2],
        lineno=p.lineno(1),
        colno=find_column(p.lexer.lexdata, p.lexpos(1)),
        lexpos=p.lexpos(1),
    )


# idk just a placeholder for now, ideally this should be anything that can be fed to an operator?
# but when I used this in p_binop it broke and I couldn't figure out why
def p_expression(p):
    """expression : NUMBER
    | xarray"""
    p[0] = p[1]


# binary operation, like 1 + 1
# in ps it's a stack format so that would be 1 1 +
# right now binary operations just take numbers or xarrays
# so you could do 1 {1 2 *} + =  3
def p_binop(p):
    """binop : NUMBER NUMBER BINOP
    | NUMBER xarray BINOP
    | xarray NUMBER BINOP
    | xarray xarray BINOP"""
    p[0] = ASTTypes.BinOp(
        left=p[1],
        right=p[2],
        op=p[3],
        lineno=p.lineno(1),
        colno=find_column(p.lexer.lexdata, p.lexpos(1)),
        lexpos=p.lexpos(1),
    )


# An inscription is a list of statements that can be executed (so a function)
# It's *magic* because it has the INSCRIBE keyword (mystical_unscaled) that tells postscript to draw this in mystical
def p_magic_inscription(p):
    """inscription : SLASH IDENTIFIER LXARRAY statements INSCRIBE RXARRAY DEF"""
    print("p_inscription", p[2])
    p[0] = ASTTypes.Inscription(
        name=p[2],
        magic=True,
        body=p[4],
        lineno=p.lineno(1),
        colno=find_column(p.lexer.lexdata, p.lexpos(1)),
        lexpos=p.lexpos(1),
    )


# A regular non-magic inscription that doesn't get drawn in mystical
def p_inscription(p):
    """inscription : SLASH IDENTIFIER LXARRAY statements RXARRAY DEF"""
    p[0] = ASTTypes.Inscription(
        name=p[2],
        magic=False,
        body=p[4],
        lineno=p.lineno(1),
        colno=find_column(p.lexer.lexdata, p.lexpos(1)),
        lexpos=p.lexpos(1),
    )


# a cast is when you call a function. So if you define "/add_two_nums{...}def" and then
# call it with "add_two_nums", that call, which is just a string, is a cast
# I don't know how to feed arguments to a function in postscript yet so it doesn't take arguments at this time :')
def p_cast(p):
    """cast : IDENTIFIER"""
    p[0] = ASTTypes.Cast(
        name=p[1],
        # TODO: Arguments?
        lineno=p.lineno(1),
        colno=find_column(p.lexer.lexdata, p.lexpos(1)),
        lexpos=p.lexpos(1),
    )


# import statements at the top of the file, we ignore those
def p_import(p):
    """import : LPAREN IDENTIFIER PERIOD PS RPAREN RUN"""
    print("import", p[2])
    # p[0] = ("import", p[2])


# these are keywords used to print the postscript code, so we just ignore them
def p_scale(p):
    """scale : NUMBER SOFTSCALE"""


def p_translate(p):
    """translate : NUMBER NUMBER TRANSLATE"""


def p_show(p):
    """show : SHOW"""


ignored_tokens = ["NEWLINE", "import", "show", "scale", "translate"]


def p_statement(p):
    """statement : NEWLINE
    | nullop
    | binop
    | expression
    | cast
    | inscription
    | invoke
    | show
    | scale
    | translate
    | array
    | import"""
    if p.slice[1].type in ignored_tokens:
        p[0] = None
    else:
        p[0] = p[1]


# error handling
def p_error(p):
    if p:
        print(
            f"Syntax error at token {p.type} (value: {p.value}) at line {getattr(p, 'lineno', '?')}"
        )
    else:
        print("Syntax error at EOF")


# the importable parser we can use in other files
parser = yacc.yacc()


def pretty_print_ast(tree, indent=0):
    """
    Recursively pretty-prints AST nodes, lists, and basic types with indentation.
    """
    pad = " " * indent
    if isinstance(tree, ASTTypes.ASTNode):
        invokeType = ""

        # Print node type
        print(pad + str(type(tree).__name__) + " -> ", end="")
        # Print node Name
        name = "name=" + tree.name + "," if hasattr(tree, "name") else ""  # type: ignore[attr-defined]
        name += (
            "invokeType=" + str(tree) + ","
            if isinstance(tree, ASTTypes.Invocation)
            else ""
        )
        print(name)

        # Print node loc
        print(
            f"{" "*(indent)} lineno={tree.lineno}, colno={tree.colno}, lexpos={tree.lexpos},"
        )
        (
            None
            if isinstance(tree, ASTTypes.BinOp) or isinstance(tree, ASTTypes.NullOp)
            else print("")
        )
        if hasattr(tree, "body"):
            pretty_print_ast(tree.body, indent + 4)  # type: ignore[attr-defined]
        elif hasattr(tree, "sigils"):
            pad = " " * (indent)
            for item in tree.sigils:  # type: ignore[attr-defined]
                pretty_print_ast(item, indent + 4)
        elif isinstance(tree, ASTTypes.BinOp):
            left = f"{" "*(indent+2)}left="
            op = f"{" "*(indent+2)}op={tree.op},"
            right = f"{" "*(indent+2)}right="
            if isinstance(tree.left, ASTTypes.ASTNode):
                print(left)
                pretty_print_ast(tree.left, indent + 4)
            else:
                print(right + str(tree.right))
            print(op)
            if isinstance(tree.right, ASTTypes.ASTNode):
                print(right)
                pretty_print_ast(tree.right, indent + 4)
            else:
                print(left + str(tree.left))
            print("")
        elif isinstance(tree, ASTTypes.NullOp):
            print(" " * (indent + 2), tree.op)
            print("")
        elif isinstance(tree, ASTTypes.Invocation):
            pass
        elif isinstance(tree, ASTTypes.Cast):
            pass
        else:
            print(pad + str(tree))
    elif isinstance(tree, list):
        pad = " " * (indent)
        for item in tree:
            pretty_print_ast(item, indent)
