
import requests
import time
import json

def bs_price():
    BTC = requests.get("https://www.bitstamp.net/api/v2/ticker/btcusd")
    LTC = requests.get("https://www.bitstamp.net/api/v2/ticker/ltcusd")
    ETH = requests.get("https://www.bitstamp.net/api/v2/ticker/ethusd")
    XRP = requests.get("https://www.bitstamp.net/api/v2/ticker/xrpusd")
    BCH = requests.get("https://www.bitstamp.net/api/v2/ticker/bchusd")
    return BTC.json(), LTC.json(), ETH.json(), XRP.json(), BCH.json()

def main():
    while True:
        BTC, LTC, ETH, XRP,BCH = bs_price()

        btc_max=float(BTC["high"])
        btc_min=float(BTC["low"])
        xrp_max=float(XRP["high"])
        xrp_min=float(XRP["low"])
        ltc_max=float(LTC["high"])
        ltc_min=float(LTC["low"])
        eth_max=float(ETH["high"])
        eth_min=float(ETH["low"])
        bch_max=float(BCH["high"])
        bch_min=float(BCH["low"])

        MM=[round(float(((btc_max - btc_min) * 100 / btc_min)),2),round(float(((xrp_max - xrp_min) * 100 / xrp_min)),2),round(float(((ltc_max - ltc_min) * 100 / ltc_min)),2),
             round(float(((eth_max - eth_min) * 100 / eth_min)),2),round(float(((bch_max - bch_min) * 100 / bch_min)),2)]

        cv = ['btc', 'xrp', 'ltc', 'eth', 'bch']


        for i in range(len(MM) - 1, 0, -1):
            for j in range(i):
                if MM[j] < MM[j + 1]:
                    MM[j], MM[j + 1] = MM[j + 1], MM[j]
                    cv[j], cv[j + 1] = cv[j + 1], cv[j]

        def pre():
            print('+-' * 20)
            print(time.asctime(), '\n')
            for value in range(len(MM)):
                print(cv[value], MM[value], '%')

        pre()
        time.sleep(15)


main()