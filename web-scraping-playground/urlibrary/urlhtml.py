# this code returns all the html tags + contents on  a webpage
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen("http://www.dr-chuck.com/page1.html")
for line in fhand:
    print(line.decode().strip())

