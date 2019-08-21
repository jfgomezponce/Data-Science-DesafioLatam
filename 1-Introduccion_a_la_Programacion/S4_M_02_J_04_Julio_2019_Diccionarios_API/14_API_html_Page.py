import json
import requests

def request(requested_url):
	#url = "https://jsonplaceholder.typicode.com/posts"
	payload = ""
	headers = {
	    'Cache-Control': "no-cache",
	    'Postman-Token': "ec3a947e-4ecd-4ba4-a68e-2c6b9fbbc4bc,4a892f5d-955c-4e02-ab71-78b8e9906706"
	    }

	response = requests.request("GET", requested_url, data=payload, headers=headers)

	return json.loads(response.text)

# /photos  = Recourse
data = request("https://jsonplaceholder.typicode.com/photos")[0:10]

# Definir un contenedor html

html = ""

for photo in data:
	html += "<img src=\"{}\">\n".format(photo["url"])

with open("output.html", "w") as f:
	f.write(html)