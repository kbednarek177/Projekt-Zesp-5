
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
        
def postaw_flage(pozycja, plansza, ile_flag):
    x, y = pozycja #y - wiersz, x- kolumna
    if plansza.bomby - ile_flag < plansza.bomby:
        if plansza.wyswietlana[y][x] == 9: #flagę postawiono
            plansza.wyswietlana[y][x] = 10
            ile_flag -= 1
        elif plansza.wyswietlana[y][x] == 10: #flagę usunięto
            plansza.wyswietlana[y][x] = 9
            ile_flag += 1
    return ile_flag
        #funkcja która sprawdza, czy miejsce jedt zakryte, jeśli tak to daje/usuwa flagę
        #zmienia plansza.wyswietlana






