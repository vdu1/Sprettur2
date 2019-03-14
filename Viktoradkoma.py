from random import shuffle
import time
#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Viktor:

    def kynning(self):
        time.sleep(1)
        print("\nViktor er dularfullar og hljóðlátur maður og hefur ýmis"
        " leyndarmál að geyma. Það fer ekki mikið fyrir honum og vita fáir að"
        " það eina sem Viktor þráir í raun er ást, umhyggja og smá athygli.\n")
        time.sleep(5)
        print("Verkefni þitt er að svara 10 laufléttum spurningum um Viktor"
        " og svara að lágmarki 5 af þeim rétt til þess að sýna Viktori að"
        " þú þekkir hann og kunnir að meta. Ef þetta tekst mun Viktor brjótast"
        " út úr skelinni, blómstra í námi sínu og útskrifast úr HÍ, ef ekki,"
        " mun hann falla úr skólanum!\n")

    def spurningar(self):

        spurningar = [("Fílar Viktor hávaða? (Já/Nei):", "Nei"),
        ("Fílar Viktor að tala? (Já/Nei):", "Nei"),
        ("Elskar Viktor þögnina? (Já/Nei):", "Já"),
        ("Hvað er uppáhaldsdrykkurinn hans Viktors? (Coke Zero/Peru Nocco/Hvítur GoGo/Pepsi Max):", "Pepsi Max"),
        ("Hvernig bíl á Vikki D? (Trabant/Lada Sport/Audi/Passat):", "Audi"),
        ("Hvað á Viktor margar klippingar eftir? (0/3 max/1/∞):", "3 max"),
        ("Hvað er uppáhalds tækjavörumerkið hans Viktors? (Apple/Dell/HP/Denver):", "Apple"),
        ("Hver er besti hópfélagi Viktors? (Hrólfur/Aron/Þorgeir/Víkingur):", "Þorgeir"),
        ("Bjó Vikki D til iPad gryfjuna? (Já/Nei/Ekki Lexi):", "Já"),
        ("Hvað er prófælmyndin hans Viktors gömul? (2 vikna/3 mánaða/6 ára/Á ekki facebook):", "6 ára")
        ]

        shuffle(spurningar)

        time.sleep(5)
        print("Spurningarnar:\n")
        fjoldirett = 0
        i=0
        for spurning, rettsvar in spurningar:
            i=i+1
            svar = input(str(i) + ". " + spurning + " ")
            time.sleep(1)
            if svar.lower() == rettsvar.lower():
                print("Rétt\n")
                fjoldirett += 1
                time.sleep(2)
            else:
                print("Rangt, svarið er: " + rettsvar + "\n")
                time.sleep(2)
        fjoldirangt = len(spurningar) - fjoldirett
        heildarspurn = len(spurningar)
        time.sleep(1)
        print( "Þú náðir " + str(fjoldirett) + " rétt og " + str(fjoldirangt) + " rangt.\n")
        time.sleep(2)
        if fjoldirett >= 5:
            print("Þú náðir að svara " + str(fjoldirett) + " spurningum af "
            + str(heildarspurn) + ", til hamingju, Viktor er kominn með"
            " BS-gráðu og fer hlæjandi út í atvinnulífið, hjálpaðu næsta"
            " nemanda að útskrifast.\n")
        else:
            print("Þú skeist á þig og varst með " + str(fjoldirangt) +
            " spurningar rangar af " + str(heildarspurn) + ", Viktor hefur því"
            " miður fallið úr skólanum.\n")

def main():

    kall = Viktor()
    kynning = kall.kynning()
    spurningar = kall.spurningar()

if __name__ == "__main__":
    main()
