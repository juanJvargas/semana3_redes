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
	aux =aux+1
