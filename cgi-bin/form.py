#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import html

form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1", "nothing")
text2 = form.getfirst("TEXT_2", "nothing")
text1 = html.escape(text1)
text2 = html.escape(text2)

print(text2)

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
	   <meta charset="utf-8">
           <title>Maza Faka</title>
        </head>
        <body>""")

print("<h1>Title</h1>")
print("<p>TEXT_1: {}</p>".format(text1))
print("<p>TEXT_2: {}</p>".format(text2))

print("""</body>
        </html>""")