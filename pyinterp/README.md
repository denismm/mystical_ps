# Python Interpreter for Mystical Images

This is a nascent python interpreter for mystical images. Or, more specifically, a python interpreter for the post script files used to generate mystical images. This is pretty early stage, so a lot of grammar is missing and loads of opportunities to refine and improve the syntax, but it's a neat proof of concept!


## How to use:
In the parent directory:
```
python -m run_mystical.py path/to/your.ps
```
This will:
- Lex the ps file into a tokens: `mystical_lexer.py`
- Parse the tokens to build an abstract syntax tree (AST): `mystical_parser.py`
- Recursively walk the tree, and use each nodes `.to_python()` method to build a python script as a string
- Run the string as python and print the result (for now)


## ✨Magical✨Vocabulary Used in This Interpreter
- Spell: The whole *.ps file
- Inscription: A funcion
- Cast: A function call
- Invocation: What you do with the result of a spell, i.e. print the result of this script uses a {exec} 'invocation' 
    - I could imagine this being extended to things like "save" to save the python script as .py file, or "graph" to graph the result as another mystical .ps file. You could even get crazy with a "chant" invocation, that translates your spell's result to play a chime on your computer or something!
- Sigil: Any item in an array or xarray, not just the special sigils made available in mystical.ps (just for convenience of description, not sure if this is the best way to think about it?)
- Fizzle: An exception that gets raised because of improper mystical syntax

### Less fun but still important
- Array/XArrays, as per parent director readme
- BinOp - Binary Operations
- Unop - Unary operations like sqrt (not implemented)
- NullOp - Nullary Operators like rand (not implemented)



## Grammar for the Interpreter

This grammar is just what made sense to me as I started to draw my own mystical rings. I don't know postscript, so I likely am making some crazy grammar rules that don't make a lot of sense in the context of postscript. That said, here's what I came up with. Looking at this file for arithmagic.ps:

![arithmagic.ps visualized](arithmagic.png)

```
(mystical.ps) run 
(dmmsigils.ps) run

/add_two_numbers_and_run {
    { 
        5
        {3 8 add} 
        mul
     {exec}
     } mystical_unscaled 
    } def


50 softscale
7 9 translate
add_two_numbers_and_run
showpage
```

- The run statemens at the top are classified as "import" statements and ignored by the interpreter as they are just used to draw the file
- `/add_two_numbers_and_run { ... mystical_unscaled} def` is a 'magical inscription'. An Inscription because it's a function, magical because it includes the `mystical_unscaled` command
- The inscription is made up two commands:
    - a binary operation that multiplies 5 * a nested executable array
        - that nested array is another binop 3 + 8 (=11)
    - An `{exec}` invocation. When this function is ran, the result will be printed out
- the softscale and translate and showpage commands are also ignored as they are also just used to draw the file
- the `add_two_numbers_and_run` inscription is cast when the function is called at the end of the page

### How I am reading the Mystical Image
- Begin at unassigned "start" sigil (not called out as a "start" sigil in [sigils documentation](docs/sigils.md), but I think it's fair to call it that?).
- Move widdershins to add 5 to the stack, continue in that direction
- Next is a ligature that takes us to another executable array, go to that ring.
    - Add 3 and 8 to the stack
    - Hit the add operator to get 11
- Return back down the ligature to the original ring, to replace that position with "11"
- Hit the multiply operator to multiply 5*11 to get 55
- Send that 55 down the "invocation" ligature to the top ring
- Hit the exec sigil to return 55.


### How to Cast this Spell
When I run `arithmagic.ps` as an argument to `run_mystical.py`, it will return output 55.
 

### Notes: 
- At this time I haven't done much with arrays, mostly just working with xarrays.
- I don't know how to send arguments to a function in post script, I gotta learn how to do that and implement it here
- Right now the invocation lives inside another executable array. I think it would be cool if it was a ligature going directly to a invocation sigil instead, but I couldn't figure out how to draw ligatures to anything other than arrays and xarrays


## Future Features?
- Test coverage
- More sigil handling:
    - Binary operations are parsed in a pretty clunky way right now, would like to improve that
    - Nullary and Unary operations
    - String handling, i.e. "(hello world)" patterns
    - Boolean handling, bitwise operators and if statements
    - Loop handling
- More support for Arrays and maybe array operations?
- Reconstructing a mystical .ps file from the output of `run_mystical.py`
- GUI that shows the spell in `foo.ps` "transform" into the result if it runs correctly OR alternately, if the mystical code is invalid, the spell "fizzles" in some visually interesting way.
- Variable Assignments? 
    - Not sure how this would work in the syntax, but it would be better than just storing a long string of python code after a "return" statement like it currently does


## Mystical Application Ideas?
I am really excited about mystical because I think it could make a really cool puzzle game. I'm using arithmetic in this interpreter, but what if we could replace `1 2 add` with `water heat add` and get steam! For that though, we'd need some kind of UI for users to create mystical spells that could be translated into valid .ps files reliably. 




