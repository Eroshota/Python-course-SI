import requests


def bb_order():
    response = requests.get("https://bitbay.net/API/Public/BTC/orderbook.json")
    return response.json()


def bb_ticker():
    response = requests.get("https://bitbay.net/API/Public/BTC/ticker.json")
    return response.json()
def cex():

    data=requests.get('https://cex.io/api/ticker/BTC/USD')
    return data.json()
def part1():
    print("Part 1")
    db = bb_order()
    print('-'*40)
    print('BIDS')
    print('-'*40)
    for i in db['bids']:
        print('Rate USD = ',i[0],"Amount BTC = ",i[1])
    print('-'*40)
    print("ASKS")
    print('-'*40)
    for i in db['asks']:
        print('Rate USD = ',i[0],"Amount BTC = ",i[1])

def part2():
    print("Part 2")
    c = cex()
    bb = bb_ticker()

    abb = bb['ask']
    bbb = bb['bid']

    ac=c['ask']
    bc = c['bid']

    if abb > ac:
        print("Better buy from Cex")
    else: 
        print("Better buy from Bitbay")
    if bbb > bc:
        print("Better sell at Bitbay")
    else:
         print("Better sell at Cex")
print("LAB 3")

part1()
part2()
