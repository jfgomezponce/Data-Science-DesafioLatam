
import requests
import json

def request(method, url, payload=''):

	headers = {
	    'User-Agent': "PostmanRuntime/7.15.0",
	    'Accept': "*/*",
	    'Cache-Control': "no-cache",
	    'Postman-Token': "f9720629-9cb3-478f-834e-8c319d05b5bd,11b3518d-2337-42db-b960-61c61043edd2",
	    'Host': "reqres.in",
	    'accept-encoding': "gzip, deflate",
	    'Connection': "keep-alive",
	    'cache-control': "no-cache"
	    }

	
	
	if method == "DELETE":
		url += '/2'
		response = requests.request(method, url, data=payload, headers=headers)
		return response
		#response = requests.request(method, url, data=payload, headers=headers)
	else:
		response = requests.request(method, url, data=payload, headers=headers)
		return json.loads(response.text)
	

#url = "https://reqres.in/api/users"

#verbo = 'GET'
#verbo = 'PUT'
#verbo = "DELETE"
#verbo = 'POST'

#print(request(verbo,url))

#diccionario = request(verbo,url)


# DESAFIO 2
#print(diccionario["data"][0])
#Utilice la función del ejercicio 1 para listar los usuarios, 
#e imprima el retorno en pantalla (por defecto mostrará 3)
diccionario = request("GET", "https://reqres.in/api/users")
usuarios = []
for i in diccionario["data"]:
	usuarios.append(i["id"])
print (usuarios)

# DESAFIO 3
#Utilice la función del ejercicio 1 para crear un usuario, 
#e imprima el retorno en pantalla
diccionario2 = request("PUT", "https://reqres.in/api/users")
print(diccionario2)

# DESAFIO 4
#Utilice la función del ejercicio 1 
#para actualizar un usuario, e imprima el retorno en pantalla
diccionario3 = request("POST", "https://reqres.in/api/users")
print(diccionario3)

# Desafío 5
# Utilice la función del ejercicio 1 para 
# eliminar un usuario, e imprima el retorno en pantalla
diccionario4 = request("DELETE", "https://reqres.in/api/users")
print(diccionario4)

