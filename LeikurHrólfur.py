# This Python file uses the following encoding: utf-8
import math
import random
import time



def intro():
    counter =0
    svar_A = ["A", "a"]
    svar_B = ["B", "b"]
    svar_C = ["C", "c"]
    Ja = ["J", "j", "já", "JÁ", "Já"]
    Nei = ["N", "n", "nei", "Nei", "NEI"]

    print("Hrólfur Sveinsson er ungur drengur úr Hafnarfirðinum."+"\n")
    time.sleep(1)
    print("Hrólfur á við ýmis vandamál að stríða. Útaf þessum vandamálum er hann oft áhyggjufullur."+"\n")
    time.sleep(1)
    print("Þökk sé streitu sér Hrólfur ungur að hann er nálægt því að missa hárið."+"\n")
    time.sleep(1)
    print("Þú ert nú komin í það hlutverk að hjálpa Hrólf með allar ákvarðanir til að minnka streitu og halda í hárið."+"\n")
    time.sleep(1)
    print("Hrólfur veit að ef hann missir allt hárið þá mun hafa ekki hafa sjálfstraustið í að klára háskólann."+"\n")
    time.sleep(1)
    print("Fyrsta stóra ákvörðunin sem þú þarft að hjálpa Hrólf með er í hvaða framhaldsskóla hann á að fara.")
    time.sleep(1)
    print ("""  A. Menntaskólann í Reykjavík
    B. Flensborgarskólann í Hafnarfirði
    C. Verzlunarskóla Íslands""")
    choice = input(">>> ") #Here is your first choice.
    if choice in svar_A:
        print("Jæja, þú ert ömurlegur ráðgjafi. Hrólfur missti allt hárið og féll úr MR á fyrstu önninni. Hann er samt mjög ánægður á dælunni.")
        return 100
    elif choice in svar_B:
        counter += option_Flens()
    elif choice in svar_C:
        counter += option_Verzl()
    else:
        print ("A, B eða C takk fyrir")
        intro()
    return counter

def option_Flens():
    svar_A = ["A", "a"]
    svar_B = ["B", "b"]
    svar_C = ["C", "c"]
    Ja = ["J", "j", "já", "JÁ", "Já"]
    Nei = ["N", "n", "nei", "Nei", "NEI"]

    print("Hrólfur er mættur í Flensborg. Honum líður vel í Firðinum og rúllar upp náminu."+"\n")
    print("Þrátt fyrir að vera heimakær hefur Hrólfur áhyggjur af að finna ekki spennandi kvenkost í Hafnarfirðinum."+"\n")
    print("Þetta angrar hann ekki svakalega en samt nóg til að hann missi 4 hár af hausnum"+"\n")
    counter = 4
    time.sleep(1)
    print("Hrólfur er mikill fótboltastrákur. Hann elskar fátt meira en að sparka í boltann með góðum félögum"+"\n")
    print("Hrólfur er hinsvegar í erfiðri stöðu. Félagarnir eru ekki með jafn mikið metnað í boltanum. Hrólfur sjálfur gæti fengið að æfa með meistaraflokki FH í sumar."+"\n")
    print("Hrólfur veit samt að það er mikið álag að vera í meistaraflokki"+"Ætti hann að eltast við draumana í FH eða ætti hann að fara með félögunum í Passion League"+"\n")
    time.sleep(1)
    print (" A. FH"
    "B. Passion League ")
    choice = input(">>> ")
    if choice in svar_A:
        print("Þetta var slæm ákvörðun. Hrólf líður ekki vel í FH reynir í nokkra mánuði að æfa undir miklu álagi en hættir síðan. -10 hár")
        counter += 10
    elif choice in svar_B:
        print ("Geggjuð ákvörðun. Hrólfur skemmtir sér konunglega með félögunum í Passion League, einn stóran Tuborg takk."+"\n")
    else:
        print ("A eða B koma svo")
    print("Námið í Flensborg er að fara vel með Hrólf. Hann er samt að velta því fyrir sér hvort hann eigi að eltast við að vera Dúx."+"\n")
    print("Það gæti gert eitthvað fyrir sjálfstraustið hans að vera dúx en það er auðvitað mikil vinna sem myndi fara í það"+"\n")
    print("A fyrir að eltast við að vera dúx eða B fyrir að útskrifast bara")
    time.sleep(1)
    choice = input(">>> ")
    if choice in svar_A:
        print("Ekki vera svona heimskur, maður græðir ekkert á að vera Dúx, spurðu bara Erni Jónsson"+"\n")
        print("-10 hár fyrir óþarfan metnað í námi")
        counter += 10
    elif choice in svar_B:
        print ("Geggjuð ákvörðun. Hrólfur skemmtir sér konunglega með félögunum í Passion League, einn stóran Tuborg takk."+"\n")
    else:
        print ("A eða B koma svo")
    return counter

def option_Verzl():
    counter=0
    svar_A = ["A", "a"]
    svar_B = ["B", "b"]
    svar_C = ["C", "c"]
    Ja = ["J", "j", "já", "JÁ", "Já"]
    Nei = ["N", "n", "nei", "Nei", "NEI"]

    print("Hrólfur er mættur í Verzló. Honum finnst félagslífið skemmtilegt en námið er erfitt."+"\n")
    print("Snappið hans Hrólfs er ekki lengi að fyllast af skonsum eftir að hann byrjar í Verzló."+"\n")
    print("Álagið við að svara öllum þessum skonsum lætur hann missa 10 hár af hausnum"+"\n")
    counter += 10
    time.sleep(1)
    print("Hrólfur er mikill fótboltastrákur. Hann elskar fátt meira en að sparka í boltann með góðum félögum"+"\n")
    print("Hrólfur er hinsvegar í erfiðri stöðu. Félagarnir eru ekki með jafn mikið metnað í boltanum. Hrólfur sjálfur gæti fengið að æfa með meistaraflokki FH í sumar."+"\n")
    print("Hrólfur veit samt að það er mikið álag að vera í meistaraflokki"+"Ætti hann að eltast við draumana í FH eða ætti hann að fara með félögunum í Passion League"+"\n")
    time.sleep(1)
    print ("""  A. FH
    B. Passion League
    """)
    choice = input(">>> ")
    if choice in svar_A:
        print("Þetta var slæm ákvörðun. Hrólf líður ekki vel í FH reynir í nokkra mánuði að æfa undir miklu álagi en hættir síðan. -10 hár")
        counter = counter -10
    elif choice in svar_B:
        print ("Geggjuð ákvörðun. Hrólfur skemmtir sér konunglega með félögunum í Passion League, einn stóran Tuborg takk."+"\n")
    else:
        print ("A eða B koma svo")
    print("Námið í Verzló er erfitt fyrir Hrólfur. Hann er að velta því fyrir sér hvort hann eigi að halda áfram eða hætta bara í skólanum."+"\n")
    print("Hann gæti átt erfitt með að halda sér í Verzló en það gæti verið að hann flosni úr skóla ef hann fer í Flensborg"+"\n")
    print("A fyrir að halda áfram eða B fyrir Flensborg")
    time.sleep(1)
    choice = input(">>> ")
    if choice in svar_A:
        print("Hrólfur tók sig á fyrir prófin og gekk mjög vel. Hann var alltaf vel undirbúinn og var því ekkert stressaður"+"\n")
    elif choice in svar_B:
        print ("Hrólfur fílaði sig ekki alveg í Flensborg, flosnaði úr námi og fór aldrei í háskólann."+"\n")
        counter =100
        return counter
    else:
        print ("A eða B koma svo")
    return counter







#_main_


har = 100
har -= intro()
