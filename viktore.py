def spurningar():
    print("Viktor er dularfullar maður og hefur ýmis leyndarmál að geyma. Þú færð 10 spurningar um Viktor og þarft að svara 5 af þeim rétt til þess að komast yfir á næsta þrep, ef þú nærð því ekki þá felluru úr skólanum!")
    spurning = "Fílar Viktor hávaða?"
    print(spurning)
    svar = input("Svar: ")
    if svar == "já":
        print("RÉTT!")
    else:
        print("RANGT")

def main():
    spurningar()

if __name__ == "__main__":
    main()
