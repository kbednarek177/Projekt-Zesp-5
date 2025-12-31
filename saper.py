import numpy as np

class Plansza:
    poziomy = {1:(0,0,0)} #poziom, który jest podawany przy inicjacji, po czym 3 wartości, odpowiednio: szerokosc, wysokosc i ilość bomb

    def __init__(self, poziom):
        self.poziom = poziom
        self.szer = self.poziomy[poziom][0]
        self.wys = self.poziomy[poziom][1]
        self.bomby = self.poziomy[poziom][2]
        self.plansza = np.zeros(self.wys,self.szer)
        self.odkryte = np.zeros(self.wys,self.szer)
        self.flagi = np.zeros(self.wys,self.szer)


def generowanie(plansza):
    pass
        #funkcja która generuje planszę(tablicę) o wymiarach self.wys i self.szer, która ma self.bomby bomb, gdzie żadna nie występuje w miejscu pirwszy_ruch.
        #funkcja zmienia self.plansza
        
def Ruch(pozycja, plansza):
    pass
        #funkcja który sprawdza, czy można odkryć element, odkrywa i sprawdza czy partia jest wygrana/przegrana, usuwa flagi w odkrytych polach
        #funkcja zmienia self.odkryte na podstawie self.plansza
        
def Postaw_Flage(pozycja, plansza):
    pass
        #funkcja która sprawdza, czy miejsce jedt odkryte, jeśli nie to daje/usuwa flagę((pole + 1)%2)
        #zmienia self.flagi






