import servidorModelo


class CampoMinado(servidorModelo.Campo):
    def __init__(self, fieldSize, numberBomb, mineField):
        super().__init__(fieldSize, numberBomb)
        '''  Atributos de Herança '''

        #numberBomb: inteiro
        #cleanField: matriz
        #mineField: matriz
        #dict: dicionario
        #dict: dictMineField
    
    def mining(self, field):
        x = -1
        sizeField = range(len(field))
        for l in sizeField:
            y = 0
            x = x + 1
            for c in sizeField:
                self.dictMineField[(x, y)] = field[x][y]            
                y = y + 1

    def played(self, line, column):
        if(line > (len(self.cleanField) - 1) or column > (len(self.cleanField) - 1) or line < 0 or column < 0):
            self.dict['controlPlay'] = 1
            self.dict['msg'] = 'Jogada inválida, coordenadas fora do campo de jogo!'
            self.dict['altered'] = False
        
        elif(self.mineField[line][column] == 9):
            self.dict['controlPlay'] = 2
            self.dict['msg'] = 'Bomba, Game Over!'
            self.mineField = self.updateDict(self.mineField)

        elif(type(self.cleanField[line][column]) == str):  
            neighbors = self.takeNeighbors(line, column)
            self.bombCount(neighbors)
            self.dict['controlPlay'] = 3
            self.dict['msg'] = 'Jogada bem sucedida!'
            self.dict['played'] += 1
            self.dict['freeAreas'] = self.countFreeArea()
            self.cleanField = self.updateDict(self.cleanField)
        
        else:
            self.dict['controlPlay'] = 4
            self.dict['msg'] = 'Jogada inválida, área já descoberta'
            self.dict['altered'] = False
            

    def takeNeighbors(self, line, column):
        self.neighbors = []
        #self.cont = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    
                    self.neighbors.append((line + i, column + j))
                    continue
                #elif -1 < (self.linha + i) < len(campoMinado) and -1 < (self.coluna + j) < len(campoMinado) and campoMinado[self.linha + i][self.coluna + j] == 9:
                    #erro na chamada recursiva, computador não suporta a qtd de chamadas
                    #self.vizinhoL = self.linha + i
                    #self.vizinhoC = self.coluna + j
                    #self.bombasVizinhas(campoMinado, self.vizinhoL, self.vizinhoC)
                    #self.cont += 1
                elif -1 < (line + i) < len(self.mineField) and -1 < (column + j) < len(self.mineField) and self.mineField[line + i][column + j] != 9:
                    #self.pegaVizinhos(campoLimpo, campoMinado, self.linha + i, self.coluna + j)
                    self.neighbors.append((line + i, column + j))
                    #print(self.vizinhos)                     
        #self.cont
        #self.campoLimpo[self.linha][self.coluna] = self.cont                            
        return self.neighbors


    def bombCount(self, neighbors):
        for x in self.neighbors:
            self.line = x[0]
            self.column = x[1]
            #self.vizinhos = self.pegaVizinhos(campoLimpo, campoMinado, self.x, self.y)
            #print(self.x, self.y)
            self.count = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    elif -1 < (self.line + i) < len(self.mineField) and -1 < (self.column + j) < len(self.mineField) and self.mineField[self.line + i][self.column + j] == 9:
                        self.count += 1
            self.cleanField[self.line][self.column] = self.count

    def countFreeArea(self):
        self.count = 0
        sizeField = len(self.cleanField)
        for line in range(0, sizeField):
            for column in range(0, sizeField):
                if (type(self.cleanField[line][column]) == str):
                    self.count = self.count + 1
        print(self.count, self.numberBomb)
        print('numero de areas livre:', self.count - self.numberBomb)
        return self.count - self.numberBomb

    
    def updateDict(self, field):
        x = -1
        sizeField = range(len(field))
        for l in sizeField:
            y = 0
            x = x + 1
            for c in sizeField:
                self.dict[(x, y)] = field[x][y]               
                y = y + 1
        self.dict['altered'] = True
        if (self.dict['freeAreas'] <= 0):
            self.dict['msg'] = 'Parabéns, você ganhou!'
        return field
        

    def showMineField(self):
        print('\n')
        self.close = '--' * len(self.mineField) * 2
        print('\n', '', self.close)
        for line in self.mineField:
            print(end=' | ')
            for column in line:
                print(column, end=' | ')
                #self.close = '--' * len(line) * 2
            print('\n', '', self.close)
                    

    def showCleanField(self):
        print('\n')
        self.close = '--' * len(self.mineField) * 2
        print('\n', '', self.close)
        for line in self.cleanField:
            print(end=' | ')
            for column in line:
                print(column, end=' | ')
                #self.close = '--' * len(line) * 2
            print('\n', '', self.close)
        

'''
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

'''





        
        