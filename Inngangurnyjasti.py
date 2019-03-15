import time
from Viktornyjasti import Viktor
from Vikingurnyjasti import Vikingur

class Inngangur:
    def inngangur():
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
leikur1 = Viktor()
leikur1.kynning()
leikur1.spurningar()
leikur2 = Vikingur()
leikur2.inngangur()
