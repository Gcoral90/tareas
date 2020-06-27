from urllib import request

response = request.urlopen('http://google.com')
print(response.read())