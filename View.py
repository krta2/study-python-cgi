import os
def getList():
    files = os.listdir('data')
    listStr = ''
    for item in files:
        listStr = listStr + '<li><a href="DataList.py?id={name}">{name}</a></li>'.format(name=item)
    return listStr