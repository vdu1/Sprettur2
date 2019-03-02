# This Python file uses the following encoding: utf-8
import math
import random


def Velja1():
    print('Þú félst í þremur lokaprófum á fyrstu önninni þinni.')
    print('Nú verður þú að velja tvö námskeið til að taka í endurtekt')
    namskeid1 = input('S fyrir Stærðfræði greiningu, L fyrir Línulega Algebru eða E fyrir Eðlisfræði')
    return namskeid1

def Velja2(namskeid1):
    print('Nú ertu búinn að velja eitt námskeið til að taka í endurtekt, próftaflan er heppileg svo þú getur tekið eitt endurtektarpróf í viðbót.')
    if namskeid1=='S':
        namskeid2= input('L fyrir Línulega Algebru eða E fyrir Eðlisfræði')
    elif namskeid1=='L':
        namskeid2=input('S fyrir Stærðfræði greiningu eða E fyrir Eðlisfræði')
    elif namskeid1=='E':
        namskeid2=input('S fyrir Stærðfræði greiningu eða L fyrir Línulega Algebru')
    else:
        print('Þú náðir ekki einu sinni að velja námskeiðin rétt, þú ert fallinn úr skólanum á fyrstu önn')
        end()
    return namskeid2

def S1Prof():
    StadFall =0
    einkunn =0
    TM =0
    print('Þú ert að læra fyrir endurtektarpróf í Stærðfræðigreiningu. Þú hefur ekki mikinn tíma þar sem þú ert haugur.')
    print('Þú verður að velja hvort þú viljir læra diffrun eða heildun fyrir prófið.')
    dh= input('Diffrun =D eða Heildun =H')
    svefn = int(input('Þú ert illa undirbúinn en veist að svefn getur gert gott fyrir þig, hvað ætlar þú að sofa mikið nóttinni fyrir prófið?'))
    if svefn<4.5:
        print('Þú fórst svo seint að sofa að þú hafðir tíma til að læra Taylor margliður, vonandi kemur það á prófinu')
        TM =1
    DH=random.randint(0,1)
    if DH==1:
        print('Nú ertu mættur í prófið, fyrsta spurningin er um Diffrun.')
        if dh == 'D':
            print('Þú ert heppinn, þú lærðir diffrun og hún kom á prófinu, einkunin þín hækkar um 2')
            einkunn = einkunn +2
        if dh == 'H':
            print('Þú valdir vitlaust, þú lærðir ekki diffrun og hún var 20% af prófinu, þú getur í mesta lagi fengið 8.')
    if DH==0:
        print('Nú ertu mættur í prófið, fyrsta spurningin er um heildun.')
        if dh == 'H':
            print('Þú ert heppinn, þú lærðir heildun og hún kom á prófinu, einkunin þín hækkar um 2')
            einkunn = einkunn +2
        if dh == 'D':
            print('Þú valdir vitlaust, þú lærðir ekki heildun og hún var 20% af prófinu, þú getur í mesta lagi fengið 8.')
    if random.randint(0,1)==1:
        print('Taylor margliður komu á prófinu')
        if TM == 0:
            print('Þú hefðir kannski átt að vaka lengur til að læra Taylor margliður, þær voru 20% af prófinu')
        if TM == 1:
            print('Vel gert að læra Taylor margliður, þú varst að ná auka 2 heilum á prófinu')
            einkunn=einkunn + 2
    else:
        print('Taylor margliður komu ekki. Það kom fáranlegt markgildisdæmi sem þú áttir aldrei séns í. Óheppinn.')
    print('20% spurning hvort að fall sé samfellt á ákveðnu bili')
    print('Er það ekki bara já og nei spurning, eða 50/50')
    svar = input('Er fallið samfellt eða ekki? J fyrir Já, N fyrir nei')
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
    print('Einfalt einingahringsdæmi, sem gildir 10%. Wu-hu.')
    Imba=input('cos^2(theta)+sin^2(theta)=x. Hvað er x?')
    if Imba==1:
        print('Var þetta gisk? Það breytir engu, þetta var allavega rétt')
        einkunn=einkunn+1
    else:
        print('Svona á að vita, þarna misstir þú dýrmætt stig úr pokanum')
    svefnkrafa = random.randint(0,9)
    if svefnkrafa >svefn:
        print('Þú hefðir átt að sofa meira. Benni kennari henti í svæsið 20% dæmi sem þú fattaðir ekki hvernig á að leysa.')
    if svefn >= svefnkrafa:
        einkunn= einkunn+2
        print('Vel gert, þú varst vel sofinn og fattaðir trixið í svæsnu 20% dæmi frá Benna')
    print('Þetta er nú fáranleg 10% spurning')
    print('Hver er uppáhalds rithöfundurinn hans Benna kennara?')
    print('A George R.R. Martin')
    print('B Douglas Adams')
    print('eða C Yrsa Sigurðardóttir')
    skrifa=input('A, B eða C?')
    if skrifa == 'B':
        einkunn= einkunn +1
        print('Þú varst augljóslega duglegur að lesa EdBook yfir önnina')
    else:
        print('Það þarf að lesa EdBook til að ná svona prófum')
    if einkunn>4:
        print('Vel gert að ná prófinu, þú færð 6 einingar')
        StadFall=1
    if einkunn<5:
        print('Þú náðir ekki prófinu og ert kominn ennþá meira aftur úr í náminu')
    return StadFall

def Lprof():
    StadFall =0
    einkunn =0
    EG =0
    print('Þú ert að læra fyrir endurtektarpróf í Línulegri algebru. Þú hefur ekki mikinn tíma þar sem þú varst upptekinn í boltanum.')
    print('Þú verður að velja hvort þú viljir læra Gauss eyðingu eða Fylkja margföldun.')
    gf= input('Gauss eyðingu =G eða Fylka margföldun =F')
    svefn = int(input('Þú ert illa undirbúinn en veist að svefn getur gert gott fyrir þig, hvað ætlar þú að sofa mikið nóttinni fyrir prófið?'))
    if svefn<4.5:
        print('Þú fórst svo seint að sofa að þú hafðir tíma til að læra Eigin gildi, vonandi kemur það á prófinu')
        EG =1
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
    if random.randint(0,1)==1:
        print('Eigin gildi komu á prófinu')
        if EG == 0:
            print('Þú hefðir kannski átt að vaka lengur til að læra Taylor margliður, þær voru 20% af prófinu')
        if EG == 1:
            print('Vel gert að læra Taylor margliður, þú varst að ná auka 2 heilum á prófinu')
            einkunn=einkunn + 2
    else:
        print('Þarna varstu óheppinn í staðinn fyrir eigin gildis dæmi komu 20% skilgreiningar sem þú bullaðir eitthvað í.')
        print('Röggi Möll sá í gegnum bullið þitt og gaf þér 0 stig fyrir dæmið')
    print('20% spurning hvort að fall sé línulegt')
    print('Er það ekki bara já og nei spurning, eða 50/50')
    svar = input('Er fallið línulegt eða ekki? J fyrir Já, N fyrir nei')
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
    akveda=input('Hvað kallast Det(A) á Íslensku?')
    if akveda=='Ákveða' or akveda=='ákveða' or akveda=='Akveda' or akveda=='akveda':
        print('Var þetta gisk? Það breytir engu, þetta var allavega rétt')
        einkunn=einkunn+1
    else:
        print('Svona á að vita, þarna misstir þú dýrmætt stig úr pokanum')
    svefnkrafa = random.randint(0,9)
    if svefnkrafa >svefn:
        print('Þú hefðir átt að sofa meira. Röggi Möll henti í svæsið 20% dæmi sem þú fattaðir ekki hvernig á að leysa.')
    if svefn >= svefnkrafa:
        einkunn= einkunn+2
        print('Vel gert, þú varst vel sofinn og fattaðir trixið í svæsnu 20% dæmi frá Rögga')
    print('Þetta er nú fáranleg spurning 10% spurning')
    print('Í hvaða framhaldsskóla kennir Þórður bróðir Rögnvalds stærðfræði?')
    print('Verzunarskóla Íslands')
    print('Menntaskólanum í Reykjavík')
    print('Leikskólanum í Skeifunni')
    print('Verkmenntaskólanum á Akureyri')
    print('Trúðaskólanum í Nauthólsvík')
    skrifa=input('VÍ, MR, MS, VMA eða HR?')
    if skrifa == 'VÍ':
        einkunn= einkunn +1
        print('Vel gert. Þú veist að bræðurnir Möller myndu alltaf bara kenna í bestu menntastofnunum landsins')
    else:
        print('Ekki nógu gott, þú hefðir átt að vita að bræðurnir Möller myndu alltaf bara kenna í bestu menntastofnunum landsins.')
        print('Verzló er rétt svar')
    if einkunn>4:
        print('Vel gert að ná prófinu, þú færð 6 einingar')
        StadFall=1
    if einkunn<5:
        print('Þú náðir ekki prófinu og ert kominn ennþá meira aftur úr í náminu')
    return StadFall






#_main_
einingar=0
namskeid1=Velja1()
namskeid2=Velja2(namskeid1)
if namskeid1 == 'S' or namskeid2 == 'S':
    einingar = einingar+6*S1Prof()

if namskeid1 == 'E' or namskeid2 == 'E':
    print('Aldeilis mistök sem þú gerðir að velja Eðlisfræði prófið.')
    print('Þú áttir aldrei séns og fékkst núll í prófinu')
if namskeid1 == 'L' or namskeid2 =='L':
    einingar = einingar+6*Lprof()
print('Þú endaðir með '+ str(einingar))
