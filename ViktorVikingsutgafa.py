# This Python file uses the following encoding: utf-8
from random import shuffle


def Kynning():
    print()
    print("Viktor er dularfullar og hljóðlátur maður og hefur ýmis leyndarmál að geyma. Það fer ekki mikið fyrir honum og vita fáir að það eina sem Viktor þráir í raun er ást, umhyggja og smá athygli.")
    print()
    print("Verkefni þitt er að svara 8 laufléttum spurningum um Viktor og svara að lágmarki 5 af þeim rétt til þess að sýna Viktori að þú þekkir hann og kunnir að meta. Ef þetta tekst mun Viktor brjótast út úr skelinni, blómstra í námi sínu og útskrifast úr HÍ, ef ekki, mun hann falla úr skólanum!")
    print()



def spyrja(spurning, rsvar, i):
        rettrangt=0
        svar = input(str(i) + ". " + spurning + " ")
        if svar.lower() == rsvar.lower():
            print("Rétt")
            rettrangt=1
        else:
            print("Rangt, svarið er: " + rsvar)
        return rettrangt


def nidurstada(fjoldirett, heildarspurn):
    fjoldirangt= heildarspurn - fjoldirett
    print( "Þú náðir " + str(fjoldirett) + " rétt og " + str(fjoldirangt) + " rangt.")
    if fjoldirett >= 5:
        print("Þú náðir að svara " + str(fjoldirett) + " spurningum af " + str(heildarspurn) + ", til hamingju, Viktor er kominn með BS-gráðu og fer hlæjandi út í atvinnulífið, hjálpaðu næsta nemanda að útskrifast.")
    else:
        print("Þú skeist á þig og varst með " + str(fjoldirangt) + " spurningar rangar af " + str(heildarspurn) + ", Viktor hefur því miður fallið úr skólanum.")

#_main_
Kynning()
spurningar = [("Fílar Viktor hávaða? (Já/Nei):", "Nei"),
    ("Fílar Viktor að tala? (Já/Nei):", "Nei"),
    ("Elskar Viktor þögnina? (Já/Nei):", "Já"),
    ("Hvað er uppáhaldsdrykkurinn hans Viktors? (Coke Zero/Peru Nocco/Hvítur GoGo/Pepsi Max):", "Pepsi Max"),
    ("Hvernig bíl á Vikki D? (Trabant/Lada Sport/Audi/Passat)", "Audi"),
    ("Hvað á Viktor margar klippingar eftir? (0/3 max/1/∞):", "3 max"),
    ("Hvað er uppáhalds tækjavörumerkið hans Viktors? (Apple/Dell/HP/Denver):", "Apple"),
    ("Hver er besti hópfélagi Viktors? (Hrólfur/Aron/Þorgeir/Víkingur):", "Þorgeir")]
shuffle(spurningar)
i=0
counter =0
for spurning, rettsvar in spurningar:
    i += 1
    counter =counter + spyrja(spurning, rettsvar, i)


nidurstada(counter, len(spurningar))
