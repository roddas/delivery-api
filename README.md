# Delivery REST API

Este é um desafio proposto pela CBLAB para adesão ao estágio de programador back-end.Para mais informações por favor queiram entrar em contato. Espero que tenham gostado.

## Especificações técnicas

Esta API foi desenvolvida em Python 3.8 , utilizando o framework Flask (a escolha do programador pela simplicidade, e pelo fato de que o enunciado somente especificou a linguagem ) sem o uso de geradores de APIs automáticos. 

## Pré-requisitos

* Ter o [Docker](https://www.docker.com/) instalado .

## Instalação e execução

```
git clone https://github.com/roddas/delivery-api

cd delivery-api

sudo docker build -t  delivery .

sudo docker run delivery

```

# Rotas

* **GET** /pedidos
* **GET** /pedidos/<int:id>
* **POST** /pedidos
* **DELETE** /pedidos/<int:id>
* **PUT** /pedidos/<int:id>