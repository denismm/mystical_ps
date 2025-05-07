#!/usr/bin/env python3
import git
from markdown_it import MarkdownIt
import sys
from datetime import date
from glob import glob

mdfile = sys.argv[1]

# read and parse markdown
with open(mdfile, 'r') as f:
    readme_lines = list(f)
title = readme_lines[0]
if not title.startswith ('# '):
    raise ValueError(f"README.md in {location} should start with H1")
title = title[2:]

# render markdown
readme_md = "".join(readme_lines)
md_parser = MarkdownIt('commonmark', {'breaks':False,'html':True}).enable('table')
readme_html = md_parser.render(readme_md)

# insert header
header = f"""
<html>
<head>
    <title>{title}</title>
    <link rel="alternate" type="application/rss+xml" href="http://www.suberic.net/~dmm/changes.xml"/>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
</head>
<body>
"""

today = date.today()

footer = f"""
<hr/>
<address>This page generated {today.isoformat()} by <a href="/~dmm/">Denis</a>.</address>
</body></html>
"""
# print html
print(header)
print(readme_html)
print(footer)
