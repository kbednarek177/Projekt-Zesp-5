
class Plansza:

    def __init__(self, szer, wys, bomby):
        self.szer = szer
        self.wys = wys
        self.bomby = bomby
        self.plansza = [[0 for i in range(szer)] for j in range(wys)]  # plansza[wiersz][kolumna]
        self.wyswietlana = [[9 for i in range(szer)] for j in range(wys)]

def generowanie(plansza):
    pass
        #funkcja która generuje planszę(tablicę) o wymiarach plansza.wys i plansza.szer, która ma plansza.bomby bomb
        #funkcja zmienia plansza.plansza
        
def ruch(pozycja, plansza):
    x, y = pozycja #y - wiersz, x- kolumna
        #funkcja który sprawdza, czy można odkryć element, odkrywa i sprawdza czy partia jest wygrana/przegrana
        #funkcja zmienia plansza.wyswietlana
        
def postaw_flage(pozycja, plansza):
    x, y = pozycja #y - wiersz, x- kolumna
    if plansza.wyswietlana[y][x] == 9:
        plansza.wyswietlana[y][x] = 10
    elif plansza.wyswietlana[y][x] == 10:
        plansza.wyswietlana[y][x] = 9
        #funkcja która sprawdza, czy miejsce jedt zakryte, jeśli tak to daje/usuwa flagę
        #zmienia plansza.wyswietlana






