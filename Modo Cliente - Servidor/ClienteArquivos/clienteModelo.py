class CampoMinado:

    def __init__(self, fieldSize):                                                                      # Recebe o tamanho do Campo a ser criado
        self.cleanField = [['-' for i in range(fieldSize)] for i in range(fieldSize)]                   # Cria uma matriz com o tamanho solicitado contendo  " - " em cada área
        self.dict = {'line': 0, 'column': 0, 'played': 0, 'id': 0}                                      # Cria um dicionário padrão que será enviado como solicitação ao servidor


