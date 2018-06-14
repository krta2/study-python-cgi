#!python
print("Content-Type: text/html\n")
import cgi, os, View
 
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
    description = description.replace('<', '&lt;')
    description = description.replace('>', '&gt;')
    update_link = '<a href="UpdateData.py?id={}">Update</a>'.format(pageId)
    delete_action = '''
        <form action="DataDeleter.py" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input type="submit" value="delete">
        </form>
    '''.format(pageId)
else:
    pageId = 'Welcome'
    description = 'Hello, web'
    update_link = ''
    delete_action = ''
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
  <a href="CreateData.py">Create</a>
  {update_link}
  {delete_action}
  <h2>{title}</h2>
  <p>{desc}</p>
</body>
</html>
'''.format(title=pageId, desc=description, listStr=View.getList(), update_link=update_link, delete_action=delete_action))