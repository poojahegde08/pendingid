from urllib.request import urlopen
import json

url = "https://jsonplaceholder.typicode.com/todos"
response = urlopen(url)
data = json.loads(response.read())

pending = {}

for each in data:
    if not each['completed']:
        pending[each['userId']] = pending.get(each['userId'], 0) + 1

print(pending)
