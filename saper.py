
class Plansza:
    
    def __init__(self, szer, wys, bomby):
        self.szer = szer
        self.wys = wys
        self.bomby = bomby
        self.plansza = [[0 for i in range(szer)] for j in range(wys)]  # plansza[wiersz][kolumna]
        self.wyswietlana = [[0 for i in range(szer)] for j in range(wys)]

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






