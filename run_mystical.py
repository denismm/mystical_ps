from pyinterp.mystical_parser import parser, pretty_print_ast
from pyinterp.mystical_lexer import lexer
import sys

# Take in a mystical .ps file and convert it to python code


# Walk the AST and apply a function to each node, currently not used, but potentially quite useful, so keeping it!
def walk_ast(node, visit_fn):
    """
    Recursively walk the AST, calling visit_fn(node) on each node.
    """
    visit_fn(node)
    # Recursively walk children based on node type
    if hasattr(node, "__dict__"):
        for value in node.__dict__.values():
            if isinstance(value, list):
                for item in value:
                    if hasattr(item, "__dict__"):
                        walk_ast(item, visit_fn)
            elif hasattr(value, "__dict__"):
                walk_ast(value, visit_fn)


def print_node(node):
    print(type(node).__name__, node)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python mystical_ast_to_python.py <inputfile>")
        exit(1)
    with open(sys.argv[1]) as f:
        code = f.read()

    # Lex the ps file into tokens
    lexer.input(code)

    # parse the tokens into an AST
    tree = parser.parse(lexer=lexer)

    # Print the ast tree for easier troubleshooting
    print("AST:")
    pretty_print_ast(tree)

    # Convert the AST to python code
    python_code = tree.to_python()
    print("GENERATED CODE:")
    print(python_code)

    # Execute the generated python code
    print("EXECUTING CODE:")
    exec(python_code)
