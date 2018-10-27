class CampoMinado:

    def __init__(self, fieldSize):
        self.cleanField = [['-' for i in range(fieldSize)] for i in range(fieldSize)]
        self.dict = {'line': 0, 'column': 0, 'played': 0}


