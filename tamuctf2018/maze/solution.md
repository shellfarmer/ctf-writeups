### maze
> I created this really cool CTF challenge where users are supposed to bypass client side authentication to get a flag. However it seems like people are able get the flag through other means!
Can you find and fix the problem in my challenge for me?

Local file include allows flag file to be read.   Added a check if the path includes flag then it will return index instead.

Changes:
```
33 -    if (filePath == __dirname)
33 +	if (filePath == __dirname || filePath.indexOf('flag'))
```
