import time #Importum module til að að hafa smá biðtíma milli falla og skipana
from random import shuffle

class Viktor:


    def __init__(self):
        pass
    def Kynning(self):
        time.sleep(3)
        print("Viktor er dularfullar og hljóðlátur maður og hefur ýmis leyndarmál"
        " að geyma. Það fer ekki mikið fyrir honum og vita fáir að það eina sem"
        " Viktor þráir í raun er ást, umhyggja og smá athygli.")
        time.sleep(5)
        print("\nVerkefni þitt er að svara 10 laufléttum spurningum um Viktor og"
        " svara að lágmarki 5 af þeim rétt til þess að sýna Viktori að þú þekkir"
        " hann og kunnir að meta. Ef þetta tekst mun Viktor brjótast út úr"
        " skelinni, blómstra í námi sínu og útskrifast úr HÍ, ef ekki, mun hann falla úr skólanum!")



    def spyrja(self, spurning, rsvar, i):
            time.sleep(2)
            svar = input(str(i) + ". " + spurning + " ")
            if svar.lower() == rsvar.lower():
                time.sleep(1)
                print("Rétt\n")
                return True
            else:
                time.sleep(1)
                print("Rangt, svarið er: \n" + rsvar)
            return False


    def nidurstada(self, fjoldirett, heildarspurn):
        fjoldirangt= heildarspurn - fjoldirett
        print( "Þú náðir " + str(fjoldirett) + " rétt og " + str(fjoldirangt) + " rangt.")
        if fjoldirett >= 5:
            print("Þú náðir að svara " + str(fjoldirett) + " spurningum af " + str(heildarspurn) + ", til hamingju, Viktor er kominn með BS-gráðu og fer hlæjandi út í atvinnulífið, hjálpaðu næsta nemanda að útskrifast.")
            return 1
        else:
            print("Þú skeist á þig og varst með " + str(fjoldirangt) + " spurningar rangar af " + str(heildarspurn) + ", Viktor hefur því miður fallið úr skólanum.")
            return 0
def main():
    kall = Viktor()
    kall.Kynning()
    spurningar = [("Fílar Viktor hávaða? (Já/Nei):", "Nei"),
        ("Hvað er uppáhaldsdrykkurinn hans Viktors? (Coke Zero/Peru Nocco/Hvítur GoGo/Pepsi Max):", "Pepsi Max"),
        ("Hvernig bíl á Vikki D? (Trabant/Lada Sport/Audi/Passat)", "Audi"),
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
    time.sleep(9)
    print("\nSpurningarnar (mundu að vera með bil og kommur réttar):\n")
    #Náum að virkja shuffle inní for-lykkjunni eins og er
    #shuffle(spurningar)
    for spurning, rettsvar in spurningar:
        i += 1
        if kall.spyrja(spurning, rettsvar, i)is True:
            counter += 1

    kall.nidurstada(counter, len(spurningar))


if __name__ == "__main__":
    main()
