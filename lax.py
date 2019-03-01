class Lax(object):
    def __init__(self, nafn, aldur):
        self.nafn = nafn
        self.aldur = aldur

        def synda(self):
            print(self.nafn + " er að synda")

        def vera_godur(self):
            print(self.nafn + " er góður.")

        def aldur(self):
            print(self.nafn + "er {0} ára".format(self.aldur))
def main():
    robert=Lax("Robert", 5) #Gefa hlutinum nafn
    robert.vera_godur()

if __name__ == "__main__":
    main()
