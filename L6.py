import requests
import time
import json

def show(data):
    print("aktualny stan portfela ", data)

def wallc(data):
    for key in list(data.keys()):
        if data[key] == 0:
            del data[key]
    cb = 0
    cn = 0
    parameteres = {'time': 'day'}

    for i in list(data.keys()):
        currency_data = i
        bs = requests.get("https://www.bitstamp.net/api/v2/transactions/{0}usd".format(currency_data),
                                  params=parameteres)
        pn = float(bs.json()[0]['price'])
        pp = float(bs.json()[-1]['price'])
        diff = round((100 * ((pn - pp) / pp)), 2)
        cb += data[i]*pp
        cn += data[i]*pn
        print(currency_data.upper())
        print("Aktualna cena:", pn,"USD "," Cena sprzed 24h:", pp,"USD")
        print("Zmiana kursu na przestrzeni 24h:", diff, "%", "Aktualna ilość w portfelu:", round(data[i], 3))
        print("Wartość w ciągu 24h zmieniła się o:", round(data[i]*pp*(diff/100), 2), "USD")
        time.sleep(1)

    print("\n   Całkowita zmiana wartości portfela w ciągu 24h =",round(cn-cb,2),"USD czyli",round(100 * ((cn - cb) / cb), 2),"%)")


def addc(data,wallet):
    avaiable_currences = ["btc", "xrp", "ltc", "eth", "bch"]
    show(data)
    print("Do wyboru: ", avaiable_currences)
    print("Podaj skrót zmienianej waluty:")
    currency = input().lower()

    while currency not in avaiable_currences:
        print("Wprowadzonej waluty nie było do wyboru, proszę wprowadź ponownie ")
        currency = input()

    q = float(input(">> Jaką ilość chcesz dodać? Chcąć odjąć środki z portfela wprowadź '-' przed wartością \n"))

    if data[currency] == 0:
        if q==0:
            data[currency] = q
        while q < 0 :
            print("Nie możesz posiadać długu. Podaj inną wartość")
            q = float(input())
    else:
        while data[currency]+q < 0 :
            print("Nie możesz posiadać długu. Podaj inną wartość")
            q = float(input())


    data[currency] += q

    with open(wallet, "w") as write_file:
        json.dump(data, write_file)
    show(data)


def menu(data,wallet):
    print('Wybierz jedną z dostępnych możliwości')
    print('1: Zmień ilość waluty w portfelu')
    print('2: pokaż portfel')
    print('3: Pokaż zmiany')
    print('0: wyjście')
    choice = input()

    if choice == '1':
        addc(data,wallet)
    elif choice == '2':
        print(data)
    elif choice == '3':
        wallc(data)
    elif choice == '0':
        return 0


def main():
    print('Wprowadź nazwę pliku:')
    wallet = input() + '.json'
    with open(wallet) as json_file:
        data = json.load(json_file)
        #print("plik załadowany")

    while True:
        if menu(data,wallet) == 0:
            break 


main()
