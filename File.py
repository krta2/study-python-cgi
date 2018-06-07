#!python
print("Content-Type: text/html\n")
import cgi
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
else:
    pageId = 'Welcome'
    description = 'Hello, Web!'
print('''<!doctype html>
<html>
<head>
<title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="File.py">WEB</a></h1>
  <ol>
    <li><a href="File.py?id=HTML">HTML</a></li>
    <li><a href="File.py?id=CSS">CSS</a></li>
    <li><a href="File.py?id=JavaScript">JavaScript</a></li>
    <li><a href="File.py?id=Python">Python</a></li>
  </ol>
  <h2>{title}</h2>
  <p>{desc}</p>
</body>
</html>
'''.format(title=pageId, desc=description))