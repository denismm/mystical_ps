# Standard Sigils
These are the sigils I came up with for built-in operators.
## Operand Stack Manipulation Operators
|![pop sigil](../images/sigil_pop.png)|![exch sigil](../images/sigil_exch.png)|![dup sigil](../images/sigil_dup.png)|![copy sigil](../images/sigil_copy.png)|![index sigil](../images/sigil_index.png)|![roll sigil](../images/sigil_roll.png)|
|:--:|:--:|:--:|:--:|:--:|:--:|
|pop|exch|dup|copy|index|roll|

No sigils for: clear, count, mark, cleartomark, counttomark
## Arithmetic and Math Operators
|![add sigil](../images/sigil_add.png)|![div sigil](../images/sigil_div.png)|![idiv sigil](../images/sigil_idiv.png)|![mod sigil](../images/sigil_mod.png)|![mul sigil](../images/sigil_mul.png)|![sub sigil](../images/sigil_sub.png)|![abs sigil](../images/sigil_abs.png)|![neg sigil](../images/sigil_neg.png)|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|add|div|idiv|mod|mul|sub|abs|neg|
|![sqrt sigil](../images/sigil_sqrt.png)|![atan sigil](../images/sigil_atan.png)|![cos sigil](../images/sigil_cos.png)|![sin sigil](../images/sigil_sin.png)|![rand sigil](../images/sigil_rand.png)|![srand sigil](../images/sigil_srand.png)|![rrand sigil](../images/sigil_rrand.png)|
|sqrt|atan|cos|sin|rand|srand|rrand|

No sigils for: ceiling, floor, round, truncate, exp, ln, log
## Array Operators
|![array sigil](../images/sigil_array.png)|![length sigil](../images/sigil_length.png)|![get sigil](../images/sigil_get.png)|![put sigil](../images/sigil_put.png)|![getinterval sigil](../images/sigil_getinterval.png)|![putinterval sigil](../images/sigil_putinterval.png)|![copy sigil](../images/sigil_copy.png)|![forall sigil](../images/sigil_forall.png)|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|array|length|get|put|getinterval|putinterval|copy|forall|

No sigils for: astore, aload
## Packed Array Operators
|![length sigil](../images/sigil_length.png)|![get sigil](../images/sigil_get.png)|![getinterval sigil](../images/sigil_getinterval.png)|![copy sigil](../images/sigil_copy.png)|![forall sigil](../images/sigil_forall.png)|
|:--:|:--:|:--:|:--:|:--:|
|length|get|getinterval|copy|forall|

No sigils for: packedarray, setpacking, currentpacking, packedarray
## Dictionary Operators
|![dict sigil](../images/sigil_dict.png)|![length sigil](../images/sigil_length.png)|![begin sigil](../images/sigil_begin.png)|![end sigil](../images/sigil_end.png)|![def sigil](../images/sigil_def.png)|![get sigil](../images/sigil_get.png)|![put sigil](../images/sigil_put.png)|![copy sigil](../images/sigil_copy.png)|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|dict|length|begin|end|def|get|put|copy|
|![forall sigil](../images/sigil_forall.png)|
|forall|

No sigils for: maxlength, load, store, undef, known, where, currentdict, errordict, $error, systemdict, userdict, globaldict, statusdict, countdictstack, dictstack, cleardictstack
## String Operators
|![string sigil](../images/sigil_string.png)|![length sigil](../images/sigil_length.png)|![get sigil](../images/sigil_get.png)|![put sigil](../images/sigil_put.png)|![getinterval sigil](../images/sigil_getinterval.png)|![putinterval sigil](../images/sigil_putinterval.png)|![copy sigil](../images/sigil_copy.png)|![forall sigil](../images/sigil_forall.png)|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|string|length|get|put|getinterval|putinterval|copy|forall|

No sigils for: anchorsearch, search, token
## Relational, Boolean, and Bitwise Operators
|![eq sigil](../images/sigil_eq.png)|![ne sigil](../images/sigil_ne.png)|![ge sigil](../images/sigil_ge.png)|![gt sigil](../images/sigil_gt.png)|![le sigil](../images/sigil_le.png)|![lt sigil](../images/sigil_lt.png)|![and sigil](../images/sigil_and.png)|![not sigil](../images/sigil_not.png)|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|eq|ne|ge|gt|le|lt|and|not|
|![or sigil](../images/sigil_or.png)|![xor sigil](../images/sigil_xor.png)|![true sigil](../images/sigil_true.png)|![false sigil](../images/sigil_false.png)|
|or|xor|true|false|

No sigils for: bitshift
## Control Operators
|![if sigil](../images/sigil_if.png)|![ifelse sigil](../images/sigil_ifelse.png)|![for sigil](../images/sigil_for.png)|![repeat sigil](../images/sigil_repeat.png)|
|:--:|:--:|:--:|:--:|
|if|ifelse|for|repeat|

No sigils for: exec, loop, exit, stop, stopped, countexecstack, execstack, quit, start
## Type, Attribute, and Conversion Operators
|![type sigil](../images/sigil_type.png)|![cvlit sigil](../images/sigil_cvlit.png)|![cvx sigil](../images/sigil_cvx.png)|![xcheck sigil](../images/sigil_xcheck.png)|![cvi sigil](../images/sigil_cvi.png)|![cvn sigil](../images/sigil_cvn.png)|![cvr sigil](../images/sigil_cvr.png)|![cvrs sigil](../images/sigil_cvrs.png)|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|type|cvlit|cvx|xcheck|cvi|cvn|cvr|cvrs|
|![cvs sigil](../images/sigil_cvs.png)|
|cvs|

No sigils for: executeonly, noaccess, readonly, rcheck, wcheck

No sigils for File Operators: file, filter, closefile, read, write, readhexstring, writehexstring, readstring, writestring, readline, token, bytesavailable, flush, flushfile, resetfile, status, run, currentfile, deletefile, renamefile, filenameforall, setfileposition, fileposition, print, =, ==, stack, pstack, printobject, writeobject, setobjectformat, currentobjectformat

No sigils for Resource Operators: defineresource, undefineresource, findresource, findcolorrendering, resourcestatus, resourceforall

No sigils for Virtual Memory Operators: save, restore, setglobal, currentglobal, gcheck, startjob, defineuserobject, execuserobject, undefineuserobject, UserObjects

No sigils for Miscellaneous Operators: bind, null, version, realtime, usertime, languagelevel, product, revision, serialnumber, executive, echo, prompt
## Graphics State Operators (Device-Independent)
|![gsave sigil](../images/sigil_gsave.png)|![grestore sigil](../images/sigil_grestore.png)|![setlinewidth sigil](../images/sigil_setlinewidth.png)|![currentlinewidth sigil](../images/sigil_currentlinewidth.png)|![setlinecap sigil](../images/sigil_setlinecap.png)|![currentlinecap sigil](../images/sigil_currentlinecap.png)|![setlinejoin sigil](../images/sigil_setlinejoin.png)|![currentlinejoin sigil](../images/sigil_currentlinejoin.png)|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|gsave|grestore|setlinewidth|currentlinewidth|setlinecap|currentlinecap|setlinejoin|currentlinejoin|
|![setmiterlimit sigil](../images/sigil_setmiterlimit.png)|![currentmiterlimit sigil](../images/sigil_currentmiterlimit.png)|![setcolor sigil](../images/sigil_setcolor.png)|![currentcolor sigil](../images/sigil_currentcolor.png)|![setgray sigil](../images/sigil_setgray.png)|![currentgray sigil](../images/sigil_currentgray.png)|![sethsbcolor sigil](../images/sigil_sethsbcolor.png)|![currenthsbcolor sigil](../images/sigil_currenthsbcolor.png)|
|setmiterlimit|currentmiterlimit|setcolor|currentcolor|setgray|currentgray|sethsbcolor|currenthsbcolor|
|![setrgbcolor sigil](../images/sigil_setrgbcolor.png)|![currentrgbcolor sigil](../images/sigil_currentrgbcolor.png)|![setcmykcolor sigil](../images/sigil_setcmykcolor.png)|![currentcmykcolor sigil](../images/sigil_currentcmykcolor.png)|
|setrgbcolor|currentrgbcolor|setcmykcolor|currentcmykcolor|

No sigils for: clipsave, cliprestore, grestoreall, initgraphics, gstate, setgstate, currentgstate, setstrokeadjust, currentstrokeadjust, setdash, currentdash, setcolorspace, currentcolorspace

No sigils for Graphics State Operators (Device-Dependent): sethalftone, currenthalftone, setscreen, currentscreen, setcolorscreen, currentcolorscreen, settransfer, currenttransfer, setcolortransfer, currentcolortransfer, setblackgeneration, currentblackgeneration, setundercolorremoval, currentundercolorremoval, setcolorrendering, currentcolorrendering, setflat, currentflat, setoverprint, currentoverprint, setsmoothness, currentsmoothness
## Coordinate System and Matrix Operators
|![currentmatrix sigil](../images/sigil_currentmatrix.png)|![setmatrix sigil](../images/sigil_setmatrix.png)|![translate sigil](../images/sigil_translate.png)|![scale sigil](../images/sigil_scale.png)|![rotate sigil](../images/sigil_rotate.png)|
|:--:|:--:|:--:|:--:|:--:|
|currentmatrix|setmatrix|translate|scale|rotate|

No sigils for: matrix, initmatrix, identmatrix, defaultmatrix, concat, concatmatrix, transform, dtransform, itransform, idtransform, invertmatrix
## Path Construction Operators
|![currentpoint sigil](../images/sigil_currentpoint.png)|![moveto sigil](../images/sigil_moveto.png)|![lineto sigil](../images/sigil_lineto.png)|![arc sigil](../images/sigil_arc.png)|![arcn sigil](../images/sigil_arcn.png)|![curveto sigil](../images/sigil_curveto.png)|![closepath sigil](../images/sigil_closepath.png)|![clip sigil](../images/sigil_clip.png)|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|currentpoint|moveto|lineto|arc|arcn|curveto|closepath|clip|

No sigils for: newpath, rmoveto, rlineto, arct, arcto, rcurveto, flattenpath, reversepath, strokepath, ustrokepath, ustrokepath, charpath, uappend, clippath, setbbox, pathbbox, pathforall, upath, initclip, eoclip, rectclip, ucache
## Painting Operators
|![stroke sigil](../images/sigil_stroke.png)|![fill sigil](../images/sigil_fill.png)|
|:--:|:--:|
|stroke|fill|

No sigils for: erasepage, eofill, rectstroke, rectfill, ustroke, ufill, ueofill, shfill, image, colorimage, imagemask

No sigils for Insideness-Testing Operators: infill, ineofill, inufill, inueofill, instroke, inustroke

No sigils for Form and Pattern Operators: makepattern, setpattern, execform

No sigils for Device Setup and Output Operators: showpage, copypage, setpagedevice, currentpagedevice, nulldevice
## Glyph and Font Operators
|![findfont sigil](../images/sigil_findfont.png)|![scalefont sigil](../images/sigil_scalefont.png)|![setfont sigil](../images/sigil_setfont.png)|![currentfont sigil](../images/sigil_currentfont.png)|![selectfont sigil](../images/sigil_selectfont.png)|![show sigil](../images/sigil_show.png)|![stringwidth sigil](../images/sigil_stringwidth.png)|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|findfont|scalefont|setfont|currentfont|selectfont|show|stringwidth|

No sigils for: definefont, composefont, undefinefont, makefont, rootfont, ashow, widthshow, awidthshow, xshow, xyshow, yshow, glyphshow, cshow, kshow, FontDirectory, GlobalFontDirectory, StandardEncoding, ISOLatin1Encoding, findencoding, setcachedevice, setcachedevice2, setcharwidth

No sigils for Interpreter Parameter Operators: setsystemparams, currentsystemparams, setuserparams, currentuserparams, setdevparams, currentdevparams, vmreclaim, setvmthreshold, vmstatus, cachestatus, setcachelimit, setcacheparams, currentcacheparams, setucacheparams, ucachestatus
