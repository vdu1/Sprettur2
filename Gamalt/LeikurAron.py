# This Python file uses the following encoding: utf-8
import math
import random
import time #Importum module til að að hafa smá biðtíma milli spurninga

class Aron:

    def __init__(self):
        pass

    # Fall til að velja fyrsta endurtektarprófið
    time.sleep(1)
    def Velja1(self):
        time.sleep(1)
        print('\nÞú féllst í þremur lokaprófum á fyrstu önninni þinni.\n'
        'Nú verður þú að velja tvö námskeið til að taka í endurtekt.')
        time.sleep(1)
        namskeid1 = str(input('\nS fyrir Stærðfræði greiningu, L fyrir Línulega Algebru eða E fyrir Eðlisfræði: '))
        return namskeid1

    # Fall til að velja seinna endurtektarprófið
    time.sleep(1)
    def Velja2(namskeid1):
        time.sleep(1)
        print('\nNú ertu búinn að velja eitt námskeið til að taka í endurtekt, próftaflan er heppileg svo þú getur tekið eitt endurtektarpróf í viðbót.\n')
        # Það er ekki hægt að velja sama endurtektarprófið tvisvar
        if namskeid1=='S':
            namskeid2= str(input('L fyrir Línulega Algebru eða E fyrir Eðlisfræði: '))
        elif namskeid1=='L':
            namskeid2= str(input('S fyrir Stærðfræði greiningu eða E fyrir Eðlisfræði: '))
        elif namskeid1=='E':
            namskeid2=str(input('S fyrir Stærðfræði greiningu eða L fyrir Línulega Algebru: '))
        else:
            print('Þú náðir ekki einu sinni að velja námskeiðin rétt, þú ert fallinn úr skólanum á fyrstu önn')
            end()
        return namskeid2
    # Fall sem er endurtektarpróf í Stærðfræðigreiningu 1
    time.sleep(1)
    def S1Prof():
        time.sleep(1)
        # Skilgreini þessar breytur sem núll til að geta notað þær seinna í forritinu
        StadFall =0
        einkunn =0
        TM =0
        print('\nÞú ert að læra fyrir endurtektarpróf í Stærðfræðigreiningu. Þú hefur ekki mikinn tíma þar sem þú ert haugur.\n'
        'Þú verður að velja hvort þú viljir læra diffrun eða heildun fyrir prófið.\n')
        time.sleep(1)
        #Maður lærir hvort maður eyði tímanum sínum í að læra diffrun eða heildun, það er 50/50 hvort kemur.
        dh= str(input('Diffrun = D eða Heildun = H: '))
        #Hérna fær maður að velja hversu mikið maður ætlar að sofa fyrir prófið, það fer eftir hvernig próf kennarinn gerir hvort það gagnist manni að sofa mikið
        time.sleep(1)
        svefn = int(input('\nÞú ert illa undirbúinn en veist að svefn getur gert gott fyrir þig, hvað ætlar þú að sofa mikið nóttinni fyrir prófið? '))
        #Til þess að maður græði eitthvað á að læra fram eftir þá nær maður að læra um Taylor margliður ef maður lærir frameftir
        if svefn<4.5:
            print('Þú fórst svo seint að sofa að þú hafðir tíma til að læra Taylor margliður, vonandi kemur það á prófinu')
            TM =1
        # 50/50 hvort það komi diffrun eða heildun, spurningin sem kemur verður 20% af prófinu
        DH=random.randint(0,1)
        time.sleep(1)
        if DH==1:
            time.sleep(1)
            print('\nNú ertu mættur í prófið, fyrsta spurningin er um Diffrun.\n')
            if dh == 'D':
                time.sleep(1)
                print('Þú ert heppinn, þú lærðir diffrun og hún kom á prófinu, einkunin þín hækkar um 2')
                einkunn = einkunn +2
            if dh == 'H':
                time.sleep(1)
                print('\nÞú valdir vitlaust, þú lærðir ekki diffrun og hún var 20% af prófinu, þú getur í mesta lagi fengið 8.\n')
        if DH==0:
            time.sleep(1)
            print('Nú ertu mættur í prófið, fyrsta spurningin er um heildun.')
            if dh == 'H':
                time.sleep(1)
                print('Þú ert heppinn, þú lærðir heildun og hún kom á prófinu, einkunin þín hækkar um 2')
                einkunn = einkunn +2
            if dh == 'D':
                time.sleep(1)
                print('Þú valdir vitlaust, þú lærðir ekki heildun og hún var 20% af prófinu, þú getur í mesta lagi fengið 8.')
        # 50/50 hvort Taylor margliður komi á prófinu. Ef maður lærði frameftir nær maður spurningunni rétt annars fær maður 0 stig.
        if random.randint(0,1)==1:
            time.sleep(1)
            print('\nTaylor margliður komu á prófinu.\n')
            if TM == 0:
                time.sleep(1)
                print('Þú hefðir kannski átt að vaka lengur til að læra Taylor margliður, þær voru 20% af prófinu.\n')
            if TM == 1:
                print('Vel gert að læra Taylor margliður, þú varst að ná auka 2 heilum á prófinu')
                einkunn=einkunn + 2
        else:
            print('Taylor margliður komu ekki. Það kom fáranlegt markgildisdæmi sem þú áttir aldrei séns í. Óheppinn.')
        # Já eða nei spurning um hvort fall sé samfell
        # Gætum bætt við mynd af falli í næsta sprett til að hafa smá raunverulega stærðfræðigreiningu í þessu
        print('20% spurning hvort að fall sé samfellt á ákveðnu bili\n'
        'Er það ekki bara já og nei spurning, eða 50/50')
        svar = str(input('Er fallið samfellt eða ekki? J fyrir Já, N fyrir nei: '))
        if random.randint(0,1)==1:
            rsvar= 'J'
            if svar == rsvar:
                print('Vel gert, þú giskaðir rétt')
                print('Útskýringin þín var samt ekki nægilega góð svo þú færð bara helmingin af dæminu rétt')
                einkunn = einkunn + 1
            else:
                print('Þú giskaðir vitlaust og kunnir ekki nóg um efnið til að búa þér til stig')
        else:
            rsvar= 'N'
            if svar == rsvar:
                print('Vel gert, þú giskaðir rétt')
                print('Útskýringin þín var samt ekki nægilega góð svo þú færð bara helmingin af dæminu rétt')
                einkunn = einkunn + 1
            else:
                print('Þú giskaðir vitlaust og kunnir ekki nóg um efnið til að búa þér til stig')
        # Hérna á að svara með tölustafnum 1
        print('Einfalt einingahringsdæmi, sem gildir 10%. Wu-hu.')
        SvarImba = 1
        Imba=int(input('cos^2(theta)+sin^2(theta)=x. Hvað er x?'))
        if Imba==SvarImba:
            print('Var þetta gisk? Það breytir engu, þetta var allavega rétt')
            einkunn=einkunn+1
        else:
            print('Svona á að vita, þarna misstir þú dýrmætt stig úr pokanum')
        # Hérna kemur svefninn inn. Ef maður fékk nægan svefn nær maður flóknu dæmi. Það er tilviljanakennt hversu mikinn svefn maður þarf.
        svefnkrafa = random.randint(0,9)
        if svefnkrafa >svefn:
            print('Þú hefðir átt að sofa meira. Benni kennari henti í svæsið 20% dæmi sem þú fattaðir ekki hvernig á að leysa.')
        if svefn >= svefnkrafa:
            einkunn= einkunn+2
            print('Vel gert, þú varst vel sofinn og fattaðir trixið í svæsnu 20% dæmi frá Benna')
        # Það stendur á hverri blaðsíðu á EdBook quote eftir Douglas Adams
        print('Þetta er nú fáranleg 10% spurning')
        print('Hver er uppáhalds rithöfundurinn hans Benna kennara?')
        print('A George R.R. Martin')
        print('B Douglas Adams')
        print('eða C Yrsa Sigurðardóttir')
        skrifa=str(input('A, B eða C?'))
        if skrifa == 'B':
            einkunn= einkunn +1
            print('Þú varst augljóslega duglegur að lesa EdBook yfir önnina')
        else:
            print('Það þarf að lesa EdBook til að ná svona prófum')
        #Prentum í lokin út lokaeinkunn og hvort viðkomandi hafi náð prófinu eða ekki
        print('Þú fékkst '+ str(einkunn) +'á prófinu')
        if einkunn>4:
            print('Vel gert að ná prófinu, þú færð 6 einingar')
            StadFall=1
        if einkunn<5:
            print('Þú náðir ekki prófinu og ert kominn ennþá meira aftur úr í náminu')
        return StadFall
    # Fall sem er endurtektarpróf í Línulegri algebru
    def Lprof():
        #Skilgreini þessar breytur hér til að geta notað þær seinna í forritinu
        StadFall =0
        einkunn =0
        EG =0
        # Þú velur hvort þú lærir og síðan er 50/50 hvort kemur á prófinu sem 20% spurning
        print('Þú ert að læra fyrir endurtektarpróf í Línulegri algebru. Þú hefur ekki mikinn tíma þar sem þú varst upptekinn í boltanum.')
        print('Þú verður að velja hvort þú viljir læra Gauss eyðingu eða Fylkja margföldun.')
        gf= str(input('Gauss eyðingu =G eða Fylka margföldun =F'))
        #Hérna fær maður að velja hversu mikið maður ætlar að sofa fyrir prófið, það fer eftir hvernig próf kennarinn gerir hvort það gagnist manni að sofa mikið
        svefn = int(input('Þú ert illa undirbúinn en veist að svefn getur gert gott fyrir þig, hvað ætlar þú að sofa mikið nóttinni fyrir prófið?'))
        # Maður verður að græða eitthvað á að læra frameftir. Í þessu tilfelli er það að geta leyst dæmi með eigin gildum
        if svefn<4.5:
            print('Þú fórst svo seint að sofa að þú hafðir tíma til að læra um Eigin gildi, vonandi kemur það á prófinu')
            EG =1
        # Hér er valið tilviljanakennt hvort gauss eyðing eða fylkja margföldun komi á prófinu
        GF=random.randint(0,1)
        if GF==1:
            print('Nú ertu mættur í prófið, fyrsta spurningin er um Gauss eyðingu.')
            if gf == 'D':
                print('Þú ert heppinn, þú lærðir Gauss eyðingu og hún kom á prófinu, einkunin þín hækkar um 2')
                einkunn = einkunn +2
            if gf == 'H':
                print('Þú valdir vitlaust, þú lærðir ekki Gauss eyðingu og hún var 20% af prófinu, þú getur í mesta lagi fengið 8.')
        if GF==0:
            print('Nú ertu mættur í prófið, fyrsta spurningin er um fylkja margföldun.')
            if gf == 'H':
                print('Þú ert heppinn, þú lærðir fylkja margföldun og hún kom á prófinu, einkunin þín hækkar um 2')
                einkunn = einkunn +2
            if gf == 'D':
                print('Þú valdir vitlaust, þú lærðir ekki fylkja margföldun og hún var 20% af prófinu, þú getur í mesta lagi fengið 8.')
        # Hérna er valið tilviljanakennt hvort eigin gildi sem sumir lærðu komi á prófinu
        # Ef maður lærði um eigin gildin fær maður +2 í einkunn
        if random.randint(0,1)==1:
            print('Eigin gildi komu á prófinu')
            if EG == 0:
                print('Þú hefðir kannski átt að vaka lengur til að læra Eigin gildi, þær voru 20% af prófinu')
            if EG == 1:
                print('Vel gert að læra Eigin gildi, þú varst að ná auka 2 heilum á prófinu')
                einkunn=einkunn + 2
        else:
            print('Þarna varstu óheppinn í staðinn fyrir eigin gildis dæmi komu 20% skilgreiningar sem þú bullaðir eitthvað í.')
            print('Röggi Möll sá í gegnum bullið þitt og gaf þér 0 stig fyrir dæmið')
        print('20% spurning hvort að fall sé línulegt')
        print('Er það ekki bara já og nei spurning, eða 50/50')
        # Hérna er 50/50 spurning hvort fallið sé línulegt
        # Gætum bætt við mynd af falli í næsta sprett til að hafa smá raunverulega línulega algebru í þessu
        svar = str(input('Er fallið línulegt eða ekki? J fyrir Já, N fyrir nei'))
        if random.randint(0,1)==0:
            rsvar= 'J'
            if svar == rsvar:
                print('Vel gert, þú giskaðir rétt')
                print('Útskýringin þín var samt ekki nægilega góð svo þú færð bara helmingin af dæminu rétt')
                einkunn = einkunn + 1
            else:
                print('Þú giskaðir vitlaust og kunnir ekki nóg um efnið til að búa þér til stig')
        else:
            rsvar= 'N'
            if svar == rsvar:
                print('Vel gert, þú giskaðir rétt')
                print('Útskýringin þín var samt ekki nægilega góð svo þú færð bara helmingin af dæminu rétt')
                einkunn = einkunn + 1
            else:
                print('Þú giskaðir vitlaust og kunnir ekki nóg um efnið til að búa þér til stig')
        print('Einföld spurning, sem gildir 10%. Wu-hu.')
        #Hérna á að svara með Ákveða
        akveda=str(input('Hvað kallast Det(A) á Íslensku?'))
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
        skrifa=str(input('VÍ, MR, MS, VMA eða HR?'))
        if skrifa == 'VÍ':
            einkunn= einkunn +1
            print('Vel gert. Þú veist að bræðurnir Möller myndu alltaf bara kenna í bestu menntastofnunum landsins')
        else:
            print('Ekki nógu gott, þú hefðir átt að vita að bræðurnir Möller myndu alltaf bara kenna í bestu menntastofnunum landsins.')
            print('Verzló er rétt svar')
        #Hérna prentast síðan niðurstöðurnar úr prófinu
        print('Þú fékkst '+ str(einkunn) +'á prófinu')
        if einkunn>4:
            print('Vel gert að ná prófinu, þú færð 6 einingar')
            StadFall=1
        if einkunn<5:
            print('Þú náðir ekki prófinu og ert kominn ennþá meira aftur úr í náminu')
        return StadFall

#_main_
#Einingarnar byrja sem núll en ef maður nær tveimur prófum maður 12 einingar
def main():
    einingar=0
    kall = Aron()
    namskeid1 = kall.Velja1()
    namskeid2=Velja2(namskeid1)
    if namskeid1 == 'S' or namskeid2 == 'S':
        einingar = einingar+6*S1Prof()
    # Til að spara forritun átti maður ekki séns á að ná eðlisfræðinni
    # Bætum mögulega við prófi í eðlisfræði fyrir næsta sprett
    if namskeid1 == 'E' or namskeid2 == 'E':
        print('Aldeilis mistök sem þú gerðir að velja Eðlisfræði prófið.')
        print('Þú áttir aldrei séns og fékkst núll í prófinu')
    if namskeid1 == 'L' or namskeid2 =='L':
        einingar = einingar+6*Lprof()
    print('Þú endaðir með '+ einingar + " , til hamingju! Hjálpaðu næsta nemanda að útskrifast")

if __name__ == "__main__":
    main()
