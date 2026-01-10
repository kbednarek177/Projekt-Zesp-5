from random import randint
class Plansza:

    def __init__(self, szer, wys, bomby):
        self.szerokosc = szer
        self.wysokosc = wys
        self.bomby = bomby
        self.tablica = [[0 for i in range(szer)] for j in range(wys)]  # tablica[wiersz][kolumna]
        self.wyswietlana = [[9 for i in range(szer)] for j in range(wys)]

def generowanie(plansza):
    # wypełnianie planszy bombami
    for k in range(plansza.ilosc_bomb):
        sel_x = randint(0, plansza.szerokosc-1)
        sel_y = randint(0, plansza.wysokosc-1)
        # rerollujemy wybór z tablicy aż trafimy na pole bez bomby
        while(plansza.tablica[sel_y][sel_x] == -1):
            sel_x = randint(0, plansza.szerokosc-1)
            sel_y = randint(0, plansza.wysokosc-1)
        plansza.tablica[sel_y][sel_x] = -1
        # i oraz j dają nam wszystkich sąsiadów pola, aby je uaktualnić
        for i in range(-1, 2):
            for j in range(-1, 2):
                # nie chcemy wyjść poza tablicę
                if(sel_x+i < 0 or sel_x+i >= plansza.wysokosc or sel_y+j < 0 or sel_y+j >= plansza.szerokosc):
                    continue
                # nie chcemy nadpisać min
                if(plansza.tablica[sel_y+j][sel_x+i] > -1):
                    plansza.tablica[sel_y+j][sel_x+i] += 1
    #funkcja która generuje planszę(tablicę) o wymiarach plansza.wys i plansza.szer, która ma plansza.bomby bomb
    #funkcja zmienia plansza.tablica
def wygrana(plansza):
    #placeholder
    return False
def ruch(pozycja, plansza):
    y, x = pozycja
    plansza.wyswietlana[y][x] = 1
    if(plansza.tablica[y][x] == -1):
        return 2
    if(plansza.wyswietlana[y][x] != 10):
        plansza.wyswietlana[y][x] = plansza.tablica[y][x]
    if(wygrana(plansza)):
        return 1
    return 0
    #y - wiersz, x- kolumna
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






