import clienteModelo

class CampoMinado(clienteModelo.CampoMinado):                                           # Herança                                       
    
    def __init__(self, fieldSize):                                                      # Recebe o tamanho do campo solicitado pelo jogador
        super().__init__(fieldSize)                                                     # Herda da Classe CampoMinado o campo e o dicionario

        # Atributos de Herança '''    
            # cleanField : matriz
            # dict : dicionario

    def showCleanField(self):

        """ Mostra o Campo Minado em tela """

        self.close = '--' * len(self.cleanField) * 2                                    # Atribui " -- " * tamanho do campo * 2 a variavel 'close' 
        print('\n', '', self.close)                                                     # Apresenta a linha superior do campo
        for line in self.cleanField:                                                    
            print(end=' | ')                                                            # Acrescenta uma barra após cada área do campo
            for column in line:
                print(column, end=' | ')                                                # Acrescenta uma barra após cada área do campo
                #self.close = '--' * len(line) * 2
            print('\n', '', self.close)                                                 # Acrescenta uma lina tracejada após cada linha do campo

    def updateDict(self, answer):

        """ Atualiza o campo após resposta do servidor """

        x = -1
        sizeField = range(len(self.cleanField))
        for l in sizeField:                                                             # Percorre todo o campo
            y = 0
            x = x + 1
            for c in sizeField:
                self.cleanField[x][y] = answer[(x, y)]                                  # Atribui os valores do dicionario recebido como resposta do servidor a cada área do Campo Minado do lado Cliente        
                y = y + 1

    def translateReturn(self, answer):

        """ Traduz a resposta do servidor e organiza as informações para mostrar em tela """

        if(answer['altered'] == True):                                                  # Verifica se o campo sofreu alguma modificação (senão significa que a jogada não foi válida)
            self.updateDict(answer)                                                     # Atualiza o Campo Minado do Jogador
            self.showCleanField()                                                       # Mostra o campo em tela
            self.dict['played'] = self.dict['played'] + 1                               # Incrementa +1 no número de jogadas
            print(answer['msg'])                                                        # Mostra a mensagem em tela para orientar do Jogador
            print('Falta decobrir', answer['freeAreas'], 'áreas')                       # Mostra a quantidade de áreas que faltam ser decobertas

        else:                                                                           # Caso o campo não tenha sofrido alterações após a jogada
            self.showCleanField()                                                       # Mostra o campo em tela
            print(answer['msg'])                                                        # Informa o ocorrido
            print('Falta decobrir', answer['freeAreas'], 'áreas')                       # Mostra a quantidade de áreas que faltam ser decobertas

        if(answer['freeAreas'] == 0):                                                   # Verifica se o jogador ganhou o jogo baseado na quantidade de areas que faltam descobrir
            print('Parabéns você ganhou!')                                              # Apresenta mensagem em tela informando a vitória

