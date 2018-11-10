import socket
import clienteControle
import ast
import subprocess
import zmq
import sys
import gestor_filas

#Variaveis globais
ENCODE = "UTF-8"     # Formato para envio e recebimento
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
    context = zmq.Context()                                     # Abre conexão com gestor de filas
    print("Conectando com o servidor...")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:%s" % PORT)                # Informa IP e PORTA para conexão

    socket.send(request)                                        # Envia solicitação de jogada ao servidor de filas
    
    #Pega a resposta
    answer = socket.recv()


    #Resposta de envio ao servidor
    answer = answer.decode(ENCODE)                              # Convertendo dados de BASE64 para UTF-8
    answer = ast.literal_eval(answer)                           # Converte para dictionary
                                                                # Dados recebidos: { (0,0): 0 , (0,1):0 , (0,2):0 , ... , (2,2):0 , ... , 'msg': x , 'freeAreas': x , 'altered': True , controlPlay: x }

    #Tratamento da resposta
    cm.dict['id'] = answer['id']                                # Atribui o identificador do cliente gerado no servidor
    print(cm.dict.values())
    cm.translateReturn(answer)                                  # Inicializa metodo para traducao e apresentacao da resposta em tela
    
    #Prende o jogo num laço
    while True:
        
        #Jogada
        print('As linhas e colunas variam de 0 à', len(cm.cleanField)-1, '\n')      # Informa qual intervalo pode ser solicitada uma jogada
        line = int(input("Informe a linha:"))                                       # Solicita Linha para processar Jogada
        column = int(input("Informe a coluna:"))                                    # Solicita Coluna para processar Jogada
        cm.dict['line'] = line                                                      # Atribui a linha ao dicionario que sera enviado ao servidor
        cm.dict['column'] = column                                                  # Atribui a coluna ao dicionario que sera enviado ao servidor

        print("Conectando com o servidor...")

        #Preparando para envio
        request = cm.dict                                       # Atribui o dicionario que será enviado a uma variavel
        request = str(request)                                  # Transforma o dicionario em String
        request = request.encode(ENCODE)				        # Codifica para BASE64 os dados de entrada	
        
        #Enviando dados
        #context = zmq.Context()                                 
        
        #socket = context.socket(zmq.REQ)
        #socket.connect("tcp://localhost:%s" % PORT)

        socket.send(request)                                    # Envia solicitação de jogada ao gestor de filas
    
        #Pega a resposta.
        answer = socket.recv()

        subprocess.call('cls', shell=True)                          # Limpa o prompt para mostrar novas informações do jogo, comando para Windows

        #Resposta de envio ao servidor
        answer = answer.decode(ENCODE)                              # Convertendo dados de BASE64 para UTF-8
        answer = ast.literal_eval(answer)                           # Converte para dictionary
                                                                    # Dados recebidos: { (0,0): 0 , (0,1):0 , (0,2):0 , ... , (2,2):0 , ... , 'msg': x , 'freeAreas': x , 'altered': True , controlPlay: x }

        #Tratamento da resposta
        cm.translateReturn(answer)                                  # Inicializa metodo para traducao e apresentacao da resposta em tela

#########################################################################################################################################################################################

if __name__ == '__main__':
    client()


    
        

