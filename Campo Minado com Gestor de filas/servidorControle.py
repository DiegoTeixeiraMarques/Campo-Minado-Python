import servidorModelo


class CampoMinado(servidorModelo.Campo):                                                                                   # Herança
    def __init__(self, fieldSize, numberBomb):                                                                             # Recebe o tamanho do campo e a quantidade de bombas
        super().__init__(fieldSize, numberBomb)                                                                            # Faz uma chamada a Super Classe
        
        #Atributos de Herança
            #numberBomb: inteiro
            #cleanField: matriz
            #mineField: matriz
            #dict: dicionario
        
    def played(self, line, column):

        """ Faz o tratamento da jogada ao receber os parâmetros linha e coluna """

        if(line > (len(self.cleanField) - 1) or column > (len(self.cleanField) - 1) or line < 0 or column < 0):            # Verifica se as coordenadas estão dentro do campo de jogo
            self.dict['controlPlay'] = 1                                                                                   # Caso verdadeiro atribui valor 1 ao 'controlPlay' do dict
            self.dict['msg'] = 'Jogada inválida, coordenadas fora do campo de jogo!'
            self.dict['altered'] = False                                                                                   # Atribui False a 'altered', pois não houve modificação no campo
        
        elif(self.mineField[line][column] == 9):                                                                           # Verifica se a jogada foi em uma área com Bomba
            self.dict['controlPlay'] = 2                                                                                   # Caso verdadeiro atribui valor 2 ao 'controlPlay' do dict
            self.dict['msg'] = 'Bomba, Game Over!'
            self.dict['altered'] = True  
            self.updateDict(self.mineField)                                                                                # Atualiza o dicionário com as áreas do campo minado, para jogador saber onde estavam as bombas

        elif(type(self.cleanField[line][column]) == str):                                                                  # Verifica se a jogada foi em uma campo sem bomba e sem está decoberto  
            neighbors = self.takeNeighbors(line, column)                                                                   # Caso verdadeiro, pega os vizinhos da área solicitada
            self.bombCount(neighbors)                                                                                      # Conta as bombas que contém na Vizinhança
            self.dict['controlPlay'] = 3                                                                                   # 'controlPlay' recebe 3, jogada bem sucedida
            self.dict['msg'] = 'Jogada bem sucedida!'
            self.dict['played'] += 1
            self.dict['altered'] = True                                                                                    # 'played' recebe +1, informando a quantidade de jogadas até o momento
            self.dict['freeAreas'] = self.countFreeArea()                                                                  # Conta as áreas livre que restam no campo para enviar ao jogador
            self.updateDict(self.cleanField)                                                                               # Atualiza o dict que será enviado ao jogador com o campo após a jogada
        
        else:                                                                                                              # Caso a área já tenha sido descoberta
            self.dict['controlPlay'] = 4                                                                                   # 'controlPlay' recebe 4
            self.dict['msg'] = 'Jogada inválida, área já descoberta'
            self.dict['altered'] = False                                                                                   # Não há alteração no campo de jogo, então, 'altered' recebe False
            

    def takeNeighbors(self, line, column):

        """ Pega as coordenadas dos vizinhos """

        self.neighbors = []                                                                                                                                         # Cria um vetor vazio para alocar os vizinhos  
        for i in range(-1, 2):                                                                                                                                      # Percorre as coordenadas x e y próximas
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    self.neighbors.append((line + i, column + j))
                    continue                                                                                                                                        
                elif -1 < (line + i) < len(self.mineField) and -1 < (column + j) < len(self.mineField) and self.mineField[line + i][column + j] != 9:               # Percorre as coordenadas x e y próximas
                    self.neighbors.append((line + i, column + j))                                                                                                   # Adiciona os vizinhos no vetor
        return self.neighbors                                                                                                                                       # Retorna o vetor com os vizinhos


    def bombCount(self, neighbors):                                                                                                                                 # Recebe o vetor de vizinhos

        """ Conta as bombas que tem ao redor da área """

        for x in self.neighbors:                                                                                                                                                # Percorre vetor de vizinhos recebido por parâmetro
            self.line = x[0]
            self.column = x[1]
            self.count = 0                                                                                                                                                      # Inicializa um contador de bombas
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    elif -1 < (self.line + i) < len(self.mineField) and -1 < (self.column + j) < len(self.mineField) and self.mineField[self.line + i][self.column + j] == 9:   # Verifica se a área contém 9, que representa uma bomba
                        self.count += 1                                                                                                                                         # Caso verdadeiro, atribui mais um na contagem de bombas da área
            self.cleanField[self.line][self.column] = self.count                                                                                                                # Atribui a contagem na área

    def countFreeArea(self):

        """ Conta área livres restantes no Campo de Jogo """

        self.count = 0                                                                # Inicializa contador
        sizeField = len(self.cleanField)
        for line in range(0, sizeField):                                              # Percorre o campo limpo
            for column in range(0, sizeField):                                        # Verifica se tem uma String (" - ")
                if (type(self.cleanField[line][column]) == str):
                    self.count = self.count + 1                                       # Se verdadeiro, atribui mais uma área livre
        return self.count - self.numberBomb                                           # A quantidade de áreas livres encontradas são subtraídas da quantidade de bombas, para o jogador saber o que falta descobrir para ganhar o jogo

    
    def updateDict(self, field):

        """ Atualiza o dicionário após uma jogada válida """

        x = -1
        sizeField = range(len(field))                                                # Encontra o tamanho do campo de jogo para percorrer o dict na quantidade certa
        for l in sizeField:                                                          
            y = 0
            x = x + 1
            for c in sizeField:
                self.dict[(x, y)] = field[x][y]                                      # Atribui os valores do novo campo ao dict que será enviado ao jogador             
                y = y + 1        

    def showMineField(self):

        """ Mostra o Campo Minado em tela """

        print('\n')
        self.close = '--' * len(self.mineField) * 2
        print('\n', '', self.close)
        for line in self.mineField:
            print(end=' | ')
            for column in line:
                print(column, end=' | ')
            print('\n', '', self.close)
                    

    def showCleanField(self):

        """ Mostra o Campo Limpo em tela """

        print('\n')
        self.close = '--' * len(self.mineField) * 2
        print('\n', '', self.close)
        for line in self.cleanField:
            print(end=' | ')
            for column in line:
                print(column, end=' | ')
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





        
        