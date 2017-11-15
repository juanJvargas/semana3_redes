import requests
import transmissionrpc

tc = transmissionrpc.Client('localhost', port=9091)
torrents=tc.get_torrents()
size = len(torrents)
print(size)
aux=0
while aux!=size:
	magnetlink="";
	magnetlink=torrents[aux].magnetLink
	magnetlink=magnetlink.replace("?","$")
	magnetlink=magnetlink.replace(".","^")
	magnetlink=magnetlink.replace("%","|")
	progreso=torrents[aux].progress
	url="https://proyectoredestorresvargas.herokuapp.com/actualizar/"+magnetlink+","+str(progreso)
	response=requests.get(url)
	print(response.content)
	aux=aux+1