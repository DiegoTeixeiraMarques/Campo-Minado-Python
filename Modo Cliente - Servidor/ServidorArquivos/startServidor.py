import servidorControle
import socket
from datetime import datetime
import ast
import subprocess

#Variáveis globais
ENCODE = "UTF-8"
MAX_BYTES = 65535      # Determina a quantidade máxima de bytes enviados na conexão
PORT = 5000            # Porta que o Servidor esta
HOST = ''     	       # Endereco IP do Servidor



def server():

    #Abrindo um socket UDP na porta 5000
    orig = (HOST, PORT)																
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)

    #Cria uma laço para manter a conexão contínua
    while True:
        
        #Limpa prompt
        #subprocess.call('cls', shell=True)

        #Recebe os dados
        data, address = sock.recvfrom(MAX_BYTES)                                 # Recebendo dados do socket
        data = data.decode(ENCODE)                                               # Convertendo dados de BASE64 para UTF-8
        data = str(data)                                                         # Convertendo para String
        data = ast.literal_eval(data)                                            # Convertendo para dictionary
        
        #Debug ---
        print(data.keys())                                                                      #Debug em tela
        print(data.values())                                                                    #Debug em tela
        # ---
        
        if (data['played'] == 0):                                                # Verifica se é um Jogo novo
            sizeField = data['line']
            numberBomb = data['column']
            cm = servidorControle.CampoMinado(sizeField, numberBomb)             # Instancia o campo minado do Servidor
        else:                                                                    # Se não for um Jogo novo    
            cm.played(data['line'], data['column'])                              # Chama o método da Jogada passando linha e coluna

        #Debug ---
        cm.showMineField()                                                                      #Debug em tela
        #---

        #Prepara resposta
        answer = str(cm.dict)                                                   # Converte a rsposta de Dictionary para String
        answer = answer.encode(ENCODE)                                          # Codifica para BASE64 os dados 

        #Envia resposta
        sock.sendto(answer, address)                                            # Enviando reposta	

if __name__ == '__main__':
    server()