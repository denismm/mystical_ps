#!/usr/bin/env python3
import subprocess
import sys
import os.path

filename = "misc/operator_lists.txt"
output_file = "docs/operators.md"
max_table_width = 8
header = """# Standard Sigils in Mystical

These are the sigils I came up with for built-in PostScript operators.  See [Mystical](../README.md) for more details about this system.
"""

ignored_sigils = ["[", "]", "<<", ">>"]

operator_categories: list[tuple[str, list[str]]] = []
with open(filename, 'r') as f: 
    current_category: str = "--"
    current_operators: list[str] = []
    for line in f:
        line = line.rstrip()
        if line.startswith('## '):
            current_category = line[3:]
            current_operators = []
            operator_categories.append((current_category, current_operators))
        elif line and line not in ignored_sigils:
            current_operators.append(line)

with open(output_file, 'w') as of:
    # write header
    of.write(header)

    skipped_categories: list[str] = []
    for category, operators in operator_categories:
        sigil_list: list[str] = []
        unknown_list: list[str] = []
        for operator in operators:
            sigil_file = f"images/sigil_{operator}.png"
            if os.path.exists(sigil_file):
                sigil_list.append(operator)
            else:
                unknown_list.append(operator)
        unknown_text = ", ".join(unknown_list)
        if sigil_list:
            of.write(f"## {category}\n")
            need_header = True
            while(sigil_list):
                table_width = min(max_table_width, len(sigil_list))
                sigil_line: str = "|"
                caption_line: str = "|"
                if need_header:
                    of.write("| " * table_width + "|\n")
                    of.write("|:--:" * table_width + "|\n")
                    need_header = False
                for operator in sigil_list[:table_width]:
                    caption_line += operator + "|"
                    sigil_file = f"../images/sigil_{operator}.png"
                    sigil_line += f"![{operator} sigil]({sigil_file})|"
                of.write(sigil_line + "\n")
                of.write(caption_line + "\n")
                sigil_list = sigil_list[table_width:]
            of.write("\n")

            if unknown_list:
                of.write(f"No sigils for: {unknown_text}\n")
        else:
            skipped_categories.append(f"**{category}** ({unknown_text})")
    of.write("\n## Skipped categories: \nI haven't yet made sigils for any of the operators in these categories:\n")
    for info in skipped_categories:
        of.write(f"* {info}\n")

    of.write("""
My thanks to Andrew Plotkin for inventing the basic form of the symbol I used for xor, in another context.
    """)
