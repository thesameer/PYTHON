#!C:\Users\iamsa\AppData\Local\Programs\Python\Python36\python.exe
print("content-type:text/html;\n")
import cgi;
x=cgi.FieldStorage();
c1=x.getvalue("c1");
print('''
	<html>
	<head>
	<h1 style='background-color:black;color:yellow;text-align:center;'>
<marquee behavior="alternate">
Book My Show
</marquee>
</h1>
	
	<style>
	<body>
	{
	background-color:blue;
	}</style>
	<div>
	<form action="summary.py" method="post">
''')
print("<input type='text' value='",c1)
print("'readonly='true'>")
print('''
	
	<p><b>Person Name:</p>
<input type="text" name="person" required placeholder="Enter Name"></br></br>
No. of People:<br/>
<input type="number" name="No. of Seats" required placeholder="Select No. of Seats"></br></br>
No. of Child:<br/>
<input type="number" name="No. of Child" required placeholder="Select No. of Seats"></br></br>
Phone:<br/>
<input type="text" name="Phone" required placeholder="Enter Phone"></br></br>
Email:<br/>
<input type="text" name="Email" required placeholder="Enter Email"></br></br>
Total amount:<br/>
<input type="text" name="Amount" required placeholder="Enter Amount"></br></br>
<button type="Submit" name="btn1" value="Submit">Submit</button>
<input type="reset">
</form>
</body>
</head>
''')