# Mystical mode for PostScript
big pretty example

I wanted to make a programming language that resembled magical circles. This is more like a way to write PostScript that looks like a magical circle. 

## Circles
There are three types of circles in Mystical:
* executable arrays, written in {} in ps, are represented as circles of text and sigils, with an inner and outer border, and a star of some sort inside.
* non-executable arrays, written in [] in ps, are the same but without the star.
* dictionaries, written in << >> in ps, are polygons with a double outer border and a circular inner border.

xarray example array example dict example

When one of these structures appear inside a different structure, a circle or dot leads from the inclusion point to the inner circle's start/end sigil.

link example

It is theoretically possible to use [ ] and << >> in ps in ways that Mystical can't handle:
```
[ 1 2 3 split { ] /first exch def [ } if 4 5 6 ] /final exch def
```
so don't do that.

Other commands like `gsave/grestore` and `begin/end` are more likely to be used in non-balanced or loop-crossing ways so those are treated as normal sigils below.

## Sigils
The circles' rims contain text or sigils.  Sigils are symbols that stand in for operators, variables, or other keywords. Any name, written in ps as `/name`, is instead written with a triangle surrounding or superimposing the text of the name or its sigil.

### Standard Sigils
Many built-in operators have been given their own sigils.  These are used in place of the text of the operator.  I have generally made these sigils based on the initial of the command and an illustration of the concept, though in some cases I have taken a more fully illustrative route or created some standard visual language.

in order from ps ref

### User Sigil Advice
Sigils for new functions or names can be added to `sigil_bank` at runtime.

Sigils for user variables can be made with any sigil system.  My examples use letter collision, inspired by Spare's Chaos Magick system, but anything that turns a word into a symbol will work - kameas, wheels, Square Word Calligraphy, illustration, puns, etc.

## Sample Algorithms
