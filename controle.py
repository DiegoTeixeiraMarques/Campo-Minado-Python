import persistencia
import random
from string import ascii_lowercase

class Campo:



    def __init__(self, nColuna, nLinha, nBombas):
        self.campo = [[0 for i in range(nColuna)] for i in range(nLinha)]
        self.campoMinado = self.gerarBombas(self.campo, nBombas, nLinha, nColuna)
        self.nJogadas = nColuna * nLinha - nBombas
        self.mostrarCampo(self.campoMinado)
        self.jogada(self.campoMinado, self.nJogadas)
        #self.mostrarCampo(self.campoMinado)

    def __repr__(self): 
        return f'matriz : {self.campoMinado}'

    def criar(self, nColuna, nLinha, nBombas):
        self.campo = [[' ' for i in range(nColuna)] for i in range(nLinha)]
        self.campoMinado = self.gerarBombas(self.campo, nBombas, nLinha, nColuna)
        self.nJogadas = nColuna * nLinha - nBombas
        return self.campoMinado

        #gera as bombas randomicamente
    def gerarBombas(self, campo, nBombas, nLinha, nColuna):
        nBombas = nBombas
        campoMinado = campo
        while nBombas > 0:
            x = random.randint(0, nLinha - 1)
            y = random.randint(0, nColuna - 1) 
            #print(x, y)
            for i in campo:
                if(campo[x][y] == 9):
                    continue
                else:
                    campo[x][y] = 9
                    nBombas = nBombas - 1
        return campoMinado

    def jogada(self, campoMinado, nJogadas):
        
        self.totalJogadas = self.nJogadas
        while (self.nJogadas > 0):
            print('--> Você tem', self.nJogadas,'/', self.totalJogadas, 'jogadas restantes', '\n')
            self.linha = int(input("--> Informe a linha: "))
            self.coluna = int(input("--> Informe a coluna: "))

            #persistencia.Salvar(self.linha, self.coluna, self.nJogadas, campoMinado)
            if(campoMinado[self.linha][self.coluna] == 10):
                print('BOMBA, GAME OVER!')
                self.mostrarCampo(campoMinado)
                break      
            else:
                #print('TENTE DENOVO')
                self.nJogadas = self.nJogadas - 1
                campoMinado = self.bombasVizinhas(campoMinado, self.linha, self.coluna)
                campoMinado[self.linha][self.coluna]
                self.mostrarCampo(campoMinado)
                      
    def bombasVizinhas(self, campoMinado, linha, coluna):
        #self.vizinhos = []
        for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue
                        elif -1 < (self.linha + i) < len(campoMinado) and -1 < (self.coluna + j) < len(campoMinado) and campoMinado[self.linha + i][self.coluna + j] == 9:
                            #erro na chamada recursiva, computador não suporta a qtd de chamadas
                            #self.vizinhoL = self.linha + i
                            #self.vizinhoC = self.coluna + j
                            #self.bombasVizinhas(campoMinado, self.vizinhoL, self.vizinhoC)
                            
                            self.campoMinado[self.linha][self.coluna] += 1
                                             
        return campoMinado  

    
    def mostrarCampo(self, campoAtual):
                print('================Início================', '\n')
                for linha in campoAtual:
                    print(end=' | ')
                    
                    for coluna in linha:
                        print(coluna, end=' | ')
                        self.fim = '--' * len(linha) * 2
                    print('\n', self.fim)
                print('\n', '================Fim================', '\n')

'''
        #mostra o campo com os índices
    def mostrarCampo(self, campoAtual):
        tamCampo = len(campoAtual)
        horizontal = '   ' + (4 * tamCampo * '-') + '-'
        superior = '     '

        for i in ascii_lowercase[:tamCampo]:
            superior = superior + i + '   '
        print(superior + '\n' + horizontal)

        for idx, i in enumerate(campoAtual):
            linha = '{0:2} |'.format(idx + 1)
            for j in i:
                linha = linha + ' ' + j + ' |'
            print(linha + '\n' + horizontal)
        print('')
'''

    
