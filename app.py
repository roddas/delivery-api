from operator import truediv
from flask import Flask,request
from helpers import PedidosHelper
from datetime import datetime

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = True

pedidosHelper = PedidosHelper()
 
def response(mensagem : str ,data : list):
    return {'mensagem':mensagem,'dados':data}

@app.route('/')
def root():
    return 'Olá a todos'

@app.route('/pedidos',methods=['GET'])
def listarPedidos():
    pedidos = pedidosHelper.lerTodosPedidos()
    return response('Sucesso',pedidos),200

@app.route('/pedidos/<int:idPedido>',methods=['GET'])
def listarPedidoPorId(idPedido : int):
    pedido = pedidosHelper.localizarPedido(idPedido)
    if pedido:
        return response('Sucesso',pedido),200
    else:
        return response('Pedido não encontrado',[]),404

@app.route('/pedidos/<int:idPedido>',methods=['DELETE'])
def eliminarPedido(idPedido : int):
    pedido = pedidosHelper.eliminarPedido(idPedido)
    if pedido:
        return response('Pedido eliminado com sucesso',[]),200
    else:
        return response('Pedido não encontrado',[]),404

@app.route('/pedidos/<int:idPedido>',methods=['PUT'])
def atualizarPedido(idPedido : int):
    body = request.json

    pedido = pedidosHelper.localizarPedido(idPedido)
    if pedido:
        dados = {
            "cliente": body.get('cliente'),
            "entregue": body.get('entregue'),
            "id": body.get('id'),
            "produto": body.get('produto'),
            "timestamp" : datetime.now().isoformat(timespec='seconds'),
            "valor": body.get('valor')
        } 
        pedidosHelper.atualizarPedido(idPedido,dados)
        return response('Pedido atualizado com sucesso',dados),200
    else:
        return response('Pedido não encontrado',[]),404


@app.route('/pedidos',methods=['POST'])
def adicionarPedido():
    body = request.json
    dados = {
            "cliente": body.get('cliente'),
            "entregue": body.get('entregue'),
            "id": body.get('id'),
            "produto": body.get('produto'),
            "timestamp": body.get('timestamp'),
            "valor": body.get('valor')
    }
    pedidosHelper.adicionarPedido(dados) 
    
    return response('Pedido adicionado com sucesso',dados),201


app.run(debug=True)

