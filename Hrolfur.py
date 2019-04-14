# This Python file uses the following encoding: utf-8
import math
import random
import time
import sys
from shutil import get_terminal_size

class Hrolfur:

    def __init__(self):
        pass

    def intro1(self):
        counter =0
        svar_A = ["A", "a"]
        svar_B = ["B", "b"]
        svar_C = ["C", "c"]
        Ja = ["J", "j", "já", "JÁ", "Já"]
        Nei = ["N", "n", "nei", "Nei", "NEI"]
        choice = None

        print1 ="Hrólfur Sveinsson er ungur drengur úr Hafnarfirðinum."+"\n\n"
        for char in print1:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(1)
        print2="Hrólfur á við ýmis vandamál að stríða. Útaf þessum vandamálum er hann oft áhyggjufullur."+"\n"
        for char in print2:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(1)
        print3= "Þökk sé streitu sér Hrólfur ungur að hann er nálægt því að missa hárið."+"\n\n"
        for char in print3:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(1)
        print4="Þú ert nú komin í það hlutverk að hjálpa Hrólf með allar ákvarðanir til að minnka streitu og halda í hárið."+"\n"
        for char in print4:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(1)
        print5="Hrólfur veit að ef hann missir allt hárið þá mun hafa ekki hafa sjálfstraustið í að klára háskólann."+"\n\n"
        for char in print5:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(1)
        print6="Fyrsta stóra ákvörðunin sem þú þarft að hjálpa Hrólf með er í hvaða framhaldsskóla hann á að fara. Veldu skóla."
        for char in print6:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(1)
        print7= """
        A. Menntaskólann í Reykjavík
        B. Flensborgarskólann í Hafnarfirði
        C. Verzlunarskóla Íslands"""+"\n"
        for char in print7:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        harin = self.intro()
        return harin


    def intro(self):
        counter =0
        svar_A = ["A", "a"]
        svar_B = ["B", "b"]
        svar_C = ["C", "c"]
        Ja = ["J", "j", "já", "JÁ", "Já"]
        Nei = ["N", "n", "nei", "Nei", "NEI"]
        choice = None
        choice = input(">>> ") #Here is your first choice.
        if choice in svar_A:
            print8="\nJæja, þú ert ömurlegur ráðgjafi. Hrólfur missti allt hárið og féll úr MR á fyrstu önninni. Hann er samt mjög ánægður á dælunni.\n"
            for char in print8:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            return 100
        elif choice in svar_B:
            counter += self.option_Flens()
        elif choice in svar_C:
            counter += self.option_Verzl()
        else:
            while (choice not in svar_A and choice not in svar_B and choice not in svar_C):
                printabc = "\nA, B eða C takk fyrir\n\n"
                for char in printabc:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.01)
                time.sleep(1)
                choice = input(">>> ")
                if choice in svar_A:
                    print8="\nJæja, þú ert ömurlegur ráðgjafi. Hrólfur missti allt hárið og féll úr MR á fyrstu önninni.\n"
                    for char in print8:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    printMR ="\nHann er samt mjög ánægður á dælunni.\n"
                    for char in printMR:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    return 100
                elif choice in svar_B:
                    counter += self.option_Flens()
                elif choice in svar_C:
                    counter += self.option_Verzl()

        return counter

    def option_Flens(self):
        svar_A = ["A", "a"]
        svar_B = ["B", "b"]
        svar_C = ["C", "c"]
        Ja = ["J", "j", "já", "JÁ", "Já"]
        Nei = ["N", "n", "nei", "Nei", "NEI"]

        time.sleep(1)
        print9="\nHrólfur er mættur í Flensborg. Honum líður vel í Firðinum og rúllar upp náminu.\n"
        for char in print9:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        print10="Þrátt fyrir að vera heimakær hefur Hrólfur áhyggjur af að finna ekki spennandi kvenkost í Hafnarfirðinum.\n\n"
        for char in print10:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(1)
        print11="Þetta angrar hann ekki svakalega en samt nóg til að hann missi 4 hár af hausnum."+"\n\n"
        for char in print11:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        counter = 4
        time.sleep(1)
        print12="Hrólfur er mikill fótboltastrákur. Hann elskar fátt meira en að sparka í boltann með góðum félögum."+"\n\n"
        for char in print12:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(1)
        print13="Hrólfur er hinsvegar í erfiðri stöðu. Félagarnir eru ekki með jafn mikið metnað í boltanum. Hrólfur sjálfur gæti fengið að æfa með meistaraflokki FH í sumar."+"\n"
        print14="Hrólfur veit samt að það er mikið álag að vera í meistaraflokki."+"Ætti hann að eltast við draumana í FH eða ætti hann að fara með félögunum í Passion League?"+"\n"
        for char in print13:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(1)
        for char in print14:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(1)
        printfh = "    A. FH"
        printpl = "\n    B. Passion League "
        for char in printfh:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        for char in printpl:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(1)
        choice = input("\n>>> ")
        time.sleep(1)
        if choice in svar_A:
            print15="Þetta var slæm ákvörðun. Hrólf líður ekki vel í FH reynir í nokkra mánuði að æfa undir miklu álagi en hættir síðan. -10 hár"
            for char in print15:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            counter += 10
        elif choice in svar_B:
            print16 ="Geggjuð ákvörðun. Hrólfur skemmtir sér konunglega með félögunum í Passion League, einn stóran Tuborg takk."+"\n"
            for char in print16:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
        else:
            print ("A eða B koma svo\n")
            while choice not in svar_A and choice not in svar_B:
                print ("    A. FH")
                print("    B. Passion League")
                choice = input("\n>>> ")
                if choice in svar_A:
                    print15="Þetta var slæm ákvörðun.\n "
                    for char in print15:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    print15="Hrólf líður ekki vel í FH reynir í nokkra mánuði að æfa undir miklu álagi en hættir síðan. -10 hár"
                    for char in print15:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    counter += 10
                elif choice in svar_B:
                    print16 ="Geggjuð ákvörðun." +"\n"
                    for char in print16:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    print4f ="Hrólfur skemmtir sér konunglega með félögunum í Passion League, einn stóran Tuborg takk."+"\n"
                    for char in print4f:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
        print17= "Námið í Flensborg er að fara vel með Hrólf. Hann er samt að velta því fyrir sér hvort hann eigi að eltast við að vera Dúx."+"\n"
        for char in print17:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        print18="Það gæti gert eitthvað fyrir sjálfstraustið hans að vera dúx en það er auðvitað mikil vinna sem myndi fara í það"+"\n"
        print19="      A fyrir að eltast við að vera dúx" + "\n" "      B fyrir að útskrifast bara"+"\n"
        for char in print18:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        for char in print19:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(1)
        choice = input(">>> ")
        if choice in svar_A:
            print20="Ekki vera svona vitlaus, maður græðir ekkert á að vera Dúx, spurðu bara Erni Jónsson"+"\n"
            print21="-10 hár fyrir óþarfa metnað í námi"+"\n"
            for char in print20:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            for char in print21:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            counter += 10
        elif choice in svar_B:
            print22="Hrólfur nýtur sín vel í náminu þar sem hann var ekki að eltast við einkunnir.\n Hann lærir efnið vel og missir ekkert hár."+"\n"
            for char in print22:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
        else:
            print23="A eða B koma svo\n"
            for char in print23:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            while choice not in svar_A and choice not in svar_B:
                choice = input(">>> ")
                if choice in svar_A:
                    print20="Ekki vera svona heimskur, maður græðir ekkert á að vera Dúx, spurðu bara Erni Jónsson"+"\n"
                    print21="-10 hár fyrir óþarfa metnað í námi"
                    for char in print20:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    for char in print21:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    counter += 10
                elif choice in svar_B:
                    print22="Hrólfur nýtur sín vel í náminu þar sem hann var ekki að eltast við einkunnir. Hann lærir efnið vel og missir ekkert hár."+"\n"
                    for char in print22:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

        print24="Hrólfur útskrifaðist úr Flensborg og stefnir núna á Iðnaðarverkfræði við Háskóla Íslands\n"
        for char in print24:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)

        return counter



    def option_Verzl(self):
        counter=0
        svar_A = ["A", "a"]
        svar_B = ["B", "b"]
        svar_C = ["C", "c"]
        Ja = ["J", "j", "já", "JÁ", "Já"]
        Nei = ["N", "n", "nei", "Nei", "NEI"]

        time.sleep(1)
        print25="\nHrólfur er mættur í Verzló. Honum finnst félagslífið skemmtilegt en námið er erfitt."+"\n"
        print26="Snappið hans Hrólfs er ekki lengi að fyllast af skonsum eftir að hann byrjar í Verzló."+"\n"
        print27="Álagið við að svara öllum þessum skonsum lætur hann missa 10 hár af hausnum."+"\n\n"
        for char in print25:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        for char in print26:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        for char in print27:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        counter += 10
        time.sleep(1)
        print12="Hrólfur er mikill fótboltastrákur. Hann elskar fátt meira en að sparka í boltann með góðum félögum."+"\n\n"
        for char in print12:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(1)
        print13="Hrólfur er hinsvegar í erfiðri stöðu. Félagarnir eru ekki með jafn mikið metnað í boltanum. Hrólfur sjálfur gæti fengið að æfa með meistaraflokki FH í sumar."+"\n"
        print14="Hrólfur veit samt að það er mikið álag að vera í meistaraflokki."+" Ætti hann að eltast við draumana í FH eða ætti hann að fara með félögunum í Passion League?"+"\n"
        for char in print13:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(1)
        for char in print14:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(1)
        printfh = "    A. FH"
        printpl = "\n    B. Passion League "
        for char in printfh:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        for char in printpl:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(1)
        choice = input("\n>>> ")
        if choice in svar_A:
            print15="\nÞetta var slæm ákvörðun. Hrólf líður ekki vel í FH reynir í nokkra mánuði að æfa undir miklu álagi en hættir síðan. -10 hár.\n"
            for char in print15:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            counter += 10
        elif choice in svar_B:
            print16 ="\nGeggjuð ákvörðun. Hrólfur skemmtir sér konunglega með félögunum í Passion League, einn stóran Tuborg takk.\n"
            for char in print16:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
        else:
            while choice not in svar_A and choice not in svar_B:
                printabc = "A eða B koma svo\n"
                for char in printabc:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.01)
                choice = input("\n>>> ")
                if choice in svar_A:
                    print15="Þetta var slæm ákvörðun. Hrólf líður ekki vel í FH reynir í nokkra mánuði að æfa undir miklu álagi en hættir síðan. -10 hár"
                    for char in print15:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    counter += 10
                elif choice in svar_B:
                    print16 ="Geggjuð ákvörðun. Hrólfur skemmtir sér konunglega með félögunum í Passion League, einn stóran Tuborg takk."+"\n"
                    for char in print16:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
        print33="Námið í Verzló er erfitt fyrir Hrólf. Hann er að velta því fyrir sér hvort hann eigi að halda áfram eða hætta bara í skólanum."+"\n"
        print34="Hann gæti átt erfitt með að halda sér í Verzló en það gæti verið að hann flosni úr skóla ef hann fer í Flensborg"+"\n"
        print35="     A fyrir að halda áfram" + "\n"  "     B fyrir Flensborg" + "\n"
        for char in print33:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        for char in print34:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        for char in print35:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(1)
        choice = input(">>> ")
        if choice in svar_A:
            print36="Hrólfur tók sig á fyrir prófin og gekk mjög vel. Hann var alltaf vel undirbúinn og var því ekkert stressaður"+"\n"
            for char in print36:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
        elif choice in svar_B:
            print37 ="Hrólfur fílaði sig ekki alveg í Flensborg, flosnaði úr námi og fór aldrei í háskólann."+"\n"
            for char in print37:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            counter =100
            return counter
        else:
            print ("A eða B koma svo\n")
            while choice not in svar_A and choice not in svar_B:
                choice = input(">>> ")
                if choice in svar_A:
                    print36="Hrólfur tók sig á fyrir prófin og gekk mjög vel. Hann var alltaf vel undirbúinn og var því ekkert stressaður"+"\n"
                    for char in print36:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                elif choice in svar_B:
                    print37 ="Hrólfur fílaði sig ekki alveg í Flensborg, flosnaði úr námi og fór aldrei í háskólann."+"\n"
                    for char in print37:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    counter =100
                    return counter
        print38="Hrólfur útskrifaðist úr Verzlunarskólanum og stefnir núna á Iðnaðarverkfræði við Háskóla Íslands"+"\n"
        for char in print38:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        return counter


    def HaskoliStartintro(self):
        counter1=0
        svar_A = ["A", "a"]
        svar_B = ["B", "b"]
        print39="Nú er Hrólfur mættur í háskólann eftir fína framhaldsskólagöngu"+"\n"
        for char in print39:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(1)
        print40="Hrólfur fattar strax að hann eigi ekki efni á kaupa sér hádegismat alla daga"+"\n"
        for char in print40:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(1)
        print41="      A. Á Hrólfur að læra að gera sér nesti eða "+"\n"
        print42="      B. Finna sér kærustu til að gera nestið fyrir sig alla daga? "+"\n"
        for char in print41:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        for char in print42:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        counter1= self.HaskoliStart()
        return counter1

    def HaskoliStart(self):
        counter=0
        svar_A = ["A", "a"]
        svar_B = ["B", "b"]
        choice = input(">>> ")
        if choice in svar_A:
            counter += self.HaskoliA()
        elif choice in svar_B:
            counter += self.HaskoliB()
        else:
            while choice not in svar_A and choice not in svar_B:
                print("A eða B takk fyrir ")
                choice = input(">>> ")
                if choice in svar_A:
                    counter += self.HaskoliA()
                elif choice in svar_B:
                    counter += self.HaskoliB()
        return counter

    def HaskoliA(self):
        counter=0
        svar_A = ["A", "a"]
        svar_B = ["B", "b"]
        svar_C = ["C", "c"]
        Ja = ["J", "j", "já", "JÁ", "Já"]
        Nei = ["N", "n", "nei", "Nei", "NEI"]
        time.sleep(1)
        print43="Hrólfur lærði að gera nesti, hann missir hinsvegar smá svefn við að vakna alltaf til að gera nesti"+"\n"
        print44="Mínus 5 hár útaf svefnleysi"+"\n"
        for char in print43:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        for char in print44:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        counter += 5
        time.sleep(1)
        print45="Hrólf gengur vel í náminu á fyrstu önn, hann þarf að fara í eitt endurtektarpróf en pakkar því saman"+"\n"
        print46="Á annarri önninni trúðar Hrólfur oft yfir sig á djamminu."+"\n"
        for char in print45:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        for char in print46:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(1)
        print47="Á Hrólfur að hætta að drekka eins og T-Paul vinur hans? (já eða nei)"+"\n"
        for char in print47:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        choice1 = input(">>> ")
        if choice1 in Ja:
            print48="Slæm ákvörðun, þar sem Hrólfur getur ekki slakað á um helgar með félögunum og einn skíítkaldan missir hann 20 hár"
            for char in print48:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            counter += 20
        if choice1 in Nei:
            print49="Góð ákvörðun, þrátt fyrir að Hrólfur prjónaði stundum yfir sig þá getur hann slakað vel á um helgar með félögunum"+"\n"
            print50="Hann þarf samt oft að hafa áhyggjur eftir að hafa trúðað yfir sig og missir því 5 hár"+"\n"+"\n"
            for char in print49:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            for char in print50:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            counter += 5
        time.sleep(1)
        if choice1 in Ja:
            print51="Þrátt fyrir að vera hættur að drekka þá nær Hrólfur öllum prófunum á önn númer 2"+"\n"
            for char in print51:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
        if choice1 in Nei:
            print52="Hrólfur náði öllum prófunum og fagnaði proflokunum vel á b5"+"\n"
            for char in print52:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
        else:
            while choice1 not in Ja and choice1 not in Nei:
                print7000="Já eða nei takk fyrir."
                for char in print7000:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.01)
                choice1 = input(">>> ")
                if choice1 in Ja:
                    print48="Slæm ákvörðun, þar sem Hrólfur getur ekki slakað á um helgar með félögunum og einn skíítkaldan missir hann 20 hár"+"\n"
                    for char in print48:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    counter += 20
                if choice1 in Nei:
                    print49="Góð ákvörðun, þrátt fyrir að Hrólfur prjónaði stundum yfir sig þá getur hann slakað vel á um helgar með félögunum"+"\n"
                    print50="Hann þarf samt oft að hafa áhyggjur eftir að hafa trúðað yfir sig og missir því 5 hár"+"\n"+"\n"
                    for char in print49:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    for char in print50:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    counter += 5
                time.sleep(1)
                if choice1 in Ja:
                    print51="Þrátt fyrir að vera hættur að drekka þá nær Hrólfur öllum prófunum á önn númer 2"+"\n"
                    for char in print51:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                if choice1 in Nei:
                    print52="Hrólfur náði öllum prófunum og fagnaði proflokunum vel á b5"+"\n"
                    for char in print52:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

        print53="Á önn númer 3 fattar Hrólfur að hann þurfi að finna sér maka"+"\n"
        for char in print53:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(1)
        print54="Þrír einstaklingar reyna við hann, öll eru með frábæran hlátur en hvern á hann að velja?"+"\n"
        print55="      A. Hressa sveitastelpu sem hatar ekki sopann"+"\n"
        print56="      B. Verzló skvísu af nesinu"+"\n"
        print57="      C. Hávaxinn fótboltatöffara úr Hlíðunum"+"\n"
        for char in print54:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        for char in print55:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        for char in print56:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        for char in print57:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        choice2 = input(">>> ")
        time.sleep(1)
        if choice2 in svar_A:
            print58="Þið djammið mikið saman og skemmtið ykkur vel"+"\n"
            print59="Of mikið myndu sumir segja og hann missir 10 hár"+"\n"+"\n"
            for char in print58:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            for char in print59:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            counter += 10
        if choice2 in svar_B:
            print60="Einbeitingin hverfur smá frá náminu og það veldur einhverjum áhyggjum"+"\n"
            for char in print60:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            time.sleep(1)
            print61="Í staðinn fær Hrólfur að sofa aðeins lengur því nú fær hann nesti tilbúið af Nesinu"+"\n"
            print63="Þetta gengur vel en auðvitað eru einhverjir hnökkrar og Hrólfur missir samtals 5 hár"+"\n"
            for char in print61:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            for char in print63:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            counter += 5
        if choice2 in svar_B:
            print64="Þetta gengur vel en auðvitað eru einhverjir hnökkrar og Hrólfur missir samtals 5 hár"
            for char in print64:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            counter += 5
        if choice2 in svar_C:
            print66="Fótboltatöffararnir njóta sín vel. Það þarf oftar að skipta um kodda en áhyggjurnar á heimilinu er almennt litlar"+"\n"
            for char in print66:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
        else:
            print("A, B eða C takk fyrir")
            while choice2 not in svar_A and choice2 not in svar_B and choice2 not in svar_C:
                choice2 = input(">>> ")
                time.sleep(1)
                if choice2 in svar_A:
                    print58="Þið djammið mikið saman og skemmtið ykkur vel"+"\n"
                    print59="Of mikið myndu sumir segja og hann missir 10 hár"+"\n"
                    for char in print58:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    for char in print59:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    counter += 10
                if choice2 in svar_B:
                    print60="Einbeitingin hverfur smá frá náminu og það veldur einhverjum áhyggjum"+"\n"
                    for char in print60:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    time.sleep(1)
                    print61="Í staðinn fær Hrólfur að sofa aðeins lengur því nú fær hann nesti tilbúið af Nesinu"+"\n"
                    print63="Þetta gengur vel en auðvitað eru einhverjir hnökkrar og Hrólfur missir samtals 5 hár"+"\n"
                    for char in print61:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    for char in print63:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    counter += 5
                if choice2 in svar_C:
                    print66="Fótboltatöffararnir njóta sín vel. Það þarf oftar að skipta um kodda en áhyggjurnar á heimilinu er almennt litlar"+"\n"
                    for char in print66:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

        print67="Á önn númer þrjú eru 4 auðveldir áfangar sem Hrólfur þarf ekki að hafa neinar áhyggjur af"+"\n"
        for char in print67:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(1)
        print68="Hrólfur þarf samt líka að taka áfangann Verkefnastjórnun, áfanginn er gríðarlega erfiður og þarf mikla vinnu til að ná honum"+"\n"
        print89="Hvaða einkunn stefnir Hrólfur á að fá í áfanganum, því meiri vinnu sem hann leggur í áfangann því meira hár missir hann"+"\n"
        for char in print68:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        for char in print89:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        verk = None
        while verk is None:
            try:
                verk = int(input("láðu inn heiltölu á milli 5 og 10>>>"))
            except ValueError:
                verk = None
        counter += (verk-5)*5
        if verk > 7:
            print90="Það var stressandi að fá góða einkunn í verkefnastjórnun, Hrólfur missti 5 hár fyrir hverja einkunn sem hann fékk yfir 5"+"\n"
            for char in print90:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            time.sleep(1)
        else:
            print91="Góð ákvörðun að láta Hrólf ekki ofreyna sig í áfanganum. Hann missti bara 5 hár fyrir hvern heilan sem hann fékk yfir 5"+"\n"
            for char in print91:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            time.sleep(1)
        print91="Hrólfur fer hlægjandi í gegnum önn 4 og 5"+"\n"+"\n"
        for char in print91:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        print74="Fyrir seinustu önnina gerði Hrólfur stór mistök."+"\n"
        for char in print74:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        print75="Hann tók sömu valáfanga og Lexi"+"\n"
        for char in print75:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        print76="Nú er hann kominn í þá gríðarlega erfiðu stöðu að þurfa að ná þessum námskeiðum"+"\n"
        print77="Við það að reyna að ná þessum fáranlegu námskeiðum sem Lexi valdi missti Hrólfur 10 hár, vonandi átti hann efni á því"+"\n"+"\n"
        for char in print76:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        for char in print77:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        counter +=10
        return counter

    def HaskoliB(self):
        counter=0
        svar_A = ["A", "a"]
        svar_B = ["B", "b"]
        svar_C = ["C", "c"]
        Ja = ["J", "j", "já", "JÁ", "Já"]
        Nei = ["N", "n", "nei", "Nei", "NEI"]
        time.sleep(1)
        print78="Hrólfur er alltaf vel nærður og missir engin hár á fyrstu önninni"+"\n"
        for char in print78:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(1)
        print79="Hrólf gengur vel í náminu á fyrstu önn, hann þarf að fara í eitt endurtektarpróf en pakkar því saman"+"\n"
        for char in print79:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        print80="Á annarri önninni trúðar Hrólfur oft yfir sig á djamminu."+"\n"
        for char in print80:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(1)
        print47="Á Hrólfur að hætta að drekka eins og T-Paul vinur hans? (já eða nei)"
        for char in print47:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        choice1 = input(">>> ")
        if choice1 in Ja:
            print48="Slæm ákvörðun, þar sem Hrólfur getur ekki slakað á um helgar með félögunum og einn skíítkaldan missir hann 20 hár"+"\n"
            for char in print48:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            counter += 20
        if choice1 in Nei:
            print49="Góð ákvörðun, þrátt fyrir að Hrólfur prjónaði stundum yfir sig þá getur hann slakað vel á um helgar með félögunum"+"\n"
            print50="Hann þarf samt oft að hafa áhyggjur eftir að hafa trúðað yfir sig og missir því 5 hár"
            for char in print49:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            for char in print50:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            counter += 5
        time.sleep(1)
        if choice1 in Ja:
            print51="Þrátt fyrir að vera hættur að drekka þá nær Hrólfur öllum prófunum á önn númer 2"+"\n"
            for char in print51:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
        if choice1 in Nei:
            print52="Hrólfur náði öllum prófunum og fagnaði proflokunum vel á b5"+"\n"
            for char in print52:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
        else:
            while choice1 not in Ja and choice1 not in Nei:
                print7000="Já eða nei takk fyrir."
                for char in print7000:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.01)
                choice1 = input(">>> ")
                if choice1 in Ja:
                    print48="Slæm ákvörðun, þar sem Hrólfur getur ekki slakað á um helgar með félögunum og einn skíítkaldan missir hann 20 hár"
                    for char in print48:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    counter += 20
                if choice1 in Nei:
                    print49="Góð ákvörðun, þrátt fyrir að Hrólfur prjónaði stundum yfir sig þá getur hann slakað vel á um helgar með félögunum"+"\n"
                    print50="Hann þarf samt oft að hafa áhyggjur eftir að hafa trúðað yfir sig og missir því 5 hár"+"\n"
                    for char in print49:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    for char in print50:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    counter += 5
                time.sleep(1)
                if choice1 in Ja:
                    print51="Þrátt fyrir að vera hættur að drekka þá nær Hrólfur öllum prófunum á önn númer 2"+"\n"
                    for char in print51:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                if choice1 in Nei:
                    print52="Hrólfur náði öllum prófunum og fagnaði proflokunum vel á b5"+"\n"
                    for char in print52:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

        print87="Á önn númer 3 eru 4 auðveldir áfangar sem Hrólfur þarf ekki að hafa neinar áhyggjur af"+"\n"
        for char in print87:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(1)
        print88="Hrólfur þarf samt líka að taka áfangann Verkefnastjórnun, áfanginn er gríðarlega erfiður og þarf mikla vinnu til að ná honum"+"\n"
        for char in print88:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        print89="Hvaða einkunn stefnir Hrólfur á að fá í áfanganum, því meiri vinnu sem hann leggur í áfangann því meira hár missir hann"+"\n"
        for char in print89:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        verk = int(input("Sláðu inn heiltölu á milli 5 og 10>>>"))
        counter += (verk-5)*5
        if verk > 7:
            print90="Það var stressandi að fá góða einkunn í verkefnastjórnun, Hrólfur missti 4 hár fyrir hverja einkunn sem hann fékk yfir 5"+"\n"
            for char in print90:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            time.sleep(1)
        else:
            print91="Góð ákvörðun að láta Hrólf ekki ofreyna sig í áfanganum. Hann missti bara 4 hár fyrir hvern heilan sem hann fékk yfir 5"+"\n"
            for char in print91:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            time.sleep(1)
        print91="Hrólfur fer hlægjandi í gegnum önn 4 og 5"+"\n"
        for char in print91:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(2)
        print91="Fyrir seinustu önnina gerði Hrólfur stór mistök."+"\n"
        print92="Hann tók sömu valáfanga og Lexi"+"\n"
        print93="Nú er hann kominn í þá gríðarlega erfiðu stöðu að þurfa að ná þessum námskeiðum"+"\n"
        print94="Við það að reyna að ná þessum fáranlegu námskeiðum sem Lexi valdi missti Hrólfur 10 hár, vonandi átti hann efni á því"+"\n"
        for char in print91:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        print("\n")
        for char in print92:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        print("\n")
        for char in print93:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        print("\n")
        for char in print94:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        counter +=10
        return counter


    def Nidurstada(self, x):
        if x>50:
            print95="\nNú er Hrólfur búinn með skólann.\n"
            for char in print95:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            time.sleep(1)
            print96="\nHann endaði með "+str(x)+" hár eftir á kollinum.\n"
            for char in print96:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            time.sleep(1)
            print97="\nÞar sem Hrólfur átti meira en 50 hár eftir á hausnum þá hafði hann nóg sjálfstraust til að klára dæmið og útskrifaðist."+"\n\n"
            for char in print97:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            time.sleep(1)
            return 1
        if x <= 50:
            print96="\nHann endaði með "+str(x)+" hár eftir á kollinum.\n"
            for char in print96:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            time.sleep(1)

            print98="\nÞar sem Hrólfur missti of mikið hár gat hann ekki náð að klára dæmið, þú náðir ekki að útskrifa Hrólf.\n\n"
            for char in print98:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            time.sleep(1)
            return 0

def main():
    print("\n" * get_terminal_size().lines, end='')
    kall = Hrolfur()
    har = 100
    har -= kall.intro1()
    if har>20:
        har -= kall.HaskoliStartintro()
    kall.Nidurstada(har)

if __name__ == "__main__":
    main()
