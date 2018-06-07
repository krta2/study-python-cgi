#!python
import cgi, os
form = cgi.FieldStorage()
pageId = form["pageId"].value
 
os.remove('data/'+pageId)
 
#Redirection
print("Location: DataList.py")
print()