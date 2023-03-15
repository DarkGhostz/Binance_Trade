from binance import client
from secret import api_Secret, api_Key
client = (api_Key, api_Secret)

#pegar informação da nossa conta
info = client.get_account()
for item in info:
    print(item)

# ver os saldos dos ativos que temos na conta
lista_ativos = info['balances']
print(lista_ativos)

# criar uma ordem dentro da binance
from binance.enums import *
order = client.create_order(
    symbol='BNBBRL',
    side=SIDE_SELL,
    type=ORDER_TYPE_LIMIT,
    timeInForce=TIME_IN_FORCE_GTC,
    quantity=0.01,
    price='0.00001'
    )
print(order)

# visualizar as ordens executadas
print(client.get_all_orders(symbol='BNBBRL'))
print(client.get_my_trades(symbol='BNBBRL'))

# te mostrar as referências de cada par de moedas
print(client.get_symbol_info('BNBBRL'))

# pegar as cotações em tempo real
transacoes = client.get_recent_trades(symbol="BNBBRL", limit=1)
print(transacoes)