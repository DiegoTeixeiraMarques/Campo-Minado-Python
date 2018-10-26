import servidorControle
import socket
from datetime import datetime
import ast
import subprocess

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000            # Porta que o Servidor esta
HOST = ''     	       # Endereco IP do Servidor



def server():

    #Abrindo um socket UDP na porta 5000
    orig = (HOST, PORT)																
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)

    while True:
        #subprocess.call('cls', shell=True)

        #recebi dados
        data, address = sock.recvfrom(MAX_BYTES) # Recebi dados do socket
        data = data.decode(ENCODE)               # Convertendo dados de BASE64 para UTF-8
        data = str(data)
        data = ast.literal_eval(data)
        print(data.keys())
        print(data.values())
        if (data['played'] == 0):
            sizeField = data['line']
            numberBomb = data['column']
            cm = servidorControle.CampoMinado(sizeField, numberBomb)
            print(cm.dict.keys())
            cm.showCleanField()
            cm.showMineField()
        else:
            cm.played(data['line'], data['column'])                

        cm.showMineField()
        answer = str(cm.dict)
    

        #Envia resposta
        #text = "Total de dados recebidos: " + str(len(data)) 
        answer = answer.encode(ENCODE) # Codifica para BASE64 os dados 
        sock.sendto(answer, address) # Enviando dados	

server()