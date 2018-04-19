#!C:\Users\iamsa\AppData\Local\Programs\Python\Python36\python.exe
print("content-type:text/html;\n")
print('''
<!DOCTYPE html>
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
			color:white;
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
<form action="continue.py" method="post">
<p>
select movie name:</p>
<select name="cc">
<option value="selected">none</option>
<option value="Black Panther">Black Panther</option>
<option value="Avengers">Avengers</option>
<option value="Lucy">Lucy</option>
</select></br></br>
<button type="Submit" name="btn1" value="Submit">Continue</button>
</form>
</div>
</center>
</body>
</html>
   ''')