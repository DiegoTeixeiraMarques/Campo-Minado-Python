import servidorControle
import ast
import subprocess
import socket
import threading
from datetime import datetime
import zmq
import sys

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5001            # Porta que o servidor escuta
HOST = ''              # Endereco IP do Servidor
players = []           # Cria uma lista para alocar os diversos jogadores online

###############################################################
                                                                # 
#Abre conexão com gestor de filas                               #
context = zmq.Context()                                         #
socket = context.socket(zmq.REP)                                #
socket.connect("tcp://localhost:%s" % PORT)                     #
                                                                #
###############################################################

""" Forma Orientado a objeto """

def server_thread_oo():

    while True:

        #Recebe os dados
        data = socket.recv()                                    # Recebendo dados do socket

        #Criação de thread orientada a objeto
        tratador = ThreadTratador(data)                         # Instancia objeto tratador da classe ThreadTratador
        tratador.tratar_conexao(data)                           # Inicializa thread
                                                                


class ThreadTratador(threading.Thread):

    def __init__(self, data):                                   # Recebe as informações de conexão
        threading.Thread.__init__(self)
        self.data = data



    def tratar_conexao(self, data):

        """ Trata as infomrações recebidas dos jogadores para devolver uma resposta válida """

        data = data.decode(ENCODE)                                             # Convertendo dados de BASE64 para UTF-8
        data = str(data)
        data = ast.literal_eval(data)
        
        if (data['played'] == 0):                                              # Verifica se é jogador novo
            
            sizeField = data['line']                                           # Atribui o tamanho do campo solicitado pelo jogador
            numberBomb = data['column']
            cm = servidorControle.CampoMinado(sizeField, numberBomb)           # Atribui a qauntidade de bombas no campo solicitado pelo jogador
            players.append(cm)                                                 # Adiciona a lista de jogadores
            cm.dict = self.identificator(cm.dict)                              # Atribui um ID único ao jogador, baseado no indice do vetor em que o objeto ficará
            print(cm.dict.keys())
            print(cm.dict.values())
            cm.showCleanField()

        else:
            cm = players[data['id']]                                           # Caso não seja um novo jogador, busca as informações do jogo nas lista que armazena os jogadores online
            cm.played(data['line'], data['column'])                            # Executa a jogada solicitada 

        cm.showMineField()                                                     # Debug com print, mostra o campo minado no servidor
        
        #Envia resposta 
        answer = str(cm.dict)                                                  # Atribui o dicionário que será enviado como resposta a uma variável
        answer = answer.encode(ENCODE)                                         # Codifica para BASE64 os dados 
        socket.send(answer)                                                    # Envia os dados	

    def identificator(self, dict):

        """ Cria um ID para um jogador novo baseado no índice em que suas informações ficarão alocadas dentro da lista de players """
        
        dict['id'] = len(players) - 1                                          # atribui ID ao jogador de acordo com seu índice na lista de players
        return dict

if __name__ == "__main__":
    server_thread_oo()