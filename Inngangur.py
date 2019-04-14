import sys
import time

class Inngangur: #Klasinn

    def __init__(self): #Smiðurinn, notum engan "smið" eins og er, eða hvað?
        pass

    def inngangur(self): #Fallið sem byrjar leikinn
        time.sleep(1)
        Inngangur = "\nAllir nemendur við Háskóla Íslands glíma við sín eigin vandamál og þurfa þeir að leysa þau ef þeir ætla að útskrifast með sæmd úr háskólanum. Þitt verkefni er að komast í gegnum þrautir leiksins og ná að brautskrá sem flesta nemendur."
        for char in Inngangur:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(1)
        hefjumst = "\n\nHefjumst handa!"
        for char in hefjumst:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(1)
        nafnid = "\n\nNafnið þitt er? "
        for char in nafnid:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        nafn = input("")
        time.sleep(1)
        print2 = "\nJæja " + nafn + ", þitt fyrsta verkefni er Viktor!\n"
        for char in print2:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        return nafn
def main():
    kall = Inngangur()
    nafn1=kall.inngangur()

if __name__ == "__main__":
    main()
