#!C:\Users\iamsa\AppData\Local\Programs\Python\Python36\python.exe
print("content-type:text/html;\n")
import cgi;
x=cgi.FieldStorage();
c1=x.getvalue("cc");
print('''
<html>
<head>
	<title>BookMyShow</title>
	<h1 style='background-color:black;color:yellow;text-align:center;'>
<marquee behavior="alternate">
Book My Show
</marquee>
</h1>
	<style>
		#box1
		{
			border: 1px solid black;
			width: 620px;
			height: 349px;
			box-shadow: 40px 50px 80px yellow;
		}
		#f1
		{border: 1px solid black;
			width: 200px;
			height: 150px;
			color:yellow;
			background-color:black;
			box-shadow: 10px 20px 30px black;
			}
	</style>
</head>
<body>
	<center>
<div id="box1">
<img src="https://www.pixelstalk.net/wp-content/uploads/2016/04/Free-avengers-backgrounds-620x349.jpg">	
</div>
</br></br></br></br>

<div id="f1">

<form action="submit.py" method="post">
<br><button type="Submit" name="btn1" value="Submit">Confirm</button>
</form>
''')
print(c1)
