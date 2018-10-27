import socket
from datetime import datetime
import clienteControle
import ast
import subprocess

ENCODE = "UTF-8"
HOST = '127.0.0.1'   # Endereco IP do Servidor
PORT = 5000          # Porta que o Servidor esta
MAX_BYTES = 65535    # Quantidade de Bytes a serem ser recebidos


def client():
    sizeField = int(input("Informe o tamanho do campo:"))
    numberBobm = int(input("Informe o numero de bombas:"))
    cm = clienteControle.CampoMinado(sizeField)

    cm.dict['line'] = sizeField
    cm.dict['column'] = numberBobm
    
    request = cm.dict
    request = str(request)
    request = request.encode(ENCODE)				    # Codifica para BASE64 os dados de entrada	
    #Enviando de dados
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Inicializar um socket UDP
    dest = (HOST, PORT)                                     # Define IP de origem e Porta de destino  
    sock.sendto(request, dest)                                 # Envia os dados para o destino

    #Resposta de envio ao servidor
    answer, address = sock.recvfrom(MAX_BYTES)    # Recebendo dados

    answer = answer.decode(ENCODE)                  # Convertendo dados de BASE64 para UTF-8
    answer = ast.literal_eval(answer)

    if(answer['altered'] == True):
        cm.updateDict(answer)
        cm.showCleanField()
        answer['msg']
        print('Falta decobrir', answer['freeAreas'], 'áreas')

    #Fechando Socket
    sock.close()
    
    while True:
        cm.dict['played'] = cm.dict['played'] + 1
        line = int(input("Informe a linha:"))
        column = int(input("Informe a coluna:"))

        cm.dict['line'] = line
        cm.dict['column'] = column
        cm.dict['played'] += cm.dict['played']

        request = cm.dict
        request = str(request)
        request = request.encode(ENCODE)				    # Codifica para BASE64 os dados de entrada	
        #Enviando de dados
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Inicializar um socket UDP
        dest = (HOST, PORT)                                     # Define IP de origem e Porta de destino  
        sock.sendto(request, dest)                                 # Envia os dados para o destino

        subprocess.call('cls', shell=True)

        #Resposta de envio ao servidor
        
        answer, address = sock.recvfrom(MAX_BYTES)    # Recebendo dados
        answer = answer.decode(ENCODE)                  # Convertendo dados de BASE64 para UTF-8
        answer = ast.literal_eval(answer)

        if(answer['altered'] == True):
            cm.updateDict(answer)
            cm.showCleanField()
            print(answer['msg'])
            print('Falta decobrir', answer['freeAreas'], 'áreas')
        else:
            cm.showCleanField()
            print(answer['msg'])
            print('Falta decobrir', answer['freeAreas'], 'áreas')

        if(answer['controlPlay'] == 2):
            print('/n')
            print('/n')
            print('/n')
            A = int(input('Digite 1 se deseja jogar novamente'))
        #Fechando Socket
        sock.close()
    
    client()        

client()


    
        

