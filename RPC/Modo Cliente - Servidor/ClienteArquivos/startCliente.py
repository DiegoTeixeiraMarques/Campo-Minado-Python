import socket
from datetime import datetime
import clienteControle
import ast
import subprocess
import xmlrpc.client



def client():
    sizeField = int(input("Informe o tamanho do campo:"))
    numberBomb = int(input("Informe o numero de bombas:"))
    
    cm = clienteControle.CampoMinado(sizeField)
    cm.dict['sizeField'] = sizeField
    cm.dict['numberBomb'] = numberBomb
    
    client = xmlrpc.client.ServerProxy('http://localhost:7002')
    answer = client.played(cm.dict, cm.mineField)
    answer = ast.literal_eval(answer)
    
    if(answer['altered'] == True):
        cm.updateDict(answer)
        cm.showCleanField()
        answer['msg']
        print('Falta decobrir', answer['freeAreas'], 'áreas')
    
    while True:
        cm.dict['played'] = cm.dict['played'] + 1
        line = int(input("Informe a linha:"))
        column = int(input("Informe a coluna:"))

        cm.dict['line'] = line
        cm.dict['column'] = column
        cm.dict['played'] += cm.dict['played']

        client = xmlrpc.client.ServerProxy('http://localhost:7002')
        answer = client.played(cm.dict, cm.mineField)
        answer = ast.literal_eval(answer)
    
        subprocess.call('cls', shell=True)
        
        if(answer['altered'] == True):
            cm.updateDict(answer)
            cm.showCleanField()
            print(answer['msg'])
            print('Falta decobrir', answer['freeAreas'], 'áreas')
        else:
            cm.showCleanField()
            print(answer['msg'])
            print('Falta decobrir', answer['freeAreas'], 'áreas')

        if(answer['controlPlay'] == 2):
            print('/n')
            print('/n')
            print('/n')
            A = int(input('Digite 1 se deseja jogar novamente'))

client()


    
        

