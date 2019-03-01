from random import shuffle

print("Viktor er dularfullar maður og hefur ýmis leyndarmál að geyma. Þú færð 10 spurningar um Viktor og þarft að svara 5 af þeim rétt til þess að útskrifa Viktor úr HÍ, ef þú nærð því ekki þá fellur Viktor úr skólanum!")
spurningar = [("Fílar Viktor hávaða? (já/nei)", "nei"),("Fílar Viktor að tala? (já/nei)", "nei"),("Elskar Viktor þögnina? (já/nei)", "já"),("Hvað er uppáhaldsdrykkurinn hans Viktors? (coke zero/peru nocco/hvítur gogo/pepsi max)", "pepsi max"),("Hvernig bíl á Vikki D? (trabant/lada sport/audi/passat)", "audi"),("Hvað á Viktor margar klippingar eftir? (0/3 max/1/∞)", "3 max"),("Hvað er uppáhalds tækjavörumerkið hans Viktors? (apple/dell/hp/denver)", "apple"),("Hver er hópfélagi Viktors? (Hrólfur/Aron/Þorgeir/Víkingur)", "Þorgeir")]

shuffle(spurningar)
fjoldirett = 0
i=0
for spurning, rettsvar in spurningar:
    i=i+1
    svar = input(str(i) + ". " + spurning + " ")
    if svar.lower() == rettsvar.lower():
        print("Rétt")
        fjoldirett += 1
    else:
        print("Rangt, svarið er: " + rettsvar)
fjoldirangt = len(spurningar) - fjoldirett
heildarspurn = len(spurningar)
print( "Þú náðir " + str(fjoldirett) + " rétt og " + str(fjoldirangt) + " rangt.")
if fjoldirett >= 5:
    print("Þú náðir að svara " + str(fjoldirett) + " spurningum af " + str(heildarspurn) + ", til hamingju, Viktor er kominn með BS-gráðu og fer hlæjandi út í atvinnulífið, hjálpaðu næsta nemanda að útskrifast.")
else:
    print("Þú skeist á þig og varst með " + str(fjoldirangt) + " spurningar rangar af " + str(heildarspurn) + ", Viktor hefur því miður fallið úr skólanum.")
