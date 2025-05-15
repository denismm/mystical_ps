#!/usr/bin/env python3
import sys

filename = sys.argv[1]

sigil_rows: list[list[str]] = []

with open(filename, 'r') as f:
    for line in f:
        sigil_rows.append(line.split())

table_width = max([len(r) for r in sigil_rows])

# print header
print("| " * table_width + "|")
print("|:--:" * table_width + "|")

# print rows
for row in sigil_rows:
    sigil_line: str = "|"
    caption_line: str = "|"
    for operator in row:
        caption_line += operator + "|"
        sigil_file = f"images/sigil_{operator}.png"
        sigil_line += f"![{operator} sigil]({sigil_file})|"
    print(sigil_line)
    print(caption_line)
