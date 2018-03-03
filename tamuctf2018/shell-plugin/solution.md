### shell-plugin

>I'm running a CTF competition that is geared towards newer students. I know that most of the students don't have easy access to a linux machine so why not give students shell access to my server so that they can use it to solve challenges?

>In order to make this a reality I wrote this cool plugin for CTFd to automatically create an account when they register for the competition.
One of the students claims that they can get a root shell on my server though. Can you figure out what happened and fix the issue for me?

Code suffers from command injection.  Added a fuction to escape quotes and modified the add-user and change-user-pass system calls. 

Changes: 

```

16 +  def shellquote(s):
17 +    return "'" + s.replace("'", "'\\''") + "'"
18 +
17 -  os.system("./add-user.sh " + name + " " + password)
20 +  os.system("./add-user.sh " + shellquote(name) + " " + shellquote(password))
20 -  os.system("./change-user-pass.sh " + name + " " + password)
23 +  os.system("./change-user-pass.sh " + shellquote(name) + " " + shellquote(password))
```


