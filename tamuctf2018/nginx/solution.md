### nginx
> My friend set up a web server using nginx but he keeps complaining that people are finding files that they are not supposed to be able to get to. Can you fix his configuration file for him?

The web root path is incorrect allow access to everything in /

Changes:

```
36 -	root /;
36 +	root /usr/share/nginx/html/;

45 -    index /usr/share/nginx/html/index.html;
45 +    index index.html;
```
