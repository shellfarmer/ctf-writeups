### sql

> I created a login form for my web page. Somehow people are logging in as admin without my password though!
Can you fix my login code for me?

Simple SQL injection attack bypassing auththentication.  Use real_escape_string to sanitise input.

Changes:
```
16 -  $user = $_POST['username'];
17 -  $pass = $_POST['password']; 
16 +  $user = $conn->real_escape_string($_POST['username']);
17 +  $pass = $conn->real_escape_string($_POST['password']); 
```

