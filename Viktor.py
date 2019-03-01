class Viktor(object):
    def __init__(self, spurning, svar):
        self.spurning = spurning
        self.svar = svar

    def spur(self):
        print(self.spurning)

    def sva(self):
        print(self.svar)

def main():
    spurningin=Viktor("Fílar Viktor hávaða?", "Nei") #Gefa hlutinum nafn
    spurningin.spur()
    spurningin.sva()

if __name__ == "__main__":
    main()
