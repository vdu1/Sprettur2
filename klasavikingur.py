import time #Importum module til að að hafa smá biðtíma milli spurninga

#Svona ættu notendur að svara spurningunum
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["J", "j", "Já", "já"]
no = ["N", "n", "Nei", "nei"]

#Hlutir sem notendur geta notfært sér
snooz = 0

rettinntak = ("\nNotaðu aðeins A, B, eða C\n") #Til að koma í veg fyrir misskilning
jn = ("\nNotaðu aðeins já eða nei\n")

class Vikingur:

    #Leið Víkings er brotin niður í mismunandi leiðir og byrjar í "inngangur"
    time.sleep(5)
    def inngangur(self):
      time.sleep(1)
      print("Jæja, komið að Víkingi!")
      time.sleep(5)
      print ("\nÞað er próf á morgun í Stærðfræðigreiningu II. Víkingur Goði var handviss um að hann gæti"
      " tekið þetta próf með bundið fyrir augun. Þess vegna mætti hann ekki fyrr en eftir miðnætti á"
      " næturvakt í VR-II. Þegar Víkingur sér hvað þetta er létt námsefni þá hugsar hann með sér að"
      " hann geti nú alveg eins sleppt því að læra.\nHvað gerir Víkingur næst?\n")
      time.sleep(5)
      print ("""      A. Fer að spila surviv.io
      B. Fer að spila Fifa
      C. Hugsar með sér að það nægi að mæta vel seint í prófið""")
      choice = input("\n>>> ") #Here is your first choice.
      if choice in answer_A:
        time.sleep(3)
        print ("\nGlæsilegt þú gast ekki klúðrað þessari spurningu því Stægrein II"
        " var svo létt fyrir Víking. Nú er Víkingur mættur í prófið.\nHvernig tekst hann á við prófið?\n")
        prof()
      elif choice in answer_B:
        time.sleep(3)
        print ("\nGlæsilegt þú gast ekki klúðrað þessari spurningu því Stægrein II"
        " var svo létt fyrir Víking. Nú er Víkingur mættur í prófið.\nHvernig tekst hann á við prófið?\n")
        prof()
      elif choice in answer_C:
        time.sleep(3)
        print ("\nGlæsilegt þú gast ekki klúðrað þessari spurningu því Stægrein II"
        " var svo létt fyrir Víking. Nú er Víkingur mættur í prófið.\nHvernig tekst hann á við prófið?\n")
        prof()
      else:
        print (rettinntak)
        inngangur()

    def prof():
      time.sleep(3)
      print ("""  A. Biður um krassblað til að geta fínskrifað svörin sín
      B. Dritar niður á blað einhverju gáfulegu og fer út án þess að fara yfir
      C. Notar allan próftímann og reynir að krafsa í öll möguleg stig""")
      choice = input("\n>>> ")
      if choice in answer_A:
        time.sleep(3)
        print ("\nRangt, þú þekkir Víking greinilega ekki nógu vel. Reyndu aftur skepnan þín!\n")
        prof()
      elif choice in answer_B:
        time.sleep(3)
        print ("\nVíkingi leið ágætlega með prófið og langar að fagna. Leiðin liggur beint"
        " á Stúdentakjallarann.\nHvað fær Víkingur sér að borða?\n")
        matur()
      elif choice in answer_C:
        time.sleep(3)
        print ("\nRangt, þú þekkir Víking greinilega ekki nógu vel. Reyndu aftur skepnan þín!\n")
        prof()
      else:
        print (rettinntak)
        prof()

    def matur():
      time.sleep(3)
      print ("""  A. Burger og bjór
      B. Grænmetislasagna
      C. Hnetusteik""")
      choice = input("\n>>> ")
      if choice in answer_A:
        time.sleep(3)
        print ("\nÚff hvað burgerinn og bjórinn var góður! Víkingur er nú saddur"
        " og fer heim og leggur sig. Hann veit að síðasta lokaprófið er á morgun"
        " og það í tölvuteikningu. Hann er því harður við sjálfan sig og stillir"
        " vekjaraklukkuna aðeins eftir 3 tíma." #Henda time gæa hingað?
        " Tíminn líður, vekjaraklukkan hringir og Víkingi dauðbregður. Hann þarf nú að taka stóra ákvörðun."
        " Ýtir Víkingur á snooze.\nJá eða nei?")
        logn()
      elif choice in answer_B:
        print ("\nRangt, þú þekkir Víking greinilega ekki nógu vel. Reyndu aftur skepnan þín!\n")
        matur()
      elif choice in answer_C:
        print ("\nRangt, þú þekkir Víking greinilega ekki nógu vel. Reyndu aftur skepnan þín!\n")
        matur()
      else:
        print (rettinntak)
        matur()

    def logn():
      time.sleep(3)
      choice = input("\n>>> ")
      if choice in yes:
        snooz = 1 #Snoozar
      elif choice in no:
        snooz = 0 #Snoozar ekki
      else:
        print (jn)
        logn()
      time.sleep(3)
      print ("\nHvað gerir Víkingur eftir það?\n")
      time.sleep(3)
      print ("""  A. Hann fer aftur að sofa
      B. Hann vaknar""")
      choice = input("\n>>> ")
      if choice in answer_A:
          if snooz > 0:
              time.sleep(3)
              print ("\nÞað er rétt, Víkingur fór aftur að sofa"
              " EN sem betur fer ýtti hann á snooze, hann snoozar"
              " hins vegar of lengi en ekki nógu lengi til að geta ekki lært fyrir prófið."
              " Víkingur lærir uppí VR-II í alla nótt sem verður til þess að hann"
              " mætir of seint í tölvuteikningar lokaprófið daginn eftir.")
              lokaprof()
          else:
              time.sleep(3)
              print ("\nÞað er rétt, Víkingur fór aftur að sofa."
              " Því miður gleymdi hann hins vegar að ýta á snooze og náði ekki"
              " að læra nóg fyrir tölvuteikningar lokaprófið."
              " Eins og svo oft áður þá varð svefninn Víkingi að falli"
              " og í þetta sinn sá svefninn til þess að Víkingur útskrifast ekki úr háskólanum! Hjálpaðu næsta"
              " nemanda að útskrifast\n")
      elif choice in answer_B:
        time.sleep(3)
        print ("\nÓtrúlegt en satt þá vaknar Víkingur á réttum tíma og hefur nægan tíma til að læra fyrir lokaprófið."
        " Hann mætir sáttur með T-stikuna í lokaprófið og rúllar því upp!")
        time.sleep(3)
        print ("\nTil hamingju þú hefur náð að útskrifa Víking Goða! Hjálpaðu næsta"
        " nemanda að útskrifast\n")
      else:
          print (rettinntak)
          logn()

    def lokaprof():
      time.sleep(3)
      print ("\nVíkingur er mættur í prófið en þar sem að hann svaf svo yfir sig þá gleymdi hann T-stikunni heima."
      " Víkingur er í klípu, hvað gerir hann nú?\n")
      time.sleep(3)
      print ("""  A. Hann fær lánað teikniborð frá Ara
      B. Hann ákveður að taka prófið fríhendis
      C. Hann vælir í kennaranum og fær að taka prófið í tölvu""")
      choice = input("\n>>> ")
      if choice in answer_A:
        time.sleep(3)
        print("\nVíkinur fékk lánað teikniborðið og rúllaði lokaprófinu upp.")
        time.sleep(3)
        print("\nTil hamingju, þú náðir að útskrifa Víking Goða! Hjálpaðu næsta"
        " nemanda að útskrifast\n")
      elif choice in answer_B:
        time.sleep(3)
        print("\nVíkingur er því miður skelfilegur að teikna fríhendis.")
        time.sleep(3)
        print("\nHann féll á prófinu og þar af leiðandi úr skólanum, því miður"
        " náður þú ekki að útskrifa Víking Goða! Hjálpaðu næsta nemanda að útskrifast\n")
      elif choice in answer_C:
        time.sleep(3)
        print("\nVíkinur er frábær í Autocad og rúllar prófinu upp.")
        time.sleep(3)
        print("\nTil hamingju, þú náðir að útskrifa Víking Goða! Hjálpaðu næsta"
        " nemanda að útskrifast\n")
      else:
        print (rettinntak)
        lokaprof()

def main():

    kall = Vikingur()
    inngangur = kall.inngangur()
    spurningar = kall.spurningar()

if __name__ == "__main__":
    main()
