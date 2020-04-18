
import requests
import time

def req():
    bb=requests.get('https://bitbay.net/API/Public/BTC/USD/ticker.json')
    c=requests.get('https://cex.io/api/ticker/BTC/USD')
    bs=requests.get('https://www.bitstamp.net/api/ticker')
    bc=requests.get("https://blockchain.info/ticker")
    return bb.json(),c.json(),bs.json(),bc.json()

def walup(wallet, buy, sell):
    #wallet[1] = wallet[1] + 0.01
    wallet[0] = wallet[0] - buy*0.01
    wallet[1] = wallet[1] - 0.01
    wallet[0] = wallet[0] + sell*0.01
    return wallet

def arbitration(wallet):
    bbt, ct, bst, bct = req()
    bbtb=float(bbt['bid'])
    bbta=float(bbt['ask'])
    ctb=float(ct['bid'])
    cta=float(ct['ask'])
    bstb=float(bst['bid'])
    bsta=float(bst['ask'])
    bctb=float(bct['USD']['sell'])
    bcta=float(bct['USD']['buy'])


    buy= {'bitbay':bbta, 'cex':cta, 'bitstamp':bsta, 'blockchain':bcta}
    sell= {'bitbay':bbtb, 'cex':ctb, 'bitstamp':bstb, 'blockchain':bctb}

    lowest=min(buy.values())
    lowesto=min(buy,key=buy.get)

    highest=max(sell.values())
    highesto=max(sell,key=sell.get)

    if lowest<highest:
        print(f"On the {lowesto} You can buy 0,01 BTC for USD at the exchange rate of {lowest} and  sell on the {highesto}, gaining {(highest-lowest)*0.1} USD ")
        print(
            f"New Wallet: {walup(wallet, lowest, highest)}")
    else:
        print("not worth")
wallet = [100, 2.0]
nwallet = wallet[:]

while(True):
    arbitration(nwallet)
    if (nwallet[0]-wallet[0]) > 0:
        print(f"You earned on transactions: {nwallet[0]-wallet[0]} USD")
    time.sleep(5)
