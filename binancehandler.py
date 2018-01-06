from binance.client import Client
from binance.websockets import BinanceSocketManager




def process_message(msg):
    print("message type: {}".format(msg['e']))
    print(msg)
    # do something
    for each in msg.split(','):
        print(each)


def process_m_message(msg):
    print("stream: {} data: {}".format(msg['stream'], msg['data']))

# pass a list of stream names

client = Client('EMQ2S4ePgPoWJE3LW5YliZuNUwdCbXXj1XkuxW8jrgX4oDAWwOMFGQ8gIkzMPJOC', secretkey)
bm = BinanceSocketManager(client)

#tickers = client.get_ticker()

#conn_key = bm.start_ticker_socket(process_message)
#conn_key = bm.start_multiplex_socket(['ethbtc@ticker', 'neobtc@ticker'], process_m_message)
testp = bm.start_symbol_ticker_socket('ethbtc',  process_message)
bm.start()