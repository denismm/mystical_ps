#!/usr/bin/env python3

import fileinput
import re

# read in a postscript program A
# write out a postscript program that draws a mystical version of A

string_accumulator = ""
paren_count = 0
header = True

comment_regex = re.compile(r'^(\s*)%\s*(.*)\s*$')

unprocessed_lines = list(fileinput.input())

# find adjacent lines that start with same number of spaces before comment

lines = []
previous_comment_indent = -1
header = True
for line in unprocessed_lines:
    if header and line.startswith('%'):
        previous_comment_indent = -1
    elif m := comment_regex.match(line):
        header = False
        new_indent = len(m.group(1))
        if new_indent == previous_comment_indent:
            lines[-1] = lines[-1].rstrip()
            lines[-1] += "\\n"
            lines[-1] += m.group(2)
            lines[-1] += "\n"
            continue
        else:
            previous_comment_indent = new_indent
    else:
        header = False
        previous_comment_indent = -1
    lines.append(line)

output_lines = []
header = True
for line in lines:
    if header and line.startswith('%'):
        continue
    header = False
    if '(' in line or ')' in line or '%' in line:
        # special handling to find comments
        slash = False # did we just see a slash?
        line_out = ""
        for i, character in enumerate(line):
            if paren_count:
                if slash:
                    string_accumulator += "\\"
                    string_accumulator += character
                    slash = False
                elif character == '\\':
                    slash = True
                elif character == '(':
                    string_accumulator += character
                    paren_count += 1
                elif character == ')':
                    string_accumulator += character
                    paren_count -= 1
                    if paren_count == 0:
                        line_out += string_accumulator
                        string_accumulator = ""
                else:
                    string_accumulator += character
            elif character == '(':
                string_accumulator = character
                paren_count = 1
            elif character == '%':
                comment_text = line[i+1:-1].strip()
                line_out += f"({comment_text}) /mystical_comment_flag pop pop\n"
                break
            else:
                line_out += character
        output_lines.append(line_out)
    else:
        if string_accumulator:
            string_accumulator += line
        else:
            output_lines.append(line)

print("""%!
(mystical.ps) run
72 dup scale
4.25 5.5 translate
4 dup scale

{ """)

for line_out in output_lines:
    print(line_out, end="")

print("} mystical\n\nshowpage\n")
