#!C:\Users\iamsa\AppData\Local\Programs\Python\Python36\python.exe
print("Content-type: text/html;\n")	
import cgi;
x=cgi.FieldStorage();
c1=x.getvalue("c1");
print('''
<html>
<head>
	<title>BOOKING SUMMARY</title>
</head>
<body>
<h1 style="font-size:1.2em">BOOKING SUMMARY</h1>
<table border="1" cellspacing="0">
<tr><th align="left" nowrap><tt>Person Name:</tt></th><td nowrap><i>"+Person Name+"<br/>")</i></td></tr>
<tr><th align="left" nowrap><tt>No. of People:</tt></th><td nowrap><i>(empty)</i></td></tr>
<tr><th align="left" nowrap><tt>No. of Child:</tt></th><td nowrap><i>(empty)</i></td></tr>
<tr><th align="left" nowrap><tt>Phone:</tt></th><td nowrap><i>(empty)</i></td></tr>
<tr><th align="left" nowrap><tt>Email:</tt></th><td nowrap><i>(empty)</i></td></tr>
<tr><th align="left" nowrap><tt>Total amount:</tt></th><td nowrap><i>(empty)</i></td></tr>
</table>
<p>Processed 2018-04-18 Time-16:23Z
</p>
</body>
</html>
''')

