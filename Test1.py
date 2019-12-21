import requests
import json

a = requests.get("https://jsonplaceholder.typicode.com/posts")
b = json.loads(a.text)
c = b[0]["title"]


print(c)
print(a.status_code)


