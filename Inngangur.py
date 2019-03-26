import time
import sys
class Inngangur: #Klasinn

    def __init__(self): #Smiðurinn, notum engan "smið" eins og er, eða hvað?
        pass

    def inngangur(self): #Fallið sem byrjar leikinn
        inngangu = "\nAllir nemendur við Háskóla Íslands glíma við sín eigin vandamál og þurfa þeir að leysa þau ef þeir ætla að útskrifast með sæmd úr\nháskólanum. Þitt verkefni er að komast í gegnum þrautir leiksins og ná að brautskrá sem flesta nemendur."

        for char in inngangu:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)

        print("\n")
        #time.sleep(5)
        hefjumst = "\nHefjumst handa!"
        for char in hefjumst:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
        nafn = input("\nNafnið þitt er? ")
        #time.sleep(2)
        print2 = "\nJæja " + nafn + ", þitt fyrsta verkefni er Viktor!\n"
        for char in print2:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
        return nafn
def main():
    kall = Inngangur()
    nafn1=kall.inngangur()

if __name__ == "__main__":
    main()
