import json
from django.db import models
from datetime import datetime

class Produto:
    def __init__(self, cliente, produto,valor,entregue):
        self.pedido['cliente'] = cliente
        self.pedido['produto'] = produto
        self.pedido['entregue'] = entregue
        self.pedido['timestamp'] =  datetime.today()

class PedidosModel(Produto):
    caminho = 'pedidos.json'
    nextId = -1

    def getNextId(self):
        if self.nextId == -1:
            with open(self.getCaminhoArquivo(), 'r') as f:
                array = json.load(f)
                self.nextId = array['nextId']
        return self.nextId
    
    def getCaminhoArquivo(self):
        return self.caminho

    def lerTodosPedidos(self):
        with open(self.getCaminhoArquivo(), 'r') as f:
            array = json.load(f)
        return array["pedidos"]

    def localizarPedido(self,id):
        pedidos = self.lerTodosPedidos()
        for a in range(len(pedidos)):
            try:
                if pedidos[a]["id"] == id:
                    return pedidos[a]
            except TypeError:
                pass
        return False
    
    def adicionarPedido(self,dado):
        pedidos = self.lerTodosPedidos()
        ultimoId = self.getNextId() + 1
        self.nextId = ultimoId
        dado['id'] = ultimoId
        pedidos.append(dado)
        objetoJson = json.dumps({'nextId' : ultimoId,'pedidos':pedidos},indent=0)
        with open(self.getCaminhoArquivo(), "w") as arquivAtualizado:
            arquivAtualizado.write(objetoJson)
        

    def atualizarPedido(self,id,dados): # partindo do pressuposto de que o ID existe
        pedidos = self.lerTodosPedidos()
        idEncontrado = False
        for a in range(len(pedidos)):
            try:
                if pedidos[a]["id"] == id:
                    pedidos[a]['cliente'] = dados['cliente']
                    pedidos[a]['produto'] = dados['produto']
                    pedidos[a]['valor'] = dados['valor']
                    pedidos[a]['entregue'] = dados['entregue']
                    pedidos[a]['timestamp'] = dados['timestamp']
                    idEncontrado = True
                    # O ID permanece, ñ será atualizado
            except TypeError:
                pass

        if idEncontrado == True:
            objetoJson = json.dumps({'nextId' : self.getNextId(),'pedidos':pedidos},indent=0)
            with open(self.getCaminhoArquivo(), "w") as arquivAtualizado:
                arquivAtualizado.write(objetoJson)
            return True
        return False

    def eliminarPedido(self,id): # partindo do pressuposto de que o ID existe
        pedidos = self.lerTodosPedidos()
        idEncontrado = False
        for a in range(len(pedidos)):
            try:
                if pedidos[a]["id"] == id:
                    pedidos[a]["id"] = -124324
                    pedidos[a]['cliente'] = ''
                    pedidos[a]['produto'] = ''
                    pedidos[a]['valor'] = 0
                    pedidos[a]['entregue'] = False
                    pedidos[a]['timestamp'] = ''
                    idEncontrado = True
                    # O ID é um número negativo para que ñ possa ser pesquisado
                    # os dados estão zerados para reduzir a quantidade de byte de pedidos.json
            except TypeError:
                pass

        if idEncontrado == True:
            objetoJson = json.dumps({'nextId' : self.getNextId(),'pedidos':pedidos},indent=0)
            with open(self.getCaminhoArquivo(), "w") as arquivAtualizado:
                arquivAtualizado.write(objetoJson)
            return True
        return False