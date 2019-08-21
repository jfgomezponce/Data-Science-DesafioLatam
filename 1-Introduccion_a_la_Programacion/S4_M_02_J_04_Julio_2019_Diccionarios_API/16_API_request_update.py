import requests

url = "https://jsonplaceholder.typicode.com/posts/20"

payload = "{\n\t\"title\":\"nuevo titulo\",\n\t\"body\":\"Este es un cambio\",\n\t\"userId\":1\n}"
headers = {
    'Content-Type': "application/json",
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "d6d63537-6998-494c-bf48-e70e6f159f0c,790c2203-e22c-4e19-ba27-e5cbf415e744",
    'Host': "jsonplaceholder.typicode.com",
    'cookie': "__cfduid=d103c727d65b6c4462063e6ce5b8567571562032691",
    'accept-encoding': "gzip, deflate",
    'content-length': "69",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("PUT", url, data=payload, headers=headers)

print(response.text)

'''
{
  "title": "nuevo titulo",
  "body": "Este es un cambio",
  "userId": 1,
  "id": 20
}
'''