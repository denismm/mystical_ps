from ast import AST
from shutil import ExecError
import black
import warnings

## dictionary of operation names in post script : operation in python
op_dict = {
    "add": "+",
    "sub": "-",
    "mul": "*",
    "div": "/",
    "mod": "%",
    "pow": "^",
    "rand": "np.random.randint(100)",  # Up for debate whether we want to be able to specify a range of random numbers, I think it makes for prettier mystical to pre-specify it as 0-100, but obviously we lose flexibility that way
}

# Invocation types tell you what to do with the result of the spell
# i.e. print, save, etc.
invoke_dict = {
    "exec": "print",
    # "save": TODO this could save the the interpreted python code to a file
}


# Custom exception for spell failures
class Fizzle(Exception):
    """Raised when a spell or operation fails unexpectedly."""

    pass


# Generalized AST node class
class ASTNode:
    """
    Represents a generic node in an Abstract Syntax Tree (AST).

    Attributes:
        lineno (int): The line number in the source code where the node appears.
        colno (int): The column number in the source code where the node appears.
        lexpos (int): The lexical position (character offset) in the source code.

    Methods:
        to_python():
            Converts the AST node to its equivalent Python representation.
            Must be implemented by subclasses.

            Raises:
                NotImplementedError: If the method is not implemented by a subclass.
    """

    def __init__(
        self,
        lineno: int,
        colno: int,
        lexpos: int,
    ):
        self.lineno = lineno
        self.colno = colno
        self.lexpos = lexpos

    def to_python(self):
        raise NotImplementedError("to_python must be implemented by subclasses")


class Spell(ASTNode):
    def __init__(
        self,
        body: list[ASTNode],
        lineno,
        colno,
        lexpos,
    ):
        super().__init__(lineno, colno, lexpos)
        self.body = body
        """
        Represents a spell node in the abstract syntax tree (AST).
        (Typically, this is the root node in the AST)
        A Spell is a collection of statements
        AKA a program/contents of a .ps file

        Args:
            body (list[ASTNode]): The contents of in inscription, what does this function do?
            lineno (int): The line number in the source code where this node appears.
            colno (int): The column number in the source code where this node appears.
            lexpos (int): The lexical position in the source code.

        Raises:
            Fizzle: If more than one Invocation is found in the body.
        """
        # Walk the tree and store Inscription nodes in a dictionary by name so we can reference them when called
        self.inscriptions: dict[str, Inscription] = {}
        for node in self.body:
            if isinstance(node, Inscription):
                self.inscriptions[node.name] = node

    def __repr__(self, indent=0):
        """
        Recursively pretty-prints AST nodes, lists, and basic types with indentation.
        Ugly printing, I recommend using the pretty_print function in mystical_parser
        """
        # TODO: Replace with pretty print function in mystical_parser.py
        pad = " " * indent
        s = f"{pad}Spell(lineno={self.lineno}, colno={self.colno}, lexpos={self.lexpos},\n"
        if hasattr(self, "body"):
            if isinstance(self.body, list):
                for item in self.body:
                    # Use default repr, but indent lines for readability
                    item_repr = repr(item)
                    item_lines = item_repr.splitlines() or [item_repr]
                    for line in item_lines:
                        s += " " * (indent + 2) + line + "\n"
            else:
                s += " " * (indent + 2) + repr(self.body) + "\n"
        s += pad + ")"
        return s

    def to_python(self, filename: str | None = None):
        """_Convert spell to python by recursively going through each node_

        Args:
            filename (str | None, optional): _.py file to save the resulting python to a file_. Defaults to None.

        Returns:
            _type_: _python code in a long string_
        """
        python_code = "import numpy as np\n"
        for n in self.body:
            # Loop through each node in the spell's AST
            if isinstance(n, Cast):
                # If inscription is cast, search the inscription for it's invocation so that the python code knows what to do with the result
                print(f"cast: {n.name}")
                inscription = self.inscriptions.get(n.name)
                invocation = inscription.invocation  # type: ignore[attr-defined]
                if invocation:
                    python_code = python_code + f"{invocation}({n.name}())\n"
                else:
                    # If no invocation in the inscription, can't cast!
                    raise Fizzle(
                        "Inscription is missing an invocation-- do you need to add {exec} to the function "
                        + f"{n.name}"
                        + " in the .ps file?"
                    )
            else:
                # Otherwise, just convert the node to python
                python_code = python_code + n.to_python()
        formatted_code = black.format_str(python_code, mode=black.FileMode())

        # TODO: Make this an invocation instead
        if filename:
            if not filename.endswith(".py"):
                filename = filename + ".py"
                warnings.warn(
                    f"Improperly named filename, writing to {filename}", UserWarning
                )

            with open(filename, "w") as f:
                f.write(formatted_code)
        return formatted_code


class Inscription(ASTNode):
    def __init__(
        self,
        name: str,
        magic: bool,
        body: list[ASTNode],
        lineno: int,
        colno: int,
        lexpos: int,
    ):
        """
        Represents an inscription node in the abstract syntax tree (AST).
        An Inscription is a collection rings that are executable
        AKA a function


        Args:
            name (str): The inscription's name (function name)
            magic (bool): Is this inscription printed in mystical? (has mystical_unscaled call)
            body (list[ASTNode]): The contents of in inscription, what does this function do?
            lineno (int): The line number in the source code where this node appears.
            colno (int): The column number in the source code where this node appears.
            lexpos (int): The lexical position in the source code.

        Other Attributes:
            invokeType: On init, recursively look through the vodyfor an invocation node and assign that as the invokeType attribute


        Methods:
            __repr__(): Returns a string representation of the Inscription node.
            to_python(): Converts the inscription to its Python code representation as a function.

        Raises:
            Fizzle: If more than one Invocation is found in the body.
        """
        super().__init__(lineno, colno, lexpos)
        self.name = name
        self.body = body

        # Use the Invocation in the Inscription to determine what to do with the result if called
        def getInvokeType(self):
            def find_invocations(nodes):
                found = []
                for n in nodes:
                    if isinstance(n, Invocation):
                        found.append(n)
                    elif hasattr(n, "body") and isinstance(n.body, list):
                        found.extend(find_invocations(n.body))
                    elif hasattr(n, "sigils") and isinstance(n.sigils, list):
                        found.extend(find_invocations(n.sigils))
                return found

            invocations = find_invocations(self.body)
            count_invokes = len(invocations)
            # Each inscription can only have 1 invocation
            if count_invokes > 1:
                raise Fizzle(
                    f"Multiple invocations in this inscription: {invocations}, only one allowed"
                )
            elif count_invokes < 1:
                return None
            else:
                return invocations[0].invocation  # type: ignore[attr-defined]

        # Get the invocation type
        self.invocation = getInvokeType(self)

    def __repr__(self):
        return f"Inscription({self.name!r}, {self.body!r})"

    def to_python(self):
        """_Convert inscription to a python function_

        Returns:
            _str_: _python code as str_
        """

        # Functions start with def FUNCTION:
        python_code: str = f"def {self.name}():\n"

        # Loop through every node in inscription and convert to python
        for n in self.body:
            # Right now it just stores all that python in one long string after a return statement
            # TODO: Variable assignments?
            python_code = python_code + "\treturn " + n.to_python() + "\n"
        return python_code


class Cast(ASTNode):
    """
    Represents a Cast node in the abstract syntax tree (AST).
    You Cast a Spell when you Invoke an Inscription
    AKA you run the program when you call a function

    Attributes:
        name (str): The name of the inscription being cast
        lineno (int): The line number in the source code where the cast appears.
        colno (int): The column number in the source code where the cast appears.
        lexpos (int): The lexical position in the source code.

        Methods:
            __repr__(): Returns a string representation of the Cast node.
            to_python(): Converts the cast operation to its Python code representation as a function call.

    Methods:
        __repr__(): Returns a string representation of the Cast node.
        to_python(): Converts the cast operation to its Python code representation as a function call.
    """

    def __init__(
        self,
        name: str,
        # TODO: arguments?
        lineno,
        colno,
        lexpos,
    ):
        super().__init__(lineno, colno, lexpos)
        self.name = name

    def __repr__(self):
        return f"Cast({self.name!r})"

    def to_python(self):
        """_Convert an cast in python code by printing it as a function call_

        Returns:
            _str_: _python code as str_
        """
        return f"{self.name}()"


class Invocation(ASTNode):
    """
    Represents an invocation node in the abstract syntax tree (AST).
    The invocation is what you do with the result of the spell.
    i.e. print, save, etc.

    Args:
        invokeType (str): Matches correspond invocation statement to the invoke_dict
        lineno (int): The line number in the source code where the invocation occurs.
        colno (int): The column number in the source code where the invocation occurs.
        lexpos (int): The lexical position in the source code.

    Methods:
        __repr__(): Returns a string representation of the invocation node.
        to_python(): Invocations are properties of Inscriptions, so this just returns an empty string
    """

    def __init__(
        self,
        invokeType: str,
        lineno,
        colno,
        lexpos,
    ):
        super().__init__(lineno, colno, lexpos)
        self.invocation = invoke_dict[invokeType]

    def __repr__(self):
        return f"{self.invocation}Cast()"

    def to_python(self):
        """return an empty string, invocations are only used when an inscription is cast"""
        return ""


# Arrays are non-executable collection of sigils
# Non-Executable Rings
class Array(ASTNode):
    def __init__(
        self,
        sigils: list,
        lineno,
        colno,
        lexpos,
    ):
        """
        Represents a postscript array (i.e. [])  node in the abstract syntax tree (AST).

        Args:
            sigils (list): Items inside the array
            lineno (int): The line number in the source code where the invocation occurs.
            colno (int): The column number in the source code where the invocation occurs.
            lexpos (int): The lexical position in the source code.

        Methods:
            __repr__(): Returns a string representation of the invocation node.
            to_python(): Converts the array to a numpy array
        """

        super().__init__(lineno, colno, lexpos)
        self.sigils = sigils

    def __repr__(self):
        return f"Array({self.sigils!r})"

    def to_python(self):
        """
        Convert the array to python by putting it inside a numpy array

        Returns:
            str: python code as string i.e. 'np.array([1,2,etc.])'
        """
        pythonstr = "np.array(["
        for idx in range(0, len(self.sigils)):
            ele = self.sigils[idx]
            if isinstance(ele, ASTNode):
                pythonstr = pythonstr + ele.to_python()
            else:
                pythonstr = pythonstr + str(ele)
            if idx == len(self.sigils) - 1:
                pythonstr = pythonstr + "])"
            else:
                pythonstr = pythonstr + ", "
        return pythonstr


class BinOp(ASTNode):
    """
    Represents a binary operation node in the abstract syntax tree (AST).

    Attributes:
        left (float or ASTNode): The left operand of the binary operation.
        right (float or ASTNode): The right operand of the binary operation.
        op (str): The operator for the binary operation, mapped from op_dict.
        lineno (int): The line number in the source code where this node appears.
        colno (int): The column number in the source code where this node appears.
        lexpos (int): The lexical position in the source code.

    Methods:
        __repr__(): Returns a string representation of the BinOp node.
        execute(): Evaluates the binary operation and returns the result.
        to_python(): Converts the binary operation to a Python expression string.
    """

    def __init__(self, left, right, op, lineno, colno, lexpos):
        super().__init__(lineno, colno, lexpos)
        self.left: float = left
        self.right: float = right
        self.op: str = op_dict[op]

    def __repr__(self):
        return f"BinOp({self.left!r}, {self.right!r}, {self.op!r}, lineno={self.lineno}, colno={self.colno}, lexpos={self.lexpos})"

    def execute(self):
        """Gets the of the binary operation in python"""
        return eval(self.to_python())

    def to_python(self):
        """
        Convert the binary operation to executable python code
        If left or right operands are AST nodes, recursively go into those and convert them to python.
        This allows things like {1 {2 3 mul} add} = (1+(2*3))

        Returns:
            str: python code as string i.e. '1 + 2'
        """

        if isinstance(self.left, ASTNode):
            leftstr = self.left.to_python()
        else:
            leftstr = str(self.left)

        if isinstance(self.right, ASTNode):
            rightstr = self.right.to_python()
        else:
            rightstr = str(self.right)

        return leftstr + self.op + rightstr

    # TODO: These op nodes could be children of a parent op class to save on the execute() method, maybe overkill tho


class NullOp(ASTNode):
    """
    Represents a nullary operation node in the abstract syntax tree (AST).
    These are operations that do not require any operands, like `rand`

    Attributes:
        op (str): The operator for the nullary operation, mapped from op_dict.
        lineno (int): The line number in the source code where this node appears.
        colno (int): The column number in the source code where this node appears.
        lexpos (int): The lexical position in the source code.

    Methods:
        __repr__(): Returns a string representation of the NullOp node.
        to_python(): Converts the nullary operation to its Python code representation.
    """

    def __init__(self, op, lineno, colno, lexpos):
        super().__init__(lineno, colno, lexpos)
        self.op = op_dict[op]

    def __repr__(self):
        return f"NullOp({self.op!r})"

    def to_python(self):
        """
        Convert the nullary operation to executable python code.

        Returns:
            str: Python code as a string, e.g., 'np.random.randint(100)'
        """
        return f"{self.op}"


# Executable Rings
class XArray(ASTNode):
    """
    Represents an executable array node in the AST.

    Attributes:
        sigils (list): The sigils of the array, which may be ASTNode instances or literals.
        lineno (int): The line number in the source code where this node appears.
        colno (int): The column number in the source code where this node appears.
        lexpos (int): The lexical position in the source code.

    Methods:
        __repr__(): Returns a string representation of the XArray node.
        to_python(): Converts the XArray node and its sigils into a Python (NumPy) array string.
    """

    def __init__(
        self,
        sigils: list,
        lineno,
        colno,
        lexpos,
    ):
        super().__init__(lineno, colno, lexpos)
        self.sigils = sigils

    def __repr__(self):
        return f"XArray({self.sigils!r})"

    def to_python(self):
        """
        Convert the array to python by putting it inside a numpy array

        Note: IF there is only one sigil in the array, it returns it outside of the numpy array.
        i.e. { 1 2 add } has one binary operation, so instead of returning  np.array([1 + 2]), it returns just '1 + 2'


        Returns:
            str: python code as string i.e. 'np.array([1,2,etc.])'
        """
        pythonstr = "np.array(["
        element_count = 0
        for idx, ele in enumerate(self.sigils):
            if isinstance(ele, ASTNode):
                if isinstance(ele, Invocation):
                    if pythonstr[-2] == ",":
                        pythonstr = pythonstr[:-2]
                else:
                    val = ele.to_python()
                    if val is None:
                        raise ValueError(
                            f"to_python() returned None for element {ele} of type {type(ele)}"
                        )
                    pythonstr += val
                    element_count += 1
            else:
                pythonstr += str(ele)
                element_count += 1
            if idx == len(self.sigils) - 1:
                pythonstr += "])"
            else:
                pythonstr += ", "

        # Count sigils in the resulting numpy array string (rough estimate)
        # This will count the number of top-level commas + 1
        array_content = pythonstr[
            len("np.array([") : -2
        ]  # strip prefix and "])", crude
        num_sigils = array_content.count(",") + 1 if array_content.strip() else 0

        if num_sigils == 1:
            pythonstr = pythonstr.replace("np.array([", "").replace("])", "")

        print(f"XArray to_python: {num_sigils} sigils in resulting np.array")
        return pythonstr
