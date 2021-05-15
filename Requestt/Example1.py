import requests
from requests.exceptions import Timeout 

# r = requests.get('https://xkcd.com/353')

# print(r);  # <Response [200]>
# # print(dir(r))
# # print(help(r))
# print(r.text);
# print()


# download image 

# r = requests.get('https://imgs.xkcd.com/comics/python.png')
# print(r.content)  # in byte 
# print(r.status_code) # 200


# with open('Comic.png', 'wb') as f:
#     f.write(r.content)


# print(r.headers); # response 
# {'Connection': 'keep-alive', 'Content-Length': '90835', 'Server': 'nginx', 'Content-Type': 'image/png', 'Last-Modified': 'Mon, 01 Feb 2010 13:07:49 GMT', 'ETag': '"4b66d225-162d3"', 'Expires': 'Sat, 05 Dec 2020 09:23:19 GMT', 'Cache-Control': 'max-age=300', 'Accept-Ranges': 'bytes', 'Date': 'Sat, 05 Dec 2020 15:52:19 GMT', 'Via': '1.1 varnish', 'Age': '0', 'X-Served-By': 'cache-bom4721-BOM', 
# 'X-Cache': 'HIT', 'X-Cache-Hits': '1', 'X-Timer': 'S1607183539.722751,VS0,VE1100'}



#   get request 
# payload = {'page':2, 'count': 25}
# r = requests.get('https://httpbin.org/get', params=payload)

# # response 
# print(r.text) 
# print(r.url)


# post request 


# payload = {'username': "sanjay_draws", 'password': 'testing'}
# r = requests.post('https://httpbin.org/post', data=payload)

# response 
# print(r.json) # <bound method Response.json of <Response [200]>>
# print(r.json())

# r_dict = r.json()
# print(r_dict['form']) # {'password': 'testing', 'username': 'sanjay_draws'}






# sign in 
# r= requests.get('https://httpbin.org/basic-auth/corey/testing', auth=('corey','testing'))
# r1= requests.get('https://httpbin.org/basic-auth/corey/testing', auth=('corey1','testing'))

# print(r.text)
# print(r1.text)
# print(r1) # <Response [401]>
# print(r)


# url response 
r = requests.get('https://httpbin.org/delay/1', timeout=3)

print(r)







