import socket
from datetime import datetime
import clienteControle
import ast
import subprocess

#Variaveis globais
ENCODE = "UTF-8"     # Formato para envio e recebimento
HOST = 'localhost'   # Endereco IP do Servidor
PORT = 5000          # Porta que o Servidor esta
MAX_BYTES = 65535    # Quantidade de Bytes a serem ser recebidos

##########################################################################################################################################################################

def client():

    """ Inicializa a conexão e a instância do jogo """ 

    #Start do Jogo
    sizeField = int(input("Informe o tamanho do campo:"))       # Primeira solicitacao 'Tamanho do Campo de Jogo'
    numberBobm = int(input("Informe o numero de bombas:"))      # Segunda solicitacao 'Quantidade de Bombas no Campo'
    cm = clienteControle.CampoMinado(sizeField)                 # Instancia o CampoMinado a partir do arquivo clienteControle
    cm.dict['line'] = sizeField                                 # Atribui o tamanho do campo ao dicionario da classe do campo criado
    cm.dict['column'] = numberBobm                              # Atribui a quantidade de bombas ao dicionario da classe do campo criado
    
    #Preparando para envio
    request = cm.dict                                           # Atribui o dicionario que sera enviado a uma variavel
    request = str(request)                                      # Transforma o dicionario em String
    request = request.encode(ENCODE)				            # Codifica para BASE64 os dados de entrada	
    
    #Enviando os dados
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)     # Inicializar um socket UDP
    dest = (HOST, PORT)                                         # Define IP de origem e Porta de destino a partir das variaveis globais
    sock.sendto(request, dest)                                  # Envia os dados para o destino
                                                                # Dados enviados = {'line': 0, 'column': 0, 'played': 0, 'id': 0}

    #Resposta de envio ao servidor
    answer, address = sock.recvfrom(MAX_BYTES)                  # Recebendo dados
    answer = answer.decode(ENCODE)                              # Convertendo dados de BASE64 para UTF-8
    answer = ast.literal_eval(answer)                           # Converte para dictionary
                                                                # Dados recebidos: { (0,0): 0 , (0,1):0 , (0,2):0 , ... , (2,2):0 , ... , 'msg': x , 'freeAreas': x , 'altered': True , controlPlay: x }

    #Tratamento da resposta
    cm.translateReturn(answer)                                  # Inicializa metodo para traducao e apresentacao da resposta em tela

    #Fechando Socket
    sock.close()                                                # Fecha conexão
    
    #Prende o jogo num laço
    while True:
        
        #Jogada
        print('As linhas e colunas variam de 0 à', len(cm.cleanField)-1, '\n')      # Informa qual intervalo pode ser solicitada uma jogada
        line = int(input("Informe a linha:"))                               # Solicita Linha para processar Jogada
        column = int(input("Informe a coluna:"))                            # Solicita Coluna para processar Jogada
        cm.dict['line'] = line                                              # Atribui a linha ao dicionario que sera enviado ao servidor
        cm.dict['column'] = column                                          # Atribui a coluna ao dicionario que sera enviado ao servidor
        #cm.dict['played'] += cm.dict['played']

        #Preparando para envio
        request = cm.dict                                       # Atribui o dicionario que sera enviado a uma variavel
        request = str(request)                                  # Transforma o dicionario em String
        request = request.encode(ENCODE)				        # Codifica para BASE64 os dados de entrada	
        
        #Enviando os dados
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)     # Inicializar um socket UDP
        dest = (HOST, PORT)                                         # Define IP de origem e Porta de destino  
        sock.sendto(request, dest)                                  # Envia os dados para o destino

        subprocess.call('cls', shell=True)                          # Limpa o prompt para mostrar novas informações do jogo

        #Resposta de envio ao servidor
        answer, address = sock.recvfrom(MAX_BYTES)                  # Recebendo dados
        answer = answer.decode(ENCODE)                              # Convertendo dados de BASE64 para UTF-8
        answer = ast.literal_eval(answer)                           # Converte para dictionary
                                                                    # Dados recebidos: { (0,0): 0 , (0,1):0 , (0,2):0 , ... , (2,2):0 , ... , 'msg': x , 'freeAreas': x , 'altered': True , controlPlay: x }

        #Tratamento da resposta
        cm.translateReturn(answer)                                  # Inicializa metodo para traducao e apresentacao da resposta em tela
        
        #Fechando Socket
        sock.close()

#########################################################################################################################################################################################

if __name__ == '__main__':
    client()


    
        

