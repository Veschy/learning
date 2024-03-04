class Supcap:
    '''
    суперконденсаторы
    '''
    def __init__(self, c, u1, u2):
        self.c = c
        self.u1 = u1
        self.u2 = u2
    
    def energy(self):
        e = self.c*(self.u1**2-self.u2**2)/2
        return e


modul111 = Supcap(83,102,51)
e = modul111.energy()
print(e)
# print(modul111.__dict__)
# print(Supcap.__dict__)

