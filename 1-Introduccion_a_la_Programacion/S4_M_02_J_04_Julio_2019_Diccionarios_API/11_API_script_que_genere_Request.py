import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

headers = {
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "ec3a947e-4ecd-4ba4-a68e-2c6b9fbbc4bc,4a892f5d-955c-4e02-ab71-78b8e9906706",
    'Host': "jsonplaceholder.typicode.com",
    'cookie': "__cfduid=d103c727d65b6c4462063e6ce5b8567571562032691",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers)

results = json.loads(response.text)

# VIDEO SCRIPT QUE GENERA
#print(response.text)
#print(response) # <Response [200]>

# VIDEO ANALIZANDO LA RESPUESTA
print(type(results))
#print(results[0])
print(results[0]["userId"]) #<class 'list'>
print(results[0]["title"]) # sunt aut facere repellat provident occaecati excepturi optio reprehenderit

for posts in results:
    print(posts["title"]) #sunt aut facere repellat provident occaecati excepturi optio reprehenderit ...
    


'''
Códigos de respuesta:

1xx : información (¡Espera!) # Se está procesando esto
2xx : respuesta correcta (¡Todo bien!)
3xx : redirección (¡No es aquí!) # apuntando mal a la dirección
4xx : error del cliente (¡Lo hiciste mal!) # el cliente hizo algo mal

401 = se requiere una autenticacion del cliente
403 = si bien se autentico, no tiene permiso para ver el contenido
404 = url no existe

5xx : error del servidor (¡No eres tu!) # el servidor hizo algo mal
'''


