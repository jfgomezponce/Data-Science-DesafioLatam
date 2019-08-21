import requests
import json

def request(requested_url, api_key='0JHhxBBth62bH7Up3CdxZx1K4GH8Az7myS4GHQKd'):

    #url = requested_url+'?sol=1&api_key='+api_key

    querystring = {"sol":"1","api_key":"0JHhxBBth62bH7Up3CdxZx1K4GH8Az7myS4GHQKd"}

    headers = {
        'User-Agent': "PostmanRuntime/7.15.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "92589247-f9c0-4870-80cc-6d62ba32cc4c,3acd603a-0a12-4a9a-a554-c21a5b9ff542",
        'Host': "api.nasa.gov",
        'accept-encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    response = requests.request("GET", requested_url, headers=headers, params=querystring)
    #response = requests.request("GET", url, headers=headers)

    return json.loads(response.text)

def build_web_page(diccio_nario):
    html = "<html>\n<head>\n</head>\n<body>\n<ul>\n"

    for photo in diccio_nario["photos"]: # Se itera sobre "photos", equivalente a la primera clave del primer diccionario
        html += "\t<li><img src=\"{}\">\n".format(photo["img_src"]) # Se itera sobre img_src (clave del diccionario)

    html+="</ul>\n</body>\n</html>"

    with open("prueba.html", "w") as f:
        f.write(html)

def photos_count(diccio_nario):
    camaras = []
    totales = []
    for photo in diccio_nario["photos"]:
        camaras.append(photo["camera"]["name"])
        #print(camaras)
        totales.append(photo["rover"]["total_photos"])

    return (dict(zip(camaras,totales)))
        #dicc = {k:v for k,v }


diccionario = request("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos")
build_web_page(diccionario)
photos_count(diccionario)
