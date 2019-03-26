# This Python file uses the following encoding: utf-8
import math
import random
import time #Importum module til að að hafa smá biðtíma milli spurninga
import sys

def get_input(output):
    return input(output)

def stor(spurning):
    tala = int(get_input(spurning))
    if tala >= 10:
        return 100
    else:
        return 50


class Aron:

    afangar = ["s", "l", "e"]
    skolar =["vi", "ví", "mr", "hr", "ms", "vma"]



    def __init__(self):
        pass

# Fall til að velja fyrsta endurtektarprófið

    time.sleep(1)
    def Velja1(self):
        namskeid1 = None
        Byrjun = "Jæja komið að Aroni!\n"
        for char in Byrjun:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
        time.sleep(1)
        Inngangur = "\nÞú féllst í þremur lokaprófum á fyrstu önninni þinni. Nú verður þú að velja tvö námskeið til að taka í endurtekt. Byrjaðu á að velja fyrsta."
        for char in Inngangur:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)

        while namskeid1 not in self.afangar:
            time.sleep(1)
            valmoguleiki1 = '\n\nS fyrir Stærðfræðigreiningu, L fyrir Línulega Algebru eða E fyrir Eðlisfræði: '
            for char in valmoguleiki1:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.050)
            namskeid1 = input("").lower()
            namskeid1 = namskeid1.lower()
            if namskeid1 in self.afangar:
                return namskeid1
            else:
                time.sleep(1)
                urskeidis1 = "Það fór eitthvað úrskeiðis hjá þér reyndu aftur að velja námskeið"
                for char in urskeidis1:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(.050)
                namskeid1 = None

# Fall til að velja seinna endurtektarprófið

    time.sleep(1)
    def Velja2(self, namskeid1):
        time.sleep(1)
        annad = "\nNú ertu búinn að velja eitt námskeið til að taka í endurtekt, veldu seinna.\n"
        for char in annad:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
        # Það er ekki hægt að velja sama endurtektarprófið tvisvar
        namskeid2 = None
        while namskeid2 not in self.afangar:

            if namskeid1.lower() =='s':
                time.sleep(1)
                valmoguleiki2 = '\nL fyrir Línulega Algebru eða E fyrir Eðlisfræði: '
                for char in valmoguleiki2:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(.050)
                namskeid2= input("")
            elif namskeid1.lower() =='l':
                time.sleep(1)
                valmoguleiki3 = '\nS fyrir Stærðfræði greiningu eða E fyrir Eðlisfræði: '
                for char in valmoguleiki3:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(.050)
                namskeid2 = input("")
            elif namskeid1.lower() =='e':
                time.sleep(1)
                valmoguleiki4 = '\nS fyrir Stærðfræði greiningu eða L fyrir Línulega Algebru: '
                for char in valmoguleiki4:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(.050)
                namskeid2 = input("")

            if namskeid2 in self.afangar:
                return namskeid2
            else:
                time.sleep(1)
                urskeidis2 = '\nÞað fór eitthvað úrskeiðis hjá þér reyndu aftur að velja námskeið'
                for char in urskeidis2:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(.050)
                namskeid2 = None

# Fall sem er endurtektarpróf í Stærðfræðigreiningu 1

    def S1Prof(self):
        time.sleep(1)
        # Skilgreini þessar breytur sem núll til að geta notað þær seinna í forritinu
        StadFall =0
        einkunn =0
        TM =0
        Inngangur2 = "\nÞú ert að læra fyrir endurtektarpróf í Stærðfræðigreiningu. Þú hefur ekki mikinn tíma þar sem þú ert haugur. Þú verður að velja hvort þú viljir læra diffrun eða heildun fyrir prófið."
        for char in Inngangur2:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
        time.sleep(1)
        #Maður lærir hvort maður eyði tímanum sínum í að læra diffrun eða heildun, það er 50/50 hvort kemur.
        dh = None
        while dh != "d" and dh != "h":
            diffhei = '\n\nDiffrun = D eða Heildun = H: '
            for char in diffhei:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.050)
            dh= input("")
            dh = dh.lower()
        #Hérna fær maður að velja hversu mikið maður ætlar að sofa fyrir prófið, það fer eftir hvernig próf kennarinn gerir hvort það gagnist manni að sofa mikið
        time.sleep(1)
        svefn = 0
        while svefn <0.01:
            svefninn = "\nÞú ert illa undirbúinn en veist að svefn getur gert gott fyrir þig, hvað ætlar þú að sofa mikið nóttinni fyrir prófið? "
            for char in svefninn:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.050)
            svefn = int(input(""))
        #Til þess að maður græði eitthvað á að læra fram eftir þá nær maður að læra um Taylor margliður ef maður lærir frameftir
        if svefn<4.5:
            time.sleep(1)
            Taylor = "\nÞú fórst svo seint að sofa að þú hafðir tíma til að læra Taylor margliður, vonandi koma þær á prófinu."
            for char in Taylor:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.050)
            TM =1
        # 50/50 hvort það komi diffrun eða heildun, spurningin sem kemur verður 20% af prófinu
        DH=random.randint(0,1)
        time.sleep(1)
        if DH==1:
            time.sleep(1)
            Diffrun = '\n\nNú ertu mættur í prófið, fyrsta spurningin er um Diffrun.'
            for char in Diffrun:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.050)
            if dh.lower() == 'd':
                time.sleep(1)
                Diffrunkom = '\n\nÞú ert heppinn, þú lærðir diffrun og hún kom á prófinu, einkunin þín hækkar um 2.'
                for char in Diffrunkom:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(.050)
                einkunn = einkunn +2
            elif dh.lower() == 'h':
                time.sleep(1)
                Lekkidiff = "\n\nÞú valdir vitlaust, þú lærðir ekki diffrun og hún var 20% af prófinu, þú getur í mesta lagi fengið 8."
                for char in Lekkidiff:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(.050)
            else:
                time.sleep(1)
                Vitlaustval = "\n\nÞar sem þú valdir þú hvorugt áðan varst þú jafn týndur þegar þessi spurning kom og VD á B5."
                for char in Vitlaustval:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(.050)

        if DH==0:
            time.sleep(1)
            Mprof = '\n\nNú ertu mættur í prófið, fyrsta spurningin er um heildun.'
            for char in Mprof:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.050)
            if dh.lower() == 'h':
                time.sleep(1)
                Ldiffh = '\n\nÞú ert heppinn, þú lærðir heildun og hún kom á prófinu, einkunin þín hækkar um 2.'
                for char in Ldiffh:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(.050)
                einkunn = einkunn +2
            if dh.lower() == 'd':
                time.sleep(1)
                Vval = "\n\nÞú valdir vitlaust, þú lærðir ekki heildun og hún var 20% af prófinu, þú getur í mesta lagi fengið 8."
                for char in Vval:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(.050)
            else:
                time.sleep(1)
                Hvorugt = "\n\nÞar sem þú valdir þú hvorugt áðan varst þú jafn týndur þegar þessi spurning kom og VD á B5."
                for char in Hvorugt:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(.050)
        # 50/50 hvort Taylor margliður komi á prófinu. Ef maður lærði frameftir nær maður spurningunni rétt annars fær maður 0 stig.
        if random.randint(0,1)==1:
            time.sleep(1)
            Tkom = '\n\nTaylor margliður komu á prófinu.'
            for char in Tkom:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.050)
            if TM == 0:
                time.sleep(1)
                Vleng = '\n\nÞú hefðir kannski átt að vaka lengur til að læra Taylor margliður, þær voru 20% af prófinu.'
                for char in Vleng:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(.050)
            if TM == 1:
                time.sleep(1)
                print1 = '\n\nVel gert að læra Taylor margliður, þú varst að ná auka 2 heilum á prófinu.'
                for char in print1:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(.050)
                einkunn=einkunn + 2
        else:
            time.sleep(1)
            print2 = '\n\nTaylor margliður komu ekki. Það kom fáranlegt markgildisdæmi sem þú áttir aldrei séns í. Óheppinn.'
            for char in print2:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.050)
            einkunn=einkunn + 2
        # Já eða nei spurning um hvort fall sé samfell
        # Gætum bætt við mynd af falli í næsta sprett til að hafa smá raunverulega stærðfræðigreiningu í þessu
        time.sleep(1)
        print3 = '\n\n20% spurning hvort að fall sé samfellt á ákveðnu bili, Er það ekki bara já og nei spurning, eða 50/50...'
        for char in print3:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
        einkunn=einkunn + 2
        svar = None
        while svar != "j" and svar != "n":
            time.sleep(1)
            print4 = '\n\nEr fallið samfellt eða ekki? J fyrir Já, N fyrir nei: '
            for char in print4:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.050)
            einkunn=einkunn + 2
            svar = input("")
            svar = svar.lower()
        if random.randint(0,1)==1:
            rsvar = 'j'
            time.sleep(1)
            if svar.lower() == rsvar:
                time.sleep(1)
                print5 = "\nVel gert, þú giskaðir rétt! Útskýringin þín var samt ekki nægilega góð svo þú færð bara helmingin af dæminu rétt."
                for char in print5:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(.050)
                einkunn = einkunn + 1
            else:
                time.sleep(1)
                print6 = 'Þú giskaðir vitlaust og kunnir ekki nóg um efnið til að búa þér til stig.'
                for char in print6:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(.050)
        else:
            rsvar= 'n'
            if svar.lower() == rsvar:
                time.sleep(1)
                print7 = '\n\nVel gert, þú giskaðir rétt. Útskýringin þín var samt ekki nægilega góð svo þú færð bara helmingin af dæminu rétt.'
                for char in print7:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(.050)
                einkunn = einkunn + 1
            else:
                time.sleep(1)
                print8 = '\n\nÞú giskaðir vitlaust og kunnir ekki nóg um efnið til að búa þér til stig.'
                for char in print8:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(.050)
        # Hérna á að svara með tölustafnum 1
        time.sleep(1)
        print9 = '\n\nEinfalt einingahringsdæmi, sem gildir 10%. Wu-hu.'
        for char in print9:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
        SvarImba = 1
        time.sleep(1)
        print10 = '\n\ncos^2(theta)+sin^2(theta)=x. Hvað er x? '
        for char in print10:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
        Imba=int(input(""))
        if Imba==SvarImba:
            time.sleep(1)
            print11 = '\nVar þetta gisk? Það breytir engu, þetta var allavega rétt.'
            for char in print11:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.050)
            einkunn=einkunn+1
        else:
            time.sleep(1)
            print12 = '\n\nSvona á að vita, þarna misstir þú dýrmætt stig úr pokanum.'
            for char in print12:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.050)

        # Hérna kemur svefninn inn. Ef maður fékk nægan svefn nær maður flóknu dæmi. Það er tilviljanakennt hversu mikinn svefn maður þarf.
        svefnkrafa = random.randint(0,9)
        if svefnkrafa >svefn:
            time.sleep(1)
            print13 = "\n\nÞú hefðir átt að sofa meira. Benni kennari henti í svæsið 20% dæmi sem þú fattaðir ekki hvernig á að leysa."
            for char in print13:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.050)
        if svefn >= svefnkrafa:
            einkunn= einkunn+2
            time.sleep(1)
            print14 = '\n\nVel gert, þú varst vel sofinn og fattaðir trixið í svæsnu 20% dæmi frá Benna.'
            for char in print14:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.050)
        # Það stendur á hverri blaðsíðu á EdBook quote eftir Douglas Adams
        time.sleep(1)
        print15 = '\n\nÞetta er nú fáranleg 10% spurning. Hver er uppáhalds rithöfundurinn hans Benna kennara?'
        for char in print15:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)

        print15 = '\n\nA George R.R. Martin\n'
        print16 = 'B Douglas Adams\n'
        print17 = 'C Yrsa Sigurðardóttir\n'
        for char in print15:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
            time.sleep(1)
        for char in print16:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
        for char in print17:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
            time.sleep(1)
        skrifa = None
        while skrifa != "a" and skrifa != "b" and skrifa != "c":
            time.sleep(1)
            print18 = '\nA, B eða C? '
            for char in print18:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.050)
            skrifa=input("")
            skrifa = skrifa.lower()
        if skrifa.lower() == 'b':
            time.sleep(1)
            einkunn= einkunn +1
            time.sleep(1)
            print19 = '\nÞú varst augljóslega duglegur að lesa EdBook yfir önnina.'
            for char in print19:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.050)
        else:
            time.sleep(1)
            print20 = '\nÞað þarf að lesa EdBook til að ná svona prófum.'
            for char in print20:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.050)
        #Prentum í lokin út lokaeinkunn og hvort viðkomandi hafi náð prófinu eða ekki
        time.sleep(1)
        print21 = '\n\nÞú fékkst '+ str(einkunn) +' á prófinu.'
        for char in print21:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
        if einkunn>4:
            time.sleep(1)
            print22 = '\n\nVel gert að ná prófinu, þú færð 6 einingar.\n'
            for char in print21:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.050)
            StadFall=1
        if einkunn<5:
            time.sleep(1)
            print23 = '\n\nÞú náðir ekki prófinu og ert kominn ennþá meira aftur úr í náminu.'
            for char in print23:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.050)
        return StadFall

# Fall sem er endurtektarpróf í Línulegri algebru

    #Setja mögulega 3 gæsa til að laga
    def Lprof(self):
        #Skilgreini þessar breytur hér til að geta notað þær seinna í forritinu
        StadFall =0
        einkunn =0
        EG =0
        # Þú velur hvort þú lærir og síðan er 50/50 hvort kemur á prófinu sem 20% spurning
        print('Þú ert að læra fyrir endurtektarpróf í Línulegri algebru. Þú hefur ekki mikinn tíma þar sem þú varst upptekinn í boltanum.\n'
        'Þú verður að velja hvort þú viljir læra Gauss eyðingu eða Fylkja margföldun.\n')
        time.sleep(1)
        gf = None
        while gf != "g" and gf != "f":
            gf= input('Gauss eyðingu = G eða Fylka margföldun = F: ')
            gf= gf.lower()
        #Hérna fær maður að velja hversu mikið maður ætlar að sofa fyrir prófið, það fer eftir hvernig próf kennarinn gerir hvort það gagnist manni að sofa mikið
        time.sleep(1)
        svefn = 0
        while svefn <0.01:
            svefn = int(input("\nÞú ert illa undirbúinn en veist að svefn getur"
            " gert gott fyrir þig, hvað ætlar þú að sofa mikið nóttinni fyrir prófið? "))# Maður verður að græða eitthvað á að læra frameftir. Í þessu tilfelli er það að geta leyst dæmi með eigin gildum
        if svefn<4.5:
            time.sleep(1)
            print('\nÞú fórst svo seint að sofa að þú hafðir tíma til að læra um Eigin gildi, vonandi kemur það á prófinu.\n')
            EG =1
        # Hér er valið tilviljanakennt hvort gauss eyðing eða fylkja margföldun komi á prófinu
        GF=random.randint(0,1)
        if GF==1:
            time.sleep(1)
            print('Nú ertu mættur í prófið, fyrsta spurningin er um Gauss eyðingu.')
            if gf.lower() == 'f':
                time.sleep(1)
                print('Þú ert heppinn, þú lærðir Gauss eyðingu og hún kom á prófinu, einkunin þín hækkar um 2')
                einkunn = einkunn +2
            if gf.lower() == 'g':
                time.sleep(1)
                print('Þú valdir vitlaust, þú lærðir ekki Gauss eyðingu og hún var 20% af prófinu, þú getur í mesta lagi fengið 8.')
        if GF==0:
            time.sleep(1)
            print('Nú ertu mættur í prófið, fyrsta spurningin er um fylkja margföldun.')
            if gf.lower() == 'g':
                print('Þú ert heppinn, þú lærðir fylkja margföldun og hún kom á prófinu, einkunin þín hækkar um 2')
                einkunn = einkunn +2
            if gf.lower() == 'f':
                print('Þú valdir vitlaust, þú lærðir ekki fylkja margföldun og hún var 20% af prófinu, þú getur í mesta lagi fengið 8.')
        # Hérna er valið tilviljanakennt hvort eigin gildi sem sumir lærðu komi á prófinu
        # Ef maður lærði um eigin gildin fær maður +2 í einkunn
        if random.randint(0,1)==1:
            print('Eigin gildi komu á prófinu')
            time.sleep(1)
            if EG == 0:
                print('Þú hefðir kannski átt að vaka lengur til að læra Eigin gildi, þær voru 20% af prófinu')
            if EG == 1:
                print('Vel gert að læra Eigin gildi, þú varst að ná auka 2 heilum á prófinu')
                einkunn=einkunn + 2
        else:
            print('Þarna varstu óheppinn í staðinn fyrir eigin gildis dæmi komu 20% skilgreiningar sem þú bullaðir eitthvað í.')
            print('Röggi Möll sá í gegnum bullið þitt og gaf þér 0 stig fyrir dæmið')
        print('20% spurning hvort að fall sé línulegt')
        time.sleep(1)
        print('Er það ekki bara já og nei spurning, eða 50/50')
        # Hérna er 50/50 spurning hvort fallið sé línulegt
        # Gætum bætt við mynd af falli í næsta sprett til að hafa smá raunverulega línulega algebru í þessu
        svar = None
        while svar != "j" and svar != "j":
            svar = input('Er fallið línulegt eða ekki? J fyrir Já, N fyrir nei: ')
            svar = svar.lower()
        if random.randint(0,1)==0:
            rsvar = 'j'
            if svar == rsvar:
                print('Vel gert, þú giskaðir rétt')
                print('Útskýringin þín var samt ekki nægilega góð svo þú færð bara helmingin af dæminu rétt')
                einkunn = einkunn + 1
            else:
                print('Þú giskaðir vitlaust og kunnir ekki nóg um efnið til að búa þér til stig')
        else:
            rsvar = 'n'
            if svar == rsvar:
                print('Vel gert, þú giskaðir rétt')
                print('Útskýringin þín var samt ekki nægilega góð svo þú færð bara helmingin af dæminu rétt')
                einkunn = einkunn + 1
            else:
                print('Þú giskaðir vitlaust og kunnir ekki nóg um efnið til að búa þér til stig')
        print('Einföld spurning, sem gildir 10%. Wu-hu.')
        #Hérna á að svara með Ákveða
        akveda=input('Hvað kallast Det(A) á Íslensku?')
        if akveda=='Ákveða' or akveda=='ákveða' or akveda=='Akveda' or akveda=='akveda':
            print('Var þetta gisk? Það breytir engu, þetta var allavega rétt')
            einkunn=einkunn+1
        else:
            print('Svona á að vita, þarna misstir þú dýrmætt stig úr pokanum')
        # Hérna kemur svefninn inn. Ef maður fékk nægan svefn nær maður flóknu dæmi. Það er tilviljanakennt hversu mikinn svefn maður þarf.
        svefnkrafa = random.randint(0,9)
        if svefnkrafa >svefn:
            print('Þú hefðir átt að sofa meira. Röggi Möll henti í svæsið 20% dæmi sem þú fattaðir ekki hvernig á að leysa.')
        if svefn >= svefnkrafa:
            einkunn= einkunn+2
            print('Vel gert, þú varst vel sofinn og fattaðir trixið í svæsnu 20% dæmi frá Rögga')
        #Þórður bróðir Rögnvalds kenndi okkur í Verzlunarskólanum svo okkur fannst tilvalið að hafa spurningu um hann
        print('Þetta er nú fáranleg spurning 10% spurning')
        print('Í hvaða framhaldsskóla kennir Þórður bróðir Rögnvalds stærðfræði?')
        print('Verzunarskóla Íslands')
        print('Menntaskólanum í Reykjavík')
        print('Leikskólanum í Skeifunni')
        print('Verkmenntaskólanum á Akureyri')
        print('Trúðaskólanum í Nauthólsvík')
        skrifa = None
        while skrifa not in self.skolar:
            skrifa=str(input('VÍ, MR, MS, VMA eða HR?'))
            skrifa = skrifa.lower()
        if skrifa.lower() == "ví" or skrifa.lower() == "vi":
            einkunn= einkunn +1
            time.sleep(1)
            print('Vel gert. Þú veist að bræðurnir Möller myndu alltaf bara kenna í bestu menntastofnunum landsins')
        else:
            time.sleep(1)
            print('Ekki nógu gott, þú hefðir átt að vita að bræðurnir Möller myndu alltaf bara kenna í bestu menntastofnunum landsins.')
            print('Verzló er rétt svar')
        #Hérna prentast síðan niðurstöðurnar úr prófinu
        print('Þú fékkst '+ str(einkunn) +'á prófinu')
        if einkunn>4:
            time.sleep(1)
            print('Vel gert að ná prófinu, þú færð 6 einingar')
            StadFall=1
        if einkunn<5:
            time.sleep(1)
            print('Þú náðir ekki prófinu og ert kominn ennþá meira aftur úr í náminu')
        return StadFall
        #Setja mögulega 3 gæsa til að laga

#_main_
#Einingarnar byrja sem núll en ef maður nær tveimur prófum maður 12 einingar
def main():
    #Kallið
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

if __name__ == "__main__":
    main()
