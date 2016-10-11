#!/usr/bin/python
import http.client
x=http.client.HTTPConnection('www.ruby-lang.org',80)
x.connect()
x.request('GET','/index.html')
y=x.getresponse()
z=y.read()
print (z)
