#!python
print("Content-Type: text/html\n")
import cgi, os
 
files = os.listdir('data')
listStr = ''
for item in files:
    listStr = listStr + '<li><a href="DataList.py?id={name}">{name}</a></li>'.format(name=item)
 
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
else:
    pageId = 'Welcome'
    description = 'Hello, web'
print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="DataList.py">WEB</a></h1>
  <ol>
    {listStr}
  </ol>
  <form action="DataCreator.py" method="post">
      <p><input type="text" name="title" placeholder="title"></p>
      <p><textarea rows="4" name="description" placeholder="description"></textarea></p>
      <p><input type="submit" value="Create"></p>
  </form>
</body>
</html>
'''.format(title=pageId, desc=description, listStr=listStr))