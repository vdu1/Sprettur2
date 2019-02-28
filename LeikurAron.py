import math
# coding=utf-8


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
        exit()
    return namskeid2

def S1prof():
    Stad/Fall =0
    einkunn =0
    print('Þú ert að læra fyrir endurtektarpróf í Stærðfræðigreiningu. Þú hefur ekki mikinn tíma þar sem þú ert haugur.')
    print('Þú verður að velja hvort þú viljir læra diffrun, heildun eða bæði fyrir prófið.')
    dh= input('Diffrun =D eða Heildun =H')
    svefn = int(input('Þú ert illa undirbúinn en veist að svefn getur gert gott fyrir þig, hvað ætlar þú að sofa mikið nóttinni fyrir prófið?'))
    DH=math.random()
    if DH>0.5:
        print('Nú ertu mættur í prófið, fyrsta spurningin er um Diffrun.')
            if dh == 'D'
                print('Þú ert heppinn, þú lærðir diffrun og hún kom á prófinu, einkunin þín hækkar um 1')
                einkunn = einkunn +1
            if dh == 'H'
                print('Þú valdir vitlaust, þú lærðir ekki diffrun og hún var 10% af prófinu, þú getur í mesta lagi fengið 9.')
    if DH<0.5:
        print('Nú ertu mættur í prófið, fyrsta spurningin er um heildun.')
            if dh == 'H'
                print('Þú ert heppinn, þú lærðir heildun og hún kom á prófinu, einkunin þín hækkar um 1')
                einkunn = einkunn +1
            if dh == 'D'
                print('Þú valdir vitlaust, þú lærðir ekki heildun og hún var 10% af prófinu, þú getur í mesta lagi fengið 9.')




#_main_
Velja1()
Velja2()
if namskeid1 == 'S':
    S1Prof()
