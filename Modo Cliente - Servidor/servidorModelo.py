import random

class Campo:
    
    """ Classe modelo para o jogo de Campo Minado Cliente/ Servidor """

    def __init__(self, fieldSize, numberBomb):
        self.numberBomb = numberBomb
        self.cleanField = [['-' for i in range(fieldSize)] for i in range(fieldSize)]
        self.mineField = self.generateBomb([[0 for i in range(fieldSize)] for i in range(fieldSize)], self.numberBomb)
        self.dict = self.createDictionary({}, fieldSize)
    

    def generateBomb(self, cleanField, numberBomb):
        
        """ Recebe um campo limpo e a quantidade de bombas e devolve um campo minado de forma randomica """

        numberBomb = numberBomb
        fieldSize = len(cleanField)
        mineField = cleanField
        while numberBomb > 0:
            x = random.randint(0, fieldSize - 1)
            y = random.randint(0, fieldSize - 1) 
            for i in mineField:
                if(mineField[x][y] == 9):
                    continue
                else:
                    mineField[x][y] = 9
                    numberBomb = numberBomb - 1
        return mineField


    def createDictionary(self, dict, fieldSize):

        """ Recebe um dicionario vazio e o tamanho do campo e devolve um dicionario com tupla(x, y) sendo a chave para cada posicao no campo """

        for x in range(fieldSize):
            for y in range(fieldSize):
                dict[(x, y)] = '-'

        dict['msg'] = 'Inicio'
        dict['freeAreas'] = fieldSize * fieldSize
        dict['played'] = 0
        dict['altered'] = True
        dict['contolPlay'] = 0
        return dict
