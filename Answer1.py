import requests

post=requests.get("https://my-json-server.typicode.com/typicode/demo/posts")
comment=requests.get("https://my-json-server.typicode.com/typicode/demo/comments")

list=[post,comment]
for i in list:
    print("Combined data both posts/comments : ",i.text)
