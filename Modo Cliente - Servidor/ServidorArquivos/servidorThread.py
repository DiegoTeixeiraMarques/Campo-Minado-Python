import servidorControle
import ast
import subprocess
import socket
import threading
from datetime import datetime

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000            # Porta que o servidor escuta
HOST = ''              # Endereco IP do Servidor

    #####################################################################################################
    
""" Forma Orientado a objeto """

def server_thread_oo():
    #Abrindo uma porta UDP
    orig = (HOST, PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)
    
    while True:
        #recebi dados
        data, address = sock.recvfrom(MAX_BYTES) # Recebi dados do socket

        #Criação de thread orientada a objeto
        tratador = ThreadTratador(sock, data, address)
        tratador.start()


class ThreadTratador(threading.Thread):

    def __init__(self, sock, data, address):
        threading.Thread.__init__(self)
        self.sock = sock
        self.data = data
        self.address = address

    def run(self):
        self.__tratar_conexao(self.sock, self.data, self.address)

    def __tratar_conexao(self, sock, data, address):

        data = data.decode(ENCODE)               # Convertendo dados de BASE64 para UTF-8
        data = str(data)
        data = ast.literal_eval(data)
        
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

        #Envia resposta
        #text = "Quantidade de bytes enviados: " + str(len(data))
        #data = text.encode(ENCODE)
        #sock.sendto(data, address)
#if __name__ == "__main__":
server_thread_oo()