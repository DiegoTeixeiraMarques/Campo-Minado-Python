import servidorControle
import socket
import ast
import subprocess
from xmlrpc.server import SimpleXMLRPCServer


def played(data, mineField):

    if (data['played'] == 0):
        sizeField = data['line']
        numberBomb = data['column']
        cm = servidorControle.CampoMinado(sizeField, numberBomb, 0)
        print(cm.dict.keys())
        print(cm.dict.values())
        cm.showMineField()
    else:
        cm = servidorControle.CampoMinado(data['sizeField'], data['numberBomb'], mineField)
        cm.mining()
        cm.played(data['line'], data['column'])

    answer = str(cm.dict)
    mineField = 
    return answer, mineField

def server():
    serverRPC = SimpleXMLRPCServer(('localhost', 7002))
    serverRPC.register_function(played)
    print("Starting server. Press CTRL+C to end...")
    serverRPC.serve_forever()

server()
