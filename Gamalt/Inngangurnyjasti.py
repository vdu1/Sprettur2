# This Python file uses the following encoding: utf-8
import unittest #Importum module til að að geta framkvæmd einingaprófanir
import time #Importum module til að að hafa smá biðtíma milli falla og skipana
from Viktornyjasti import Viktor #Importum Viktor úr Viktornyjasti til að geta kallað á leikinn í inngangsforritinu
from Vikingurnyjasti import Vikingur #Importum Vikingur úr Vikingurnyjasti til að geta kallað á leikinn í inngangsforritinu
<<<<<<< HEAD:Gamalt/Inngangurnyjasti.py
from LeikurHrólfur import Hrolfur #Importum Hrolfur úr LeikurHrólfur til að geta kallað á leikinn í inngangsforritinu
from AronnyjastiFyrirHrólfur import Aron #Importum Aron úr Aronnyjasti til að geta kallað á leikinn í inngangsforritinu
=======
from Aronnyjasti import Aron #Importum Aron úr Aronnyjasti til að geta kallað á leikinn í inngangsforritinu
>>>>>>> d43f6f8afe983c5a593a16af7aaf7779c28980ef:Inngangurnyjasti.py
class Inngangur: #Klasinn

    def __init__(self): #Smiðurinn, notum engan "smið" eins og er, eða hvað?
        pass

    def inngangur(): #Fallið sem byrjar leikinn
        time.sleep(1)
        print("\nAllir nemendur við Háskóla Íslands glíma við sín eigin vandamál og þurfa þeir að leysa þau ef"
        " þeir ætla að útskrifast með sæmd úr\nháskólanum. Þitt verkefni er að komast í gegnum þrautir leiksins og ná að brautskrá sem flesta nemendur.")
        time.sleep(5)
        print("\nHefjumst handa!")
        time.sleep(1)
        val = input("\nNafnið þitt er? ")
        time.sleep(2)
        print("\nJæja " + val + ", þitt fyrsta verkefni er Viktor!")
    inngangur()


#__main__
def main():
    leikur1 = Viktor()
    leikur1.kynning()
    leikur1.spurningar()
    leikur2 = Vikingur()
    leikur2.inngangur()

    """
    #Kallið fyrir leikur3
    einingar=0
    kall = Aron()
    namskeid1 = kall.Velja1()
    namskeid2 = kall.Velja2(namskeid1)
    if namskeid1.lower() == 's' or namskeid2.lower() == 's':
        einingar = einingar+6*kall.S1Prof()

    # Til að spara forritun átti maður ekki séns á að ná eðlisfræðinni
    # Bætum mögulega við prófi í eðlisfræði fyrir næsta sprett
    if namskeid1.lower() == 'e' or namskeid2.lower() == 'e':
        print('Aldeilis mistök sem þú gerðir að velja Eðlisfræði prófið.')
        print('Þú áttir aldrei séns og fékkst núll í prófinu')

    if namskeid1.lower() == 'l' or namskeid2.lower() =='l':
        einingar = einingar+6*kall.Lprof()
    print('Þú endaðir með '+ str(einingar) + " einingar, til hamingju! Hjálpaðu næsta nemanda að útskrifast")

    leikur4 = Hrolfur()
<<<<<<< HEAD:Gamalt/Inngangurnyjasti.py
    leikur4.intro()
    """

    print(utskrifadir2)
=======
    Leikur4.Intro()
    leikur4 = Aron()
    leikur4.Velja1()
    leikur4.Velja2(namskeid1)
>>>>>>> d43f6f8afe983c5a593a16af7aaf7779c28980ef:Inngangurnyjasti.py

if __name__ == "__main__":
    main()
