# Installation of Mystical

This is very sloppy.  I intend to improve both the code organization and this document.

## Get Mystical

Clone the mystical repo.

```
git clone <mystical_ps repo>
cd mystical_ps
```

## Get dmmlib

Clone the dmmlib repo into a subdirectory of the repo, or clone it elsewhere and make a soft link to it.  Your mystical directory should have a dmmlib directory in it.  The mystical .gitignore already knows to ignore dmmlib.

`git clone git@github.com:denismm/dmmlib.git`

### pstopng

dmmlib includes a perl script, `dmmlib/bin/pstopng`, which automates rendering PostScript code to an image.  It's very idiosyncratic as nobody else has used it but it works for my purposes.  It does require that you have not only ghostscript but also the netpbm utilities installed.

## Install ghostscript

This is what I use.  It's important that you be able to specify that you want to allow running of code in other files that may be in subdirectories.  This is generally a dangerous thing to do - I'm working on making it unnecessary - but for now I'm asking you to trust me that there's no code in dmmlib that reformats your hard drive.

I'm not going to tell you how to install gs - good chance that whatever you're currently doing for package management knows how to get it.

## Make an alias to generate pdfs

The OSX builtin pstopdf does not allow execution of included files in subdirectories.  I have this defined in my bin directory, alter it appropriately:

```
> cat ~/bin/gstopdf
#!/usr/bin/perl
use strict;
use warnings;
use autodie;
die "No files" if @ARGV == 0;
foreach my $psfile (@ARGV) {
    my ($basefile) = $psfile =~ /^(.*).ps$/ or die "Not a ps file: $psfile";
    my $pdffile = $basefile . ".pdf";
    system ("/usr/local/bin/gs", "-r720", "-dNOSAFER", "-dNOPAUSE", "-dNOEPS", "-sDEVICE=pdfwrite", "-sOutputFile=$pdffile", "-dBATCH", "$psfile");
}
```

## Bonus: install a ps viewer

I use gv, which requires X and is only available on homebrew through a nonstandard cask, because I like its functionality much more than gsview, but in any case it's useful to be able to interpret ps without generating a pdf.  You will need to add the `-dNOSAFER` option to "gs options" in whatever tool you use.

## Get started

See [Getting Started with Mystical](docs/intro.md).
