import time #Importum module til að að hafa smá biðtíma milli falla og skipana
from random import shuffle
import sys
from shutil import get_terminal_size

class Viktor:

    rettinntak = ["A", "a", "B", "b", "C", "c", "D", "d"]
    rettinntakprint = ("\nEitthvað fór úrskeiðis hjá þér, mundu að nota rétta stafi\n") #Til að koma í veg fyrir misskilning

    def __init__(self):
        pass
    def Kynning(self):
        time.sleep(1)
        print1 ="\nViktor er dularfullur og hljóðlátur maður og hefur ýmis leyndarmál "
        print12="að geyma. Það fer ekki mikið fyrir honum og vita fáir að það eina sem "
        print13=" Viktor þráir í raun er ást, umhyggja og smá athygli."
        for char in print1:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        for char in print12:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        for char in print13:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(1)

        print2 ="\n\nVerkefni þitt er að svara 10 laufléttum spurningum um Viktor og "
        print21="svara að lágmarki 5 af þeim rétt til þess að sýna Viktori að þú þekkir "
        print22="hann og kunnir að meta. Ef þetta tekst mun Viktor brjótast út úr "
        print23="skelinni, blómstra í námi sínu og útskrifast úr HÍ, ef ekki, mun hann falla úr skólanum!"
        for char in print2:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        for char in print21:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        for char in print22:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        for char in print23:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)


    def spyrja(self, spurning, rsvar, i):
            time.sleep(1)
            print3 = str(i) + ". "+ spurning
            for char in print3:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            time.sleep(1)
            svar = None

            #Henda inn try/except hér?
            while svar not in self.rettinntak:
                svar = input("\n>>> ")
                if svar in self.rettinntak:
                    if svar.lower() == rsvar.lower():
                        time.sleep(1)
                        printr = "\nRétt\n\n"
                        for char in printr:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        return True
                    elif svar in self.rettinntak:
                        time.sleep(1)
                        print4 =  "\nRangt, svarið er: " + rsvar + "\n\n"
                        for char in print4:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        return False
                else:
                    printrettinntak = self.rettinntakprint
                    for char in printrettinntak:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    time.sleep(1)

    def nidurstada(self, fjoldirett, heildarspurn):
        fjoldirangt= heildarspurn - fjoldirett
        if fjoldirett >= 5:
            time.sleep(1)
            print17 ="Þú náðir að svara " + str(fjoldirett) + " spurningum af " + str(heildarspurn) + ", til hamingju, Viktor er kominn með BS-gráðu og fer hlæjandi út í atvinnulífið, hjálpaðu næsta nemanda að útskrifast.\n\n"
            for char in print17:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            return 1
        else:
            time.sleep(1)
            print6 ="Þú skeist á þig og varst með " + str(fjoldirangt) + " spurningar rangar af " + str(heildarspurn) + ", Viktor hefur því miður fallið úr skólanum, hjálpaðu næsta nemanda að útskrifast.\n\n"
            for char in print6:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            return 0
def main():
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
    print7 = "\n\nSpurningarnar (mundu að svara aðeins A, B, C eða D eftir því sem við á):\n\n"
    for char in print7:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    time.sleep(1)
    shuffle(spurningar)
    for spurning, rettsvar in spurningar:
        i += 1
        if kall.spyrja(spurning, rettsvar, i)is True:
            counter += 1

    kall.nidurstada(counter, len(spurningar))


if __name__ == "__main__":
    main()
