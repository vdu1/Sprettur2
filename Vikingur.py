import time #Importum module til að að hafa smá biðtíma milli falla og skipana
import sys

class Vikingur:
    #Svona ættu notendur að svara spurningunum
    answer_A = ["A", "a"]
    answer_B = ["B", "b"]
    answer_C = ["C", "c"]
    yes = ["J", "j", "Já", "já"]
    no = ["N", "n", "Nei", "nei"]

    #Hlutir sem notendur geta notfært sér
    snooz = 0

    rettinntak = ("\nNotaðu aðeins A, B, eða C\n") #Til að koma í veg fyrir misskilning
    jn = ("\nNotaðu aðeins já eða nei")

    def __init__(self):
        pass

    #Leið Víkings er brotin niður í mismunandi leiðir og byrjar í "inngangur"
    #Það þarf að laga byrjunina
    #time.sleep(1)
    def inngangur(self):
        self.prof()
    #   teljari =0
    #   time.sleep(5)
    #   print1="Jæja, komið að Víkingi!\n"
    #   for char in print1:
    #       sys.stdout.write(char)
    #       sys.stdout.flush()
    #       time.sleep(.050)
    #   time.sleep(2)
    #   print2= "\nÞitt verkefni er að vinna þig upp í gegnum lokaprófssögu Víkings og koma honum í gegnum prófin."
    #   print21=" Passaðu þig að velja rétt, annars fellur Víkingur úr skólanum!\n"
    #   for char in print2:
    #       sys.stdout.write(char)
    #       sys.stdout.flush()
    #       time.sleep(.050)
    #   for char in print21:
    #       sys.stdout.write(char)
    #       sys.stdout.flush()
    #       time.sleep(.050)
    #   time.sleep(1)
    #   print3="\nNú byrjar ballið!"
    #   for char in print3:
    #       sys.stdout.write(char)
    #       sys.stdout.flush()
    #       time.sleep(.050)
    #   time.sleep(1)
    #   print("\n")
    #   print31="Það er próf á morgun í Stærðfræðigreiningu II. Víkingur Goði var handviss um að hann gæti"
    #   print32=" tekið þetta próf með bundið fyrir augun. Þess vegna mætti hann ekki fyrr en eftir miðnætti á"
    #   print33=" næturvakt í VR-II. Þegar Víkingur sér hvað þetta er létt námsefni þá hugsar hann með sér að"
    #   print34=" hann geti nú alveg eins sleppt því að læra."
    #   for char in print31:
    #       sys.stdout.write(char)
    #       sys.stdout.flush()
    #       time.sleep(.050)
    #   for char in print32:
    #       sys.stdout.write(char)
    #       sys.stdout.flush()
    #       time.sleep(.050)
    #   for char in print33:
    #       sys.stdout.write(char)
    #       sys.stdout.flush()
    #       time.sleep(.050)
    #   for char in print34:
    #       sys.stdout.write(char)
    #       sys.stdout.flush()
    #       time.sleep(.050)
    #   time.sleep(1)
    #   print("\n")
    #     print4="Hvað gerir Víkingur næst?\n"
    #     for char in print4:
    #         sys.stdout.write(char)
    #         sys.stdout.flush()
    #         time.sleep(.050)
    #     self.kvold()
    #
    # def kvold(self):
    #
    #   print5= """\n      A. Fer að spila surviv.io
    #   B. Fer að spila Fifa
    #   C. Hugsar með sér að það nægi að mæta vel seint í prófið"""
    #   for char in print5:
    #       sys.stdout.write(char)
    #       sys.stdout.flush()
    #       time.sleep(.050)
    #   time.sleep(1)
    #   choice = input("\n>>> ") #Here is your first choice.
    #   time.sleep(1)
    #
    #   #Henda inn try/except hér?
    #
    #   if choice in self.answer_A:
    #     time.sleep(1)
    #     print6= "\nGlæsilegt þú gast ekki klúðrað þessari spurningu því Stægrein II"
    #     " var svo létt fyrir Víking. Nú er Víkingur mættur í prófið.\nHvernig tekst hann á við prófið?\n"
    #     for char in print6:
    #         sys.stdout.write(char)
    #         sys.stdout.flush()
    #         time.sleep(.050)
    #     teljari = self.prof()
    #   elif choice in self.answer_B:
    #     time.sleep(1)
    #     print61= "\nGlæsilegt þú gast ekki klúðrað þessari spurningu því Stægrein II"
    #     print62= " var svo létt fyrir Víking. Nú er Víkingur mættur í prófið.\nHvernig tekst hann á við prófið?\n"
    #     for char in print61:
    #         sys.stdout.write(char)
    #         sys.stdout.flush()
    #         time.sleep(.050)
    #     for char in print62:
    #         sys.stdout.write(char)
    #         sys.stdout.flush()
    #         time.sleep(.050)
    #     teljari = self.prof()
    #   elif choice in self.answer_C:
    #     time.sleep(1)
    #     print63= "\nGlæsilegt þú gast ekki klúðrað þessari spurningu því Stægrein II"
    #     print64=" var svo létt fyrir Víking. Nú er Víkingur mættur í prófið.\nHvernig tekst hann á við prófið?\n"
    #     for char in print63:
    #         sys.stdout.write(char)
    #         sys.stdout.flush()
    #         time.sleep(.050)
    #     for char in print64:
    #         sys.stdout.write(char)
    #         sys.stdout.flush()
    #         time.sleep(.050)
    #     teljari = self.prof()
    #   else:
    #     printrettinntak = self.rettinntak
    #     for char in printrettinntak:
    #         sys.stdout.write(char)
    #         sys.stdout.flush()
    #         time.sleep(.050)
    #     self.kvold()
    #   return teljari

    def prof(self):
      teljari2 = 0
      time.sleep(1)
      print71="""\n      A. Biður um krassblað til að geta fínskrifað svörin sín
      B. Dritar niður á blað einhverju gáfulegu og fer út án þess að fara yfir
      C. Notar allan próftímann og reynir að krafsa í öll möguleg stig"""
      for char in print71:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(.050)
      time.sleep(1)
      choice = input("\n>>> ")
      if choice in self.answer_A:
        time.sleep(1)
        print72= "\nRangt, þú þekkir Víking greinilega ekki nógu vel. Reyndu aftur skepnan þín!\n"
        for char in print72:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
        teljari2 = self.prof()
      elif choice in self.answer_B:
        time.sleep(1)
        print73= "\nVíkingi leið ágætlega með prófið og langar að fagna. Leiðin liggur beint"
        print74= " á Stúdentakjallarann.\nHvað fær Víkingur sér að borða?\n"
        for char in print73:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
        for char in print74:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
        teljari2 = self.matur()
      elif choice in self.answer_C:
        time.sleep(1)
        print8 ="\nRangt, þú þekkir Víking greinilega ekki nógu vel. Reyndu aftur skepnan þín!\n"
        for char in print8:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
        teljari2 = self.prof()
      else:
        printrettinntak1 = self.rettinntak
        for char in printrettinntak1:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
        teljari = self.prof()
      return teljari2

    def matur(self):
      counter = 0
      time.sleep(1)
      print9 ="""\n      A. Burger og bjór
      B. Grænmetislasagna
      C. Hnetusteik"""
      for char in print9:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(.050)

      choice = input("\n>>> ")
      if choice in self.answer_A:
        time.sleep(1)
        print91 ="\nÚff hvað burgerinn og bjórinn var góður! Víkingur er nú saddur"
        print92 =" og fer heim og leggur sig. Hann veit að síðasta lokaprófið er á morgun"
        print93 =" og það í tölvuteikningu. Hann er því harður við sjálfan sig og stillir"
        print94 =" vekjaraklukkuna aðeins eftir 3 tíma." #Henda time gæa hingað?
        print95 =" Tíminn líður, vekjaraklukkan hringir og Víkingi dauðbregður. Hann þarf nú að taka stóra ákvörðun."
        print96 =" Ýtir Víkingur á snooze.\nJá eða nei?"
        for char in print91:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
        for char in print92:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
        for char in print93:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
        for char in print94:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
        for char in print95:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
        for char in print96:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
        counter = self.logn()
      elif choice in self.answer_B:
        print100 ="\nRangt, þú þekkir Víking greinilega ekki nógu vel. Reyndu aftur skepnan þín!\n"
        for char in print100:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
        counter = self.matur()
      elif choice in self.answer_C:
        print101 ="\nRangt, þú þekkir Víking greinilega ekki nógu vel. Reyndu aftur skepnan þín!\n"
        for char in print101:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
        counter = self.matur()
      else:
        print (self.rettinntak)
        counter = self.matur()
      return counter

    #Það þarf að laga if setningar þannig að það komi ekki bull ef notandi slær inn vitlaust
    def logn(self):
      utskrifadir2 = 0
      time.sleep(1)
      choice = input("\n>>> ")
      if choice in self.yes:
        snooz = 1 #Snoozar
      elif choice in self.no:
        snooz = 0 #Snoozar ekki
      else:
        print (self.jn)
        utskrifadir2 = self.logn()
      time.sleep(1)
      print102= "\nHvað gerir Víkingur eftir það?\n"
      for char in print102:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(.050)
      time.sleep(1)
      print103= """      A. Hann fer aftur að sofa
      B. Hann vaknar"""
      for char in print103:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(.050)
      choice = input("\n>>> ")
      if choice in self.answer_A:
          if snooz > 0:
              time.sleep(1)
              print104= "\nÞað er rétt, Víkingur fór aftur að sofa"
              print105= " EN sem betur fer ýtti hann á snooze, hann snoozar"
              print106= " hins vegar of lengi en ekki nógu lengi til að geta ekki lært fyrir prófið."
              print107= " Víkingur lærir uppí VR-II í alla nótt sem verður til þess að hann"
              print108= " mætir of seint í tölvuteikningar lokaprófið daginn eftir."
              for char in print104:
                  sys.stdout.write(char)
                  sys.stdout.flush()
                  time.sleep(.050)
              for char in print105:
                  sys.stdout.write(char)
                  sys.stdout.flush()
                  time.sleep(.050)
              for char in print106:
                  sys.stdout.write(char)
                  sys.stdout.flush()
                  time.sleep(.050)
              for char in print107:
                  sys.stdout.write(char)
                  sys.stdout.flush()
                  time.sleep(.050)
              for char in print108:
                  sys.stdout.write(char)
                  sys.stdout.flush()
                  time.sleep(.050)

              utskrifadir2 = self.lokaprof()
          else:
              utskrifadir2 = 0
              time.sleep(1)
              print109 = "\nÞað er rétt, Víkingur fór aftur að sofa."
              print110 =" Því miður gleymdi hann hins vegar að ýta á snooze og náði ekki"
              print111 =" að læra nóg fyrir tölvuteikningar lokaprófið."
              print112 =" Eins og svo oft áður þá varð svefninn Víkingi að falli"
              print113= " og í þetta sinn sá svefninn til þess að Víkingur útskrifast ekki úr háskólanum! Hjálpaðu næsta"
              print114= " nemanda að útskrifast\n"
              for char in print109:
                  sys.stdout.write(char)
                  sys.stdout.flush()
                  time.sleep(.050)
              for char in print110:
                  sys.stdout.write(char)
                  sys.stdout.flush()
                  time.sleep(.050)
              for char in print111:
                  sys.stdout.write(char)
                  sys.stdout.flush()
                  time.sleep(.050)
              for char in print112:
                  sys.stdout.write(char)
                  sys.stdout.flush()
                  time.sleep(.050)
              for char in print113:
                  sys.stdout.write(char)
                  sys.stdout.flush()
                  time.sleep(.050)
              for char in print114:
                  sys.stdout.write(char)
                  sys.stdout.flush()
                  time.sleep(.050)

      elif choice in self.answer_B:
        utskrifadir2 = 1
        time.sleep(1)
        print115= "\nÓtrúlegt en satt þá vaknar Víkingur á réttum tíma og hefur nægan tíma til að læra fyrir lokaprófið."
        print116= " Hann mætir sáttur með T-stikuna í lokaprófið og rúllar því upp!"
        for char in print115:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
        for char in print116:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
        time.sleep(1)
        print117= "\nTil hamingju þú hefur náð að útskrifa Víking Goða!\n\nHjálpaðu næsta"
        " nemanda að útskrifast.\n"
        for char in print117:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
      else:
          print (self.rettinntak)
          self.logn()
      return utskrifadir2

    def lokaprof(self):
      utskrifadir3=0
      time.sleep(1)
      print120="\nVíkingur er mættur í prófið en þar sem að hann svaf svo yfir sig þá gleymdi hann T-stikunni heima."
      print121= " Víkingur er í klípu, hvað gerir hann nú?\n"
      for char in print120:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(.050)
      for char in print121:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(.050)
      time.sleep(1)
      print122= """      A. Hann fær lánað teikniborð frá Ara
      B. Hann ákveður að taka prófið fríhendis
      C. Hann vælir í kennaranum og fær að taka prófið í tölvu"""
      for char in print122:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(.050)

      choice = input("\n>>> ")
      if choice in self.answer_A:
        utskrifadir3 = 1
        time.sleep(1)
        print123="\nVíkinur fékk lánað teikniborðið og rúllaði lokaprófinu upp."
        for char in print123:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)

        time.sleep(1)
        print124="\nTil hamingju, þú náðir að útskrifa Víking Goða! Hjálpaðu næsta nemanda að útskrifast.\n"
        for char in print124:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
      elif choice in self.answer_B:
        utskrifadir3 = 0
        time.sleep(1)
        print125= "\nVíkingur er því miður skelfilegur að teikna fríhendis."
        for char in print125:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
        #time.sleep(1)
        print126= "\nHann féll á prófinu og þar af leiðandi úr skólanum, því miður"
        print127= " náður þú ekki að útskrifa Víking Goða!\n\nHjálpaðu næsta nemanda að útskrifast.\n"
        for char in print126:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
        for char in print127:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
      elif choice in self.answer_C:
        utskrifadir3 = 1
        time.sleep(1)
        print128= "\nVíkinur er frábær í Autocad og rúllar prófinu upp."
        for char in print129:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
        time.sleep(1)
        print130="\nTil hamingju, þú náðir að útskrifa Víking Goða! Hjálpaðu næsta nemanda að útskrifast.\n"
        for char in print130:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.050)
      else:
        print (self.rettinntak)
        self.lokaprof()
      return utskrifadir3

def main():

    kall = Vikingur()
    inngangur = kall.inngangur()

if __name__ == "__main__":
    main()
