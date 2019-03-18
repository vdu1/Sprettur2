import time
from klasavikingur import Vikingur
from Viktoradkoma import Viktor

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


#__main__
kennari=[]
leikur1 = Viktor(True)
kennri.append(leikur1)

leikur1.kynning()
leikur1.spurningar()

leikur2 = Vikingur(False)
kennari.append(leikur2)

leikur2.inngangur()
