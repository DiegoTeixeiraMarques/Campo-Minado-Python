import persistencia
import random
from string import ascii_lowercase
import subprocess

class Campo:

    def __init__(self, nColuna, nLinha, nBombas):
        self.nLinha = nLinha
        self.nBombas = nBombas
        self.campoLimpo = [['-' for i in range(nColuna)] for i in range(nLinha)]
        self.campoMinado = [[0 for i in range(nColuna)] for i in range(nLinha)]
        self.nJogadas = nColuna * nLinha - nBombas
        
        self.areaLivre = self.contaAreaslivres(self.campoLimpo)

        #gera as bombas randomicamente
    def gerarBombas(self, campo, nBombas, nLinha, nColuna):
        nBombas = nBombas
        campoMinado = campo
        while nBombas > 0:
            x = random.randint(0, nLinha - 1)
            y = random.randint(0, nColuna - 1) 
            for i in campo:
                if(campo[x][y] == 9):
                    continue
                else:
                    campo[x][y] = 9
                    nBombas = nBombas - 1
        return campoMinado

    def jogada(self, campoLimpo, campoMinado, nJogadas, linha, coluna):
        if(linha > (len(campoLimpo) - 1) or coluna > (len(campoLimpo) - 1)):
            subprocess.call('color e', shell=True)
            print('Jogada inválida, coordenadas fora do campo de jogo!', '\n')
            return campoLimpo, 0
        elif(type(campoLimpo[linha][coluna]) == str):     
            if(campoMinado[linha][coluna] == 9):
                subprocess.call('color c', shell=True)
                print('BOMBA, GAME OVER!', '\n')
                return campoLimpo, 2     
            else:
                subprocess.call('color a', shell=True)
                vizinhos = self.pegaVizinhos(campoLimpo, campoMinado, linha, coluna)
                campoLimpo = self.contaBombas(vizinhos, campoMinado, campoLimpo)
                return campoLimpo, 1
        else:
            subprocess.call('color e', shell=True)
            print('Jogada inválida, área já descoberta!', '\n')
            return campoLimpo, 0

    def pegaVizinhos(self, campoLimpo, campoMinado, linha, coluna):
        self.vizinhos = []
        #self.cont = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    self.vizinhos.append((linha + i, coluna + j))
                    continue
                #elif -1 < (self.linha + i) < len(campoMinado) and -1 < (self.coluna + j) < len(campoMinado) and campoMinado[self.linha + i][self.coluna + j] == 9:
                    #erro na chamada recursiva, computador não suporta a qtd de chamadas
                    #self.vizinhoL = self.linha + i
                    #self.vizinhoC = self.coluna + j
                    #self.bombasVizinhas(campoMinado, self.vizinhoL, self.vizinhoC)
                    #self.cont += 1
                elif -1 < (linha + i) < len(campoMinado) and -1 < (coluna + j) < len(campoMinado) and campoMinado[linha + i][coluna + j] != 9:
                    #self.pegaVizinhos(campoLimpo, campoMinado, self.linha + i, self.coluna + j)
                    self.vizinhos.append((linha + i, coluna + j))
                    #print(self.vizinhos)                     
        #self.cont
        #self.campoLimpo[self.linha][self.coluna] = self.cont                            
        return self.vizinhos


    def contaBombas(self, vizinhos, campoMinado, campoLimpo):
        for x in self.vizinhos:
            self.linha = x[0]
            self.coluna = x[1]
            #self.vizinhos = self.pegaVizinhos(campoLimpo, campoMinado, self.x, self.y)
            #print(self.x, self.y)
            self.cont = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    elif -1 < (self.linha + i) < len(campoMinado) and -1 < (self.coluna + j) < len(campoMinado) and campoMinado[self.linha + i][self.coluna + j] == 9:
                        self.cont += 1
            campoLimpo[self.linha][self.coluna] = self.cont                   
            #self.campoLimpo[self.linha][self.coluna] = self.cont
        return campoLimpo          
    
    def mostrarCampo(self, campoAtual):
                print('\n')
                for linha in campoAtual:
                    print(end=' | ')
                    for coluna in linha:
                        print(coluna, end=' | ')
                        self.fim = '--' * len(linha) * 2
                    print('\n', self.fim)
                print('\n')

    def contaAreaslivres(self, campoLimpo):
        self.cont = 0
        tam = len(campoLimpo)
        for linha in range(0, tam):
            for coluna in range(0, tam):
                if (type(campoLimpo[linha][coluna]) == str):
                    self.cont = self.cont + 1
        return self.cont

        #mostra o campo com os índices
    def mostrarCampo2(self, campoAtual):
        #converte os valores da matriz em string
        tamCampo = len(campoAtual)
        for linha in range(0, tamCampo):
            for coluna in range(0, tamCampo):
                if (type(campoAtual[linha][coluna]) == int):
                    campoAtual[linha][coluna] = str(campoAtual[linha][coluna])
        #mostra a matriz com os indices
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


    
