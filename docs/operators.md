# Standard Sigils
These are the sigils I came up with for built-in operators.
## Operand Stack Manipulation Operators
|![pop sigil](../images/sigil_pop.png)|![exch sigil](../images/sigil_exch.png)|![dup sigil](../images/sigil_dup.png)|![copy sigil](../images/sigil_copy.png)|![index sigil](../images/sigil_index.png)|![roll sigil](../images/sigil_roll.png)|
|:--:|:--:|:--:|:--:|:--:|:--:|
|pop|exch|dup|copy|index|roll|

Unknown: ['clear', 'count', 'mark', 'cleartomark', 'counttomark']
## Arithmetic and Math Operators
|![add sigil](../images/sigil_add.png)|![div sigil](../images/sigil_div.png)|![idiv sigil](../images/sigil_idiv.png)|![mod sigil](../images/sigil_mod.png)|![mul sigil](../images/sigil_mul.png)|![sub sigil](../images/sigil_sub.png)|![abs sigil](../images/sigil_abs.png)|![neg sigil](../images/sigil_neg.png)|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|add|div|idiv|mod|mul|sub|abs|neg|
|![rand sigil](../images/sigil_rand.png)|![srand sigil](../images/sigil_srand.png)|![rrand sigil](../images/sigil_rrand.png)|
|rand|srand|rrand|

Unknown: ['ceiling', 'floor', 'round', 'truncate', 'sqrt', 'atan', 'cos', 'sin', 'exp', 'ln', 'log']
## Array Operators
|![array sigil](../images/sigil_array.png)|![length sigil](../images/sigil_length.png)|![copy sigil](../images/sigil_copy.png)|![forall sigil](../images/sigil_forall.png)|
|:--:|:--:|:--:|:--:|
|array|length|copy|forall|

Unknown: ['[', ']', 'get', 'put', 'getinterval', 'putinterval', 'astore', 'aload']
## Packed Array Operators
|![length sigil](../images/sigil_length.png)|![copy sigil](../images/sigil_copy.png)|![forall sigil](../images/sigil_forall.png)|
|:--:|:--:|:--:|
|length|copy|forall|

Unknown: ['packedarray', 'setpacking', 'currentpacking', 'get', 'getinterval', 'packedarray']
## Dictionary Operators
|![dict sigil](../images/sigil_dict.png)|![length sigil](../images/sigil_length.png)|![begin sigil](../images/sigil_begin.png)|![end sigil](../images/sigil_end.png)|![def sigil](../images/sigil_def.png)|![copy sigil](../images/sigil_copy.png)|![forall sigil](../images/sigil_forall.png)|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|dict|length|begin|end|def|copy|forall|

Unknown: ['<<', '>>', 'maxlength', 'load', 'store', 'get', 'put', 'undef', 'known', 'where', 'currentdict', 'errordict', '$error', 'systemdict', 'userdict', 'globaldict', 'statusdict', 'countdictstack', 'dictstack', 'cleardictstack']
## String Operators
|![length sigil](../images/sigil_length.png)|![copy sigil](../images/sigil_copy.png)|![forall sigil](../images/sigil_forall.png)|
|:--:|:--:|:--:|
|length|copy|forall|

Unknown: ['string', 'get', 'put', 'getinterval', 'putinterval', 'anchorsearch', 'search', 'token']
## Relational, Boolean, and Bitwise Operators
|![and sigil](../images/sigil_and.png)|![not sigil](../images/sigil_not.png)|![or sigil](../images/sigil_or.png)|![xor sigil](../images/sigil_xor.png)|
|:--:|:--:|:--:|:--:|
|and|not|or|xor|

Unknown: ['eq', 'ne', 'ge', 'gt', 'le', 'lt', 'true', 'false', 'bitshift']
## Control Operators
|![if sigil](../images/sigil_if.png)|![ifelse sigil](../images/sigil_ifelse.png)|![repeat sigil](../images/sigil_repeat.png)|
|:--:|:--:|:--:|
|if|ifelse|repeat|

Unknown: ['exec', 'for', 'loop', 'exit', 'stop', 'stopped', 'countexecstack', 'execstack', 'quit', 'start']

None: Type, Attribute, and Conversion Operators

None: File Operators

None: Resource Operators

None: Virtual Memory Operators

None: Miscellaneous Operators
## Graphics State Operators (Device-Independent)
|![gsave sigil](../images/sigil_gsave.png)|![grestore sigil](../images/sigil_grestore.png)|![setlinewidth sigil](../images/sigil_setlinewidth.png)|![currentlinewidth sigil](../images/sigil_currentlinewidth.png)|![setlinecap sigil](../images/sigil_setlinecap.png)|![currentlinecap sigil](../images/sigil_currentlinecap.png)|![setlinejoin sigil](../images/sigil_setlinejoin.png)|![currentlinejoin sigil](../images/sigil_currentlinejoin.png)|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|gsave|grestore|setlinewidth|currentlinewidth|setlinecap|currentlinecap|setlinejoin|currentlinejoin|
|![setcolor sigil](../images/sigil_setcolor.png)|![currentcolor sigil](../images/sigil_currentcolor.png)|![sethsbcolor sigil](../images/sigil_sethsbcolor.png)|![currenthsbcolor sigil](../images/sigil_currenthsbcolor.png)|![setrgbcolor sigil](../images/sigil_setrgbcolor.png)|![currentrgbcolor sigil](../images/sigil_currentrgbcolor.png)|![setcmykcolor sigil](../images/sigil_setcmykcolor.png)|![currentcmykcolor sigil](../images/sigil_currentcmykcolor.png)|
|setcolor|currentcolor|sethsbcolor|currenthsbcolor|setrgbcolor|currentrgbcolor|setcmykcolor|currentcmykcolor|

Unknown: ['clipsave', 'cliprestore', 'grestoreall', 'initgraphics', 'gstate', 'setgstate', 'currentgstate', 'setmiterlimit', 'currentmiterlimit', 'setstrokeadjust', 'currentstrokeadjust', 'setdash', 'currentdash', 'setcolorspace', 'currentcolorspace', 'setgray', 'currentgray']

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
