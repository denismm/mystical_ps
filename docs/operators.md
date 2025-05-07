# Standard Sigils
These are the sigils I came up with for built-in operators.
## Operand Stack Manipulation Operators
|![pop sigil](../images/sigil_pop.png)|![dup sigil](../images/sigil_dup.png)|
|:--:|:--:|
|pop|dup|

Unknown: ['exch', 'copy', 'index', 'roll', 'clear', 'count', 'mark', 'cleartomark', 'counttomark']
## Arithmetic and Math Operators
|![mul sigil](../images/sigil_mul.png)|
|:--:|
|mul|

Unknown: ['add', 'div', 'idiv', 'mod', 'sub', 'abs', 'neg', 'ceiling', 'floor', 'round', 'truncate', 'sqrt', 'atan', 'cos', 'sin', 'exp', 'ln', 'log', 'rand', 'srand', 'rrand']
## Array Operators
|![array sigil](../images/sigil_array.png)|![forall sigil](../images/sigil_forall.png)|
|:--:|:--:|
|array|forall|

Unknown: ['[', ']', 'length', 'get', 'put', 'getinterval', 'putinterval', 'astore', 'aload', 'copy']
## Packed Array Operators
|![forall sigil](../images/sigil_forall.png)|
|:--:|
|forall|

Unknown: ['packedarray', 'setpacking', 'currentpacking', 'length', 'get', 'getinterval', 'packedarray', 'copy']
## Dictionary Operators
|![dict sigil](../images/sigil_dict.png)|![begin sigil](../images/sigil_begin.png)|![end sigil](../images/sigil_end.png)|![def sigil](../images/sigil_def.png)|![forall sigil](../images/sigil_forall.png)|
|:--:|:--:|:--:|:--:|:--:|
|dict|begin|end|def|forall|

Unknown: ['<<', '>>', 'length', 'maxlength', 'load', 'store', 'get', 'put', 'undef', 'known', 'where', 'copy', 'currentdict', 'errordict', '$error', 'systemdict', 'userdict', 'globaldict', 'statusdict', 'countdictstack', 'dictstack', 'cleardictstack']
## String Operators
|![forall sigil](../images/sigil_forall.png)|
|:--:|
|forall|

Unknown: ['string', 'length', 'get', 'put', 'getinterval', 'putinterval', 'copy', 'anchorsearch', 'search', 'token']
## Relational, Boolean, and Bitwise Operators
|![and sigil](../images/sigil_and.png)|![or sigil](../images/sigil_or.png)|![xor sigil](../images/sigil_xor.png)|
|:--:|:--:|:--:|
|and|or|xor|

Unknown: ['eq', 'ne', 'ge', 'gt', 'le', 'lt', 'not', 'true', 'false', 'bitshift']
## Control Operators
|![repeat sigil](../images/sigil_repeat.png)|
|:--:|
|repeat|

Unknown: ['exec', 'if', 'ifelse', 'for', 'loop', 'exit', 'stop', 'stopped', 'countexecstack', 'execstack', 'quit', 'start']

None: Type, Attribute, and Conversion Operators

None: File Operators

None: Resource Operators

None: Virtual Memory Operators

None: Miscellaneous Operators
## Graphics State Operators (Device-Independent)
|![gsave sigil](../images/sigil_gsave.png)|![grestore sigil](../images/sigil_grestore.png)|![setlinewidth sigil](../images/sigil_setlinewidth.png)|![currentlinewidth sigil](../images/sigil_currentlinewidth.png)|![setlinecap sigil](../images/sigil_setlinecap.png)|![currentlinecap sigil](../images/sigil_currentlinecap.png)|![setlinejoin sigil](../images/sigil_setlinejoin.png)|![currentlinejoin sigil](../images/sigil_currentlinejoin.png)|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|gsave|grestore|setlinewidth|currentlinewidth|setlinecap|currentlinecap|setlinejoin|currentlinejoin|

Unknown: ['clipsave', 'cliprestore', 'grestoreall', 'initgraphics', 'gstate', 'setgstate', 'currentgstate', 'setmiterlimit', 'currentmiterlimit', 'setstrokeadjust', 'currentstrokeadjust', 'setdash', 'currentdash', 'setcolorspace', 'currentcolorspace', 'setcolor', 'currentcolor', 'setgray', 'currentgray']

None: Graphics State Operators (Device-Dependent)
## Coordinate System and Matrix Operators
|![currentmatrix sigil](../images/sigil_currentmatrix.png)|![setmatrix sigil](../images/sigil_setmatrix.png)|![translate sigil](../images/sigil_translate.png)|![scale sigil](../images/sigil_scale.png)|![rotate sigil](../images/sigil_rotate.png)|
|:--:|:--:|:--:|:--:|:--:|
|currentmatrix|setmatrix|translate|scale|rotate|

Unknown: ['matrix', 'initmatrix', 'identmatrix', 'defaultmatrix', 'concat', 'concatmatrix', 'transform', 'dtransform', 'itransform', 'idtransform', 'invertmatrix']
## Path Construction Operators
|![currentpoint sigil](../images/sigil_currentpoint.png)|![moveto sigil](../images/sigil_moveto.png)|![lineto sigil](../images/sigil_lineto.png)|![arc sigil](../images/sigil_arc.png)|![arcn sigil](../images/sigil_arcn.png)|![closepath sigil](../images/sigil_closepath.png)|
|:--:|:--:|:--:|:--:|:--:|:--:|
|currentpoint|moveto|lineto|arc|arcn|closepath|

Unknown: ['newpath', 'rmoveto', 'rlineto', 'arct', 'arcto', 'curveto', 'rcurveto', 'flattenpath', 'reversepath', 'strokepath', 'ustrokepath', 'ustrokepath', 'charpath', 'uappend', 'clippath', 'setbbox', 'pathbbox', 'pathforall', 'upath', 'initclip', 'clip', 'eoclip', 'rectclip', 'ucache']
## Painting Operators
|![stroke sigil](../images/sigil_stroke.png)|![fill sigil](../images/sigil_fill.png)|
|:--:|:--:|
|stroke|fill|

Unknown: ['erasepage', 'eofill', 'rectstroke', 'rectfill', 'ustroke', 'ufill', 'ueofill', 'shfill', 'image', 'colorimage', 'imagemask']

None: Insideness-Testing Operators

None: Form and Pattern Operators

None: Device Setup and Output Operators

None: Glyph and Font Operators

None: Interpreter Parameter Operators
