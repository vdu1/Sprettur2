import time #Importum module til að að hafa smá biðtíma milli falla og skipana
from random import shuffle
import sys

class Viktor:


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
            time.sleep(.050)
        for char in print12:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
        for char in print13:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
        time.sleep(1)

        print2 ="\n\nVerkefni þitt er að svara 10 laufléttum spurningum um Viktor og "
        print21="svara að lágmarki 5 af þeim rétt til þess að sýna Viktori að þú þekkir "
        print22="hann og kunnir að meta. Ef þetta tekst mun Viktor brjótast út úr "
        print23="skelinni, blómstra í námi sínu og útskrifast úr HÍ, ef ekki, mun hann falla úr skólanum!"
        for char in print2:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
        for char in print21:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
        for char in print22:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
        for char in print23:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)


    def spyrja(self, spurning, rsvar, i):
            time.sleep(1)
            print3 = "\n" + str(i) + ". "+ spurning
            for char in print3:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.050)
            svar = input("")
            if svar.lower() == rsvar.lower():
                time.sleep(1)
                print("Rétt\n")
                return True
            else:
                time.sleep(1)
                print4 =  "Rangt, svarið er: \n" + rsvar
                for char in print4:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(.050)
                print("\n")
            return False


    def nidurstada(self, fjoldirett, heildarspurn):
        fjoldirangt= heildarspurn - fjoldirett
        print4= "Þú náðir " + str(fjoldirett) + " rétt og " + str(fjoldirangt) + " rangt."
        for char in print4:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
        if fjoldirett >= 5:
            print5 ="Þú náðir að svara " + str(fjoldirett) + " spurningum af " + str(heildarspurn) + ", til hamingju, Viktor er kominn með BS-gráðu og fer hlæjandi út í atvinnulífið, hjálpaðu næsta nemanda að útskrifast."
            for char in print5:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.050)
                return 1
        else:
            print6 ="Þú skeist á þig og varst með " + str(fjoldirangt) + " spurningar rangar af " + str(heildarspurn) + ", Viktor hefur því miður fallið úr skólanum."
            for char in print6s:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.050)
            return 0
def main():
    kall = Viktor()
    kall.Kynning()
    spurningar = [("Fílar Viktor hávaða? (Já/Nei):", "Nei"),
        ("Hvað er uppáhaldsdrykkurinn hans Viktors? (Coke Zero/Peru Nocco/Hvítur GoGo/Pepsi Max):", "Pepsi Max"),
        ("Hvernig bíl á Vikki D? (Trabant/Lada Sport/Audi/Passat):", "Audi"),
        ("Hvað á Viktor margar klippingar eftir? (0/3 max/1/∞):", "3 max"),
        ("Fílar Viktor að tala? (Já/Nei):", "Nei"),
        ("Hvað er uppáhalds tækjavörumerkið hans Viktors? (Apple/Dell/HP/Denver):", "Apple"),
        ("Hver er besti hópfélagi Viktors? (Hrólfur/Aron/Þorgeir/Víkingur):", "Þorgeir"),
        ("Elskar Viktor þögnina? (Já/Nei):", "Já"),
        ("Bjó Vikki D til iPad gryfjuna? (Já/Nei/Ekki Lexi):", "Já"),
        ("Hvað er prófælmyndin hans Viktors gömul? (2 vikna/3 mánaða/6 ára/Á ekki facebook):", "6 ára")
        ]
    i=0
    counter =0
    time.sleep(1)
    print7 = "\n\nSpurningarnar (mundu að vera með bil og kommur réttar):\n"
    for char in print7:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.050)
    #Náum að virkja shuffle inní for-lykkjunni eins og er
    shuffle(spurningar)
    for spurning, rettsvar in spurningar:
        i += 1
        if kall.spyrja(spurning, rettsvar, i)is True:
            counter += 1

    kall.nidurstada(counter, len(spurningar))


if __name__ == "__main__":
    main()
