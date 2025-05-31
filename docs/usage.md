# Mystical usage notes

## Functions defined in main dictionary by mystical.ps

### Full renderers
`mystical`: takes an array, xarray, or dict and renders it in mystical, descending into substructures as necessary.  The entire image will be scaled to fit into a unit circle. 

`mystical_evoke`: The same as `mystical` but it takes a name that is looked up in the current dictionary.

`mystical_evoke_label`:  Like `mystical_evoke` but adds a name-def ligature with the name at the top and orients the image so that the name sigil is right-side-up.

All of these have versions with `_unscaled` appended to them that skip the scaling step.  The rings will be 1 unit thick so the image will be quite large.

### Parsing and rendering functions

`mystical_get_spell`: takes an array, xarray, or dict and returns a Spell object (see below for object definitions).

`mystical_scale_spell`: takes a Spell and scales the current space to fit the spell within a 1-unit circle.

`mystical_draw_spell`: takes a Spell, scales it with `mystical_scale_spell`, and renders it.

`mystical_make_evocation_ligature`: takes a Spell and a string, returns a Token that will render as a def-ligature with that string as the name.  The ligature will be rendered as if it's at the top of an inside-out ring large enough to contain the spell.

`mystical_draw_evocation_label`: takes a Spell and a string, calls `mystical_make_evocation_ligature`, and renders it.

## Presentation control

The font for spells is set at the top of mystical.ps with `/Zapf-Chancery 0.5 selectfont`.  Setting a different font before calling any mystical functions should change the font throughout, though some other values might need adjusting if the font size changes.  Be sure to call it before layout since stringwidth is often used.

### useful values set in mystical_dict

These can be set in mystical_dict to change behavior.

* `ring_spacing` (default 2): this is the distance from the parent ring radius (which is not the outside of the ring) to the full_radius of the child ring.  It needs to be at least 1 to leave room for the ring_halfwidth and the cross bar of the return sigil.
* `ring_width` (default 1) , `ring_halfwidth` (default 0.5): The width of the band of the ring, containing text and sigils.  `ring_width` is never actually used.
* `sibling_spacing` (default 0.5), `sibling_hs` (default 0.25): distance between rings with the same parent.  Again, `sibling_spacing` is never used.
* `kerning` (default true): whether to layout sigils and text based on their actual width.  If this is false, every object will be considered to be std_sigil_width wide.  This will result in overlaps for long text.
* `std_sigil_width` (default 1.25): how wide a sigil should be considered to be during layout. Sigils are generally within a 1-unit square so this will give them a little space on either side.
* `nonsigil_spacing` (default 0.125): how much space to add to the horizontal stringwidth (in the current font) of nonsigils for layout.  Strings have this added twice to leave room for the cartouche.
* `cartouche_radius` (default 0.25): the radius of the end-caps of the cartouches around strings, and thus half the width of the long section of the cartouches.  This should be at least half the height of the current font.
* `nib_angle` (default -60): this is used in `nstroke`, see below.

### nstroke and ndot

All strokes are done with the `nstroke` function, which is a calligraphic stroke (sing dmmlib/lines.ps) with a linewidth of 1/24 by 1/48 rotated by nib_angle (defaulting to -60).  This angle is from the reading direction for each token and from the return sigil for each ring.  I also use `ndot` for a 1/16 x 3/64 ellipse at the same angle.  The nib_angle value can be redefined before rendering, or `nstroke` and `ndot` can be redefinded to `stroke` and `dot` (a dmmlib/base.ps function).

## Objects

mystical rendering creates two types of objects, Spell and Token.  These correspond to rings and sigils/text.

### Spell fields

* `components`: a list of Token objects, in code order
* `circumference`: the sum of the widths of all components
* `radius`: the distance from the center of the ring to the middle of the band
* `rull_radius`: the distance from the center of the ring to the farthest point on any subring, or the outside of the band if there are none
* `rtype`: /array, /dict, or /xarray

    
### Token fields

* `name`: the text of a string or the name of an object.
* `otype`: the postscript type of the object, made non-executable, or /return for return tokens.
* `xflag`: true if the object is executable.
* `aflag`: true if the object is an array, xarray, or dict.
* `position`: the position along the circumference of the token.
* `angle`: the angle at which the token will be drawn.
* `parent`: the ring containing this token.

For rings:
* `offset`: how far the center of the ring is from its parent.
* `ring_angle`: at what angle the ring is drawn.  Can be different from `angle`.
* `ring`: the Spell object.

For name-def ligatures:
* `defligature`: true if this is a name-def ligature, unset otherwise.
