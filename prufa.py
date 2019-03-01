class Viktor(object):
    def __init__(self, nafn, aldur):
        self.nafn = nafn
        self.aldur = aldur

    def synda(self):
        print(self.nafn + "er að senda")

    def vera_godur(self):
        print(self.nafn + " er góður.")
        self.aldur()

    def aldur(self):
        print(self.nafn + "er {0} ára".format(self.aldur))

def main():
    robert=Lax("Robert", 5) #Gefa hlutinum nafn
    robert.vera_godur()
    aslaug=Lax("Aslaug", 4)
    aslaug.synda()

if __name__ == "__main__":
    main()
