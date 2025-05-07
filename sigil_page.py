#!/usr/bin/env python3
import subprocess
import sys
import os.path

filename = "misc/operator_lists.txt"
output_file = "docs/operators.md"
max_table_width = 8
header = """# Standard Sigils
These are the sigils I came up with for built-in operators.
"""

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
        elif line:
            current_operators.append(line)

with open(output_file, 'w') as of:
    # write header
    of.write(header)

    for category, operators in operator_categories:
        sigil_list: list[str] = []
        unknown_list: list[str] = []
        for operator in operators:
            sigil_file = f"images/sigil_{operator}.png"
            if os.path.exists(sigil_file):
                sigil_list.append(operator)
            else:
                unknown_list.append(operator)
        if sigil_list:
            of.write(f"## {category}\n")
            table_width = min(max_table_width, len(sigil_list))
            sigil_line: str = "|"
            caption_line: str = "|"
            for operator in sigil_list[:table_width]:
                caption_line += operator + "|"
                sigil_file = f"../images/sigil_{operator}.png"
                sigil_line += f"![{operator} sigil]({sigil_file})|"
            of.write(sigil_line + "\n")
            of.write("|:--:" * table_width + "|\n")
            of.write(caption_line + "\n")
            of.write("\n")

            if unknown_list:
                of.write(f"Unknown: {unknown_list}\n")
        else:
            of.write(f"\nNone: {category}\n")
