#!C:\Users\iamsa\AppData\Local\Programs\Python\Python36\python.exe
print("content-type:text/html;\n")
import cgi;
x=cgi.FieldStorage();
username=x.getvalue("Username");
email=x.getvalue("Email");
phone=x.getvalue("Phone");
password=x.getvalue("pass1");
print('''
<html>
<head>
<title>Registration Form </title>
<h1>Online Registration Form</h1>
</head>
<body>
<form action="" method="post">
Username:</br>
<input type="text" name="Username" required placeholder="Enter Username"></br>
Email:<br/>
<input type="email" name="Email" required placeholder="Enter Email"></br>
Phone:<br/>
<input type="text" name="Phone" required placeholder="Enter Phone"></br>
Password:<br/>
<input type="Password" name="pass1" required placeholder="Enter Password"></br>
<button type="Submit" name="btn1" value="Submit">Submit</button>
</form>
</body>
</html>
''')
print("username:"+username+"<br/>");
print("email:"+email+"<br/>");
print("phone:"+phone+"<br/>");
print("password:"+password+"<br/>");

