# This Python file uses the following encoding: utf-8
import time #Importum module til að að hafa smá biðtíma milli falla og skipana
from random import shuffle
from Viktor import Viktor #Importum Viktor úr Viktornyjasti til að geta kallað á leikinn í inngangsforritinu
from Vikingur import Vikingur2 #Importum Vikingur úr Vikingurnyjasti til að geta kallað á leikinn í inngangsforritinu
from Hrolfur import Hrolfur #Importum Hrolfur úr LeikurHrólfur til að geta kallað á leikinn í inngangsforritinu
from Aron import Aron #Importum Aron úr Aronnyjasti til að geta kallað á leikinn í inngangsforritinu
from Inngangur import Inngangur
from shutil import get_terminal_size
import sys

#__main__
def main():
    Teljari = 0
    print("\n" * get_terminal_size().lines, end='')
    kall = Inngangur()
    nafn1=kall.inngangur()

#Kallið fyrir leikur1
    print("\n" * get_terminal_size().lines, end='')
    kall = Viktor()
    kall.Kynning()
    spurningar = [("Fílar Viktor hávaða?\n      A. Já\n      B. Nei", "B"),
        ("Hvað er uppáhaldsdrykkurinn hans Viktors?\n      A. Coke Zero\n      B. Peru Nocco\n      C. Hvítur GoGo\n      D. Pepsi Max", "D"),
        ("Hvernig bíl á Vikki D?\n      A. Trabant\n      B. Lada Sport\n      C. Audi\n      D. Passat", "C"),
        ("Hvað á Viktor margar klippingar eftir?\n      A. 0\n      B. 3 max\n      C. 1\n      D. ∞", "B"),
        ("Fílar Viktor að tala?\n      A. Já\n      B. Nei", "B"),
        ("Hvað er uppáhalds tækjavörumerkið hans Viktors?\n      A. Apple\n      B. Dell\n      C. HP\n      D. Denver", "A"),
        ("Hver er besti hópfélagi Viktors?\n      A. Hrólfur\n      B. Aron\n      C. Þorgeir\n      D. Víkingur", "C"),
        ("Elskar Viktor þögnina?\n      A. Já\n      B. Nei", "A"),
        ("Bjó Vikki D til iPad gryfjuna?\n      A. Já\n      B. Nei\n      C. Ekki Lexi", "A"),
        ("Hvað er prófælmyndin hans Viktors gömul?\n      A. 2 vikna\n      B. 3 mánaða\n      C. 6 ára\n      D. Á ekki facebook", "C")
        ]
    i=0
    counter=0
    time.sleep(1)
    print7 = "\n\nSpurningarnar (mundu að svara aðeins A, B, C eða D):\n\n"
    for char in print7:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.050)
    time.sleep(1)
    shuffle(spurningar)
    for spurning, rettsvar in spurningar:
        i += 1
        if kall.spyrja(spurning, rettsvar, i)is True:
            counter += 1

    Teljari += kall.nidurstada(counter, len(spurningar))

    #Kallið fyrir leikur2
    print("\n" * get_terminal_size().lines, end='')
    Útskrift= False
    kall = Vikingur()
    kall.inngangur()
    kall.prof()
    kall.matur()
    nidurstada1 = kall.logn()
    if nidurstada1 == "P":
        Útskrift = kall.lokaprof()
    elif nidurstada1 == "Ú":
        Útskrift = True
    if Útskrift is True:
        Teljari += 1

    #Kallið fyrir leikur3
    print("\n" * get_terminal_size().lines, end='')
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
    if einingar == 12:
        Teljari += 1

    #Kallið fyrir leikur4
    print("\n" * get_terminal_size().lines, end='')
    kall = Hrolfur()
    har = 100
    har -= kall.intro1()
    if har>20:
        har -= kall.HaskoliStartintro()
    kall.Nidurstada(har)

    #Nú viljum við taka allt saman til að birta niðurstöður leikjanna
    print("\n" * get_terminal_size().lines, end='')
    print(nafn1 + " þú útskrifaðir " + str(Teljari) + " af 4 nemendum")

if __name__ == "__main__":
    main()
