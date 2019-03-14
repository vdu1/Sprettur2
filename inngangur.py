import time
svar_A = ["Hrólfur", "hrólfur"]
svar_B = ["Aron", "aron"]
tsvar = ("\nNotaðu aðeins A eða B\n")

class Inngangur:
    def inngangur():
        time.sleep(1)
        print("\nAllir nemendur við Háskóla Íslands glíma við sín eigin vandamál og þurfa þeir að leysa þau ef"
        " þeir ætla að útskrifast með sæmd úr háskólanum. Þitt verkefni er að ná að brautskrá sem flesta nemendur.")
        time.sleep(2)
        print("\nHefjumst handa!")
        time.sleep(2)
        val = input("\nNafnið þitt er? ")
        print("\nJæja " + val + ", þitt fyrsta verkefni er Viktor!")
        if val in svar_A:
            pass
        elif val in svar_B:
            pass
        else:
            print(tsvar)
            inngangur()
    inngangur()

from Viktoradkoma import Viktor
leikur1 = Viktor()
leikur1.kynning()
leikur1.spurningar()
from klasavikingur import Vikingur
leikur2 = Vikingur()
leikur2.inngangur()
