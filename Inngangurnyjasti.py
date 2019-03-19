import unittest #Importum module til að að geta framkvæmd einingaprófanir
import time #Importum module til að að hafa smá biðtíma milli falla og skipana
from Viktornyjasti import Viktor #Importum Viktor úr Viktornyjasti til að geta kallað á leikinn í inngangsforritinu
from Vikingurnyjasti import Vikingur #Importum Vikingur úr Vikingurnyjasti til að geta kallað á leikinn í inngangsforritinu
from Aronnyjasti import Aron #Importum Aron úr Aronnyjasti til að geta kallað á leikinn í inngangsforritinu
class Inngangur: #Klasinn

    def __init__(self): #Smiðurinn, notum engan "smið" eins og er, eða hvað?
        pass

    def inngangur(): #Fallið sem byrjar leikinn
        time.sleep(1)
        print("\nAllir nemendur við Háskóla Íslands glíma við sín eigin vandamál og þurfa þeir að leysa þau ef"
        " þeir ætla að útskrifast með sæmd úr háskólanum. Þitt verkefni er að ná að brautskrá sem flesta nemendur.")
        time.sleep(1)
        print("\nHefjumst handa!")
        time.sleep(1)
        val = input("\nNafnið þitt er? ")
        print("\nJæja " + val + ", þitt fyrsta verkefni er Viktor!")
    inngangur()


#__main__
def main():
    leikur1 = Viktor()
    leikur1.kynning()
    leikur1.spurningar()
    leikur2 = Vikingur()
    leikur2.inngangur()
    leikur4 = Hrolfur()
    Leikur4.Intro()
    leikur4 = Aron()
    leikur4.Velja1()
    leikur4.Velja2(namskeid1)

if __name__ == "__main__":
    main()
