import requests
import transmissionrpc

tc = transmissionrpc.Client('localhost', port=9091)

url="https://proyectoredestorresvargas.herokuapp.com/pendiente"
response=requests.get(url)
info= response.content
descargar = info.split(",")
size=len(descargar)-1
aux=0
while aux!=size:
	tc.add_torrent(descargar[aux])
	last= len(tc.get_torrents())
	torrent=tc.get_torrent(last)
	name= torrent.name
	magnetlink=descargar[aux]
	magnetlink=magnetlink.replace("?","$")
	magnetlink=magnetlink.replace(".","^")
	magnetlink=magnetlink.replace("%","|")
	name=name.replace(" ","=")
	url="https://proyectoredestorresvargas.herokuapp.com/actualizar"+ magnetlink +","+name
	response=requests.get(url)
	aux =aux+1
