from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import PedidosModel
import json

class PedidosView(View):
    @method_decorator
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,id=0):
        pedidosModel = PedidosModel()

        if id > 0 :
            pedido = list(pedidosModel.localizarPedido(id))
            if pedido != False:
                return JsonResponse({'mensagem' : 'Sucesso', 'pedido':pedido})
            else:
                return JsonResponse({'mensagem' : 'Pedido não encontrado'})
        else:
            listaPedidos = pedidosModel.lerTodosPedidos()
            if len(listaPedidos) > 0 :
                return JsonResponse({'mensagem' : 'Sucesso', 'pedidos':pedido})
            else:
                return JsonResponse({'mensagem' : 'A lista de pedidos está vazia', 'pedidos':[]})

    def post(self,request):
        dados = json.load(request.body)
        pedidosModel = PedidosModel()
        novoPedido = {
            'cliente':dados['cliente'],
            'produto':dados['produto'],
            'valor':dados['valor'],
            'entregue':dados['entregue'],
            'timestamp':dados['timestamp']
        }
        pedidosModel.adicionarPedido(novoPedido)
        return JsonResponse({'mensagem':'Novo pedido foi cadastrado com sucessso', 'pedido':novoPedido})       

    def put(self,request,id=0):
        dados = json.load(request.body)
        pedidosModel = PedidosModel()
        pedido = {
            'cliente':dados['cliente'],
            'produto':dados['produto'],
            'valor':dados['valor'],
            'entregue':dados['entregue'],
            'timestamp':dados['timestamp']
        }    
        return JsonResponse({'mensagem': 'Pedido foi atualizado com sucessso' if pedidosModel.atualizarPedido(id,pedido) == True else 'Pedido não encotrado' })

    def delete(self,request,id=0):
        pedidosModel = PedidosModel()
        pedidosModel.atualizarPedido(id)
        return JsonResponse({'mensagem': 'Pedido foi eliminado com sucessso' if pedidosModel.eliminarPedido(id) == True else 'Pedido não encotrado' })