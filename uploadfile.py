#!/usr/local/bin/python2.2
from cgi import FieldStorage
header=”Content-type:text/html\n\n”
dynhtml=”””<html>
<head>
<title>File upload</title>
</head>
<body>
<form action=”/cgi-bin/uploadfile.py” method=”POST”
enctype=”multipart/form-data”>
<input type=”file” name=”file_name” size=”50”>
<input type=”submit”>
</form>
</body>
</html>”””
shtml = ‘’’<HTML><HEAD><TITLE>
</TITLE></HEAD>
<BODY>
<H3>Contents: %s</H3>
<PRE>%s
</PRE>
</BODY></HTML>’’’
form=FieldStorage()
if not form:
    print (header+dynhtml)
elif form.has_key(“file_name”):
    fileupload=form[“file_name”]
    data=’ ‘
    if fileupload.file:
        count=0
        while 1:
            line=fileupload.file.readline()
            data=data+line
            if not line:
                break
            count=count+1
        print (header+shtml % (fileupload.filename,data))
else:
pass
