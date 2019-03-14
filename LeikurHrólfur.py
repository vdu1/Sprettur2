# This Python file uses the following encoding: utf-8
import math
import random
import time



def intro():
   print ("Hrólfur Sveinsson er ungur drengur úr Hafnarfirðinum."+"\n")
   time.sleep(1)
   print ("Hrólfur á við ýmis vandamál að stríða. Útaf þessum vandamálum er hann oft áhyggjufullur."+"\n")
   time.sleep(1)
   print ("Þökk sé streitu sér Hrólfur ungur að hann er nálægt því að missa hárið."+"\n")
   time.sleep(1)
   print("Þú ert nú komin í það hlutverk að hjálpa Hrólf með allar ákvarðanir til að minnka streitu og halda í hárið."+"\n")
   time.sleep(1)
   print ("Hrólfur veit að ef hann missir allt hárið þá mun hafa ekki hafa sjálfstraustið í að klára háskólann."+"\n")
   time.sleep(1)
   print("Fyrsta stóra ákvörðunin sem þú þarft að hjálpa Hrólf með er í hvaða framhaldsskóla hann á að fara.")
  time.sleep(1)
  print ("""  A. Menntaskólann í Reykjavík
  B. Flensborgarskólann í Hafnarfirði
  C. Verzlunarskóla Íslands""")
  choice = input(">>> ") #Here is your first choice.
  if choice in answer_A:
    print("Jæja, þú ert ömurlegur ráðgjafi. Hrólfur missti allt hárið og féll úr MR á fyrstu önninni. Hann er samt mjög ánægður á dælunni.")
    return 100
  elif choice in answer_B:
    option_Flens()
  elif choice in answer_C:
    option_Verzl()
  else:
    print ("A, B eða C takk fyrir")
    intro()

def option_Flens():
  print ("Hrólfur er mættur í Flensborg. Honum líður vel í Firðinum og rúllar upp náminu."+"\n")
  print("Þrátt fyrir að vera heimakær hefur Hrólfur áhyggjur af að finna ekki spennandi kvenkost í Hafnarfirðinum."+"\n")
  print("Þetta angrar hann ekki svakalega en samt nóg til að hann missi 4 hár af hausnum"+"\n")
  counter = counter - 4
  time.sleep(1)
  print("Hrólfur er mikill fótboltastrákur. Hann elskar fátt meira en að sparka í boltann með góðum félögum"+"\n")
  print("Hrólfur er hinsvegar í erfiðri stöðu. Félagarnir eru ekki með jafn mikið metnað í boltanum. Hrólfur sjálfur gæti fengið að æfa með meistaraflokki FH í sumar."+"\n")
  print("Hrólfur veit samt að það er mikið álag að vera í meistaraflokki"+"Ætti hann að eltast við draumana í FH eða ætti hann að fara með félögunum í Passion League"+"\n")
  time.sleep(1)
  print ("""  A. FH
  B. Passion League
  """)
  choice = input(">>> ")
  if choice in answer_A:
    print("Þetta var slæm ákvörðun. Hrólf líður ekki vel í FH reynir í nokkra mánuði að æfa undir miklu álagi en hættir síðan. -10 hár")
    counter = counter -10
  elif choice in answer_B:
    print ("Geggjuð ákvörðun. Hrólfur skemmtir sér konunglega með félögunum í Passion League, einn stóran Tuborg takk."+"\n")
  else:
    print ("A eða B koma svo")
  print("Námið í Flensborg er að fara vel með Hrólf. Hann er samt að velta því fyrir sér hvort hann eigi að eltast við að vera Dúx."+"\n")
  print("Það gæti gert eitthvað fyrir sjálfstraustið hans að vera dúx en það er auðvitað mikil vinna sem myndi fara í það"+"\n")
  print("A fyrir að eltast við að vera dúx eða B fyrir að útskrifast bara")
  time.sleep(1)
  choice = input(">>> ")
  if choice in answer_A:
    print("Ekki vera svona heimskur, maður græðir ekkert á að vera Dúx, spurðu bara Erni Jónsson"+"\n")
    print("-10 hár fyrir óþarfan metnað í námi")
    counter = counter -10
  elif choice in answer_B:
    print ("Geggjuð ákvörðun. Hrólfur skemmtir sér konunglega með félögunum í Passion League, einn stóran Tuborg takk."+"\n")
  else:
    print ("A eða B koma svo")


def option_cave():
  print ("\nYou were hesitant, since the cave was dark and "
  "ominous. Before you fully enter, you notice a shiny sword on "
  "the ground. Do you pick up a sword. Y/N?")
  choice = input(">>> ")
  if choice in yes:
    sword = 1 #adds a sword
  else:
    sword = 0
  print ("\nWhat do you do next?")
  time.sleep(1)
  print ("""  A. Hide in silence
  B. Fight
  C. Run""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("\nReally? You're going to hide in the dark? I think "
    "orcs can see very well in the dark, right? Not sure, but "
    "I'm going with YES, so...\n\nYou died!")
  elif choice in answer_B:
   if sword > 0:
    print ("\nYou laid in wait. The shimmering sword attracted "
    "the orc, which thought you were no match. As he walked "
    "closer and closer, your heart beat rapidly. As the orc "
    "reached out to grab the sword, you pierced the blade into "
    "its chest. \n\nYou survived!")
   else: #If the user didn't grab the sword
     print ("\nYou should have picked up that sword. You're "
     "defenseless. \n\nYou died!")
  elif choice in answer_C:
    print ("As the orc enters the dark cave, you sliently "
    "sneak out. You're several feet away, but the orc turns "
    "around and sees you running.")
    option_run()
  else:
    print (required)
    option_cave()

def option_run():
  print ("\nYou run as quickly as possible, but the orc's "
  "speed is too great. You will:")
  time.sleep(1)
  print ("""  A. Hide behind boulder
  B. Trapped, so you fight
  C. Run towards an abandoned town""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("You're easily spotted. "
    "\n\nYou died!")
  elif choice in answer_B:
    print ("\nYou're no match for an orc. "
    "\n\nYou died!")
  elif choice in answer_C:
    option_town()
  else:
    print (required)
    option_run()

def option_town():
  print ("\nWhile frantically running, you notice a rusted "
  "sword lying in the mud. You quickly reach down and grab it, "
  "but miss. You try to calm your heavy breathing as you hide "
  "behind a delapitated building, waiting for the orc to come "
  "charging around the corner. You notice a purple flower "
  "near your foot. Do you pick it up? Y/N")
  choice = input(">>> ")
  if choice in yes:
    flower = 1 #adds a flower
  else:
    flower = 0
  print ("You hear its heavy footsteps and ready yourself for "
  "the impending orc.")
  time.sleep(1)
  if flower > 0:
    print ("\nYou quickly hold out the purple flower, somehow "
    "hoping it will stop the orc. It does! The orc was looking "
    "for love. "
    "\n\nThis got weird, but you survived!")
  else: #If the user didn't grab the sword
     print ("\nMaybe you should have picked up the flower. "
     "\n\nYou died!")
#_main_
svar_A = ["A", "a"]
svar_B = ["B", "b"]
svar_C = ["C", "c"]
Já = ["J", "j", "já", "JÁ", "Já"]
Nei = ["N", "n", "nei", "Nei", "NEI"]

counter = 100
intro()
