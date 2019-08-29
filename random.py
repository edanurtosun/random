import random
class Zar:
    kose = 6

    def at(self):
        return random.randint(1,self.kose)

class OnlukZar(Zar):
    kose = 10

benim_zarim = Zar()
print(benim_zarim.at())

benim_zarim_onluk = OnlukZar()
print(benim_zarim_onluk.at())
