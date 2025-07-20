#!/usr/bin/env python3

import fileinput

# read in a postscript program A
# write out a postscript program that draws a mystical version of A

string_accumulator = ""
paren_count = 0
header = True

print("""%!
(mystical.ps) run
72 dup scale
4.25 5.5 translate
4 dup scale

{
""")

for line in fileinput.input():
    if header and line.startswith('%!'):
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
        print(line_out, end="")
    else:
        if string_accumulator:
            string_accumulator += line
        else:
            print(line, end="")


print("} mystical\nshowpage\n")
