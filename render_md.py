#!/usr/bin/env python3
import git
from markdown_it import MarkdownIt
import sys
import re
from datetime import date
from glob import glob

md_file = sys.argv[1]
html_file = md_file.replace('.md', '.html')
if md_file == html_file:
    raise ValueError("file collision {md_file}")

# read and parse markdown
with open(md_file, 'r') as f:
    page_lines = list(f)
title = page_lines[0]
if not title.startswith ('# '):
    raise ValueError(f"README.md in {location} should start with H1")
title = title[2:]

# render markdown
page_md = "".join(page_lines)
md_parser = MarkdownIt('commonmark', {'breaks':False,'html':True}).enable('table')
page_html = md_parser.render(page_md)

# correct md links
page_html = re.sub(r'(<a href="[^\"]*)\.md(\">)', r'\1.html\2', page_html)

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
with open(html_file, 'w') as of:
    print(header, file=of)
    print(page_html, file=of)
    print(footer, file=of)
