import http.client
x=http.client.HTTPConnection("http://classdata.readthedocs.io/en/latest/section.html",80)
x.connect()
x.request('GET','/section.html')
y=x.getresponse()
z=y.read()
print (z)

