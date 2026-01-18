from random import randint
class Plansza:

    def __init__(self, szer, wys, bomby):
        self.szerokosc = szer
        self.wysokosc = wys
        self.ilosc_bomb = bomby
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
    #funkcja która generuje planszę(tablicę) o wymiarach plansza.wysokosc i plansza.szerokosc, która ma plansza.ilosc_bomb bomb
    #funkcja zmienia plansza.tablica

def wygrana(plansza): #ewentualnie można dodać jakiś warunek z flagami 
    for y in range(plansza.wysokosc):
        for x in range(plansza.szerokosc):
            if plansza.tablica[y][x] != -1 and (plansza.wyswietlana[y][x] == 9 or plansza.wyswietlana[y][x] == 10):
                return False
    #jeśli wszystkie pola != -1 są odkryte to wygrana
    return True

def ruch(pozycja, plansza, ile_flag): #ile_flag - ile zostało, jeśli flaga usunięta to ile_flag += 1
    x, y = pozycja
    if(plansza.tablica[y][x] == -1):
        plansza.wyswietlana[y][x] = -2
        return 2, ile_flag
    if(plansza.wyswietlana[y][x] != 10): #trzeba odkryć sąsiadujące zera i jeśli usunięta flaga to ile_flag += 1
        plansza.wyswietlana[y][x] = plansza.tablica[y][x]
    if(wygrana(plansza)):
        return 1, ile_flag
    return 0, ile_flag
    #y - wiersz, x- kolumna
        #funkcja który sprawdza, czy można odkryć element, odkrywa i sprawdza czy partia jest wygrana/przegrana
        #funkcja zmienia plansza.wyswietlana
        
def postaw_flage(pozycja, plansza, ile_flag):
    x, y = pozycja #y - wiersz, x- kolumna
    if ile_flag > 0:
        if plansza.wyswietlana[y][x] == 9: #flagę postawiono
            plansza.wyswietlana[y][x] = 10
            ile_flag -= 1
        elif plansza.wyswietlana[y][x] == 10: #flagę usunięto
            plansza.wyswietlana[y][x] = 9
            ile_flag += 1
    return ile_flag
        #funkcja która sprawdza, czy miejsce jest zakryte, jeśli tak to daje/usuwa flagę
        #zmienia plansza.wyswietlana

def odkrywanie(pozycja, plansza, ile_flag):
    # rekurencyjne odkrywanie sąsiadujących pól o ile nie mają otaczających min
    x, y = pozycja
    if(plansza.wyswietlana[y][x] != 9):
        return
    ruch(pozycja, plansza, ile_flag)
    if(plansza.tablica[y][x] == 0):
        odkrywanie((x-1, y), plansza, ile_flag)
        odkrywanie((x+1, y), plansza, ile_flag)
        odkrywanie((x, y-1), plansza, ile_flag)
        odkrywanie((x, y+1), plansza, ile_flag)




