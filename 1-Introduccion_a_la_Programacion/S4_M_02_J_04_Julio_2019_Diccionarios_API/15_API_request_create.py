import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = "{\n\t\"title\":\"Post 101\",\n\t\"body\":\"Este es nuestro primer post\",\n\t\"userId\":1\n}"
headers = {
    'Content-Type': "application/json",
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "35576862-8016-4cca-97ac-5e597fce72a1,15a8b212-06e0-486b-a4b9-4a8c07bda5c3",
    'Host': "jsonplaceholder.typicode.com",
    'cookie': "__cfduid=d103c727d65b6c4462063e6ce5b8567571562032691",
    'accept-encoding': "gzip, deflate",
    'content-length': "75",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

'''
SALIDA identica a la de Postman

{
  "title": "Post 101",
  "body": "Este es nuestro primer post",
  "userId": 1,
  "id": 101
}

'''