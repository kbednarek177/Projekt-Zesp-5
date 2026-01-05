from random import randint
# READ ME
# Plik ten zawiera klasę Plansza która będzie wykorzystywana podczas gry
# klasa zawiera:

# trzy tablice dwuwymiarowe o rozmiarach szerokość x wysokość
    # tablica, czyli dane o tym, czy pole jest bombą lub ile jest sąsiadujących bomb
    # odkryte, czyli dane o tym, które pola zostały już odkryte przez użytkownika w trakcie gry
    # display, czyli wersja tablicy gotowa do wyświetlenia graczowi
# informacje o tym czy na polu jest flaga czy nie zawarte są w tablicy 'display'

# parametry planszy
    # pozostale_bomby, czyli liczba bomb nieoznaczonych jeszcze flagami
    # szerokosc
    # wysokosc
    # ilosc_bomb, czyli ile bomb zawiera nasza plansza

# metody planszy
    # zmien, ustawia parametry planszy na liczby na wejsciu w formacie szerokość, wysokość, ilość bomb
    # generuj, generuje nową planszę w oparciu o ówczesne parametry planszy
    # wczytaj, wczytuje planszę z poprzedniej gry [Jeszcze niegotowe]
    # wyswietl, wypisuje na terminal planszę (tablicę display)
    # przegrana, wywoływana po przegraniu gry (czyli przez odkrycie pola z miną)
    # wygrana, wywoływana po wygraniu gry (czyli oflagowaniu każdego pola z miną)
    # postaw_flage, zmienia display dodając/usuwając flagę, aktualizuje także wartość parametru pozostale_bomby
    # odkryj, odkrywa podane pole i konczy gre jeśli wybraliśmy minę
    # wykonaj_ruch, rekurencyjnie odkrywa spójny 'region' planszy złożony z sąsiadujących pól o wartości '0' oraz otaczających ich pól
class Plansza:
    # pierwszy indeks to wysokość (współrzędna y), drugi indeks to szerokość (współrzędna x)
    tablica = []
    odkryte = []
    display = []
    pozostale_bomby = 0
    szerokosc = 0
    wysokosc = 0
    ilosc_bomb = 0
    # aktualizacja parametrow
    def zmien(self, szer, wys, il_bomb):
        self.szerokosc = szer
        self.wysokosc = wys
        self.ilosc_bomb = il_bomb
    # generowanie planszy
    def generuj(self):
        pozostale_bomby = self.ilosc_bomb
        # tworzenie planszy jako tablicy dwuwymiarowej
        # tablica i odkryte
        for i in range(self.wysokosc):
            temp = []
            temp2 = []
            for j in range(self.szerokosc):
                temp.append(0)
                temp2.append(" ")
            self.tablica.append(temp)
            self.display.append(temp2)
            self.odkryte.append(temp)
        # wypełnianie planszy bombami
        for k in range(self.ilosc_bomb):
            sel_x = randint(0, self.szerokosc-1)
            sel_y = randint(0, self.wysokosc-1)
            # rerollujemy wybór z tablicy aż trafimy na pole bez bomby
            while(self.tablica[sel_y][sel_x] == -1):
                sel_x = randint(0, self.szerokosc-1)
                sel_y = randint(0, self.wysokosc-1)
            self.tablica[sel_y][sel_x] = -1
            # i oraz j dają nam wszystkich sąsiadów pola, aby je uaktualnić
            for i in range(-1, 2):
                for j in range(-1, 2):
                    # nie chcemy wyjść poza tablicę
                    if(sel_x+i < 0 or sel_x+i >= self.wysokosc or sel_y+j < 0 or sel_y+j >= self.szerokosc):
                        continue
                    # nie chcemy nadpisać min
                    if(self.tablica[sel_y+j][sel_x+i] > -1):
                        self.tablica[sel_y+j][sel_x+i] += 1
    def wczytaj(self):
        pass
    def wyswietl(self):
        for i in range(self.wysokosc):
            for j in range(self.szerokosc):
                print(self.display[i][j], end="")
            print()
        print("test")
        for i in range(self.wysokosc):
            for j in range(self.szerokosc):
                if(self.tablica[i][j] == -1):
                    print("x", end="")
                else:
                    print(self.tablica[i][j], end="")
            print()
    def przegrana(self):
        pass
    def wygrana(self):
        pass
    flag_character = "F"
    def postaw_flage(self, x, y):
        # znak F to placeholder na znak flagi
        # jeśli flaga już jest to ją usuwamy zamiast jej dodawać
        if(self.display[y][x] == self.flag_character):
            # patrzymy, czy pole pod flagą było ukryte
            if(self.odkryte[y][x] == 0):
                self.display[y][x] == " "
            else:
                # nie przejmujemy się że odkrywamy to pole
                # skoro już było kiedyś odkryte i dalej gramy
                # to znaczy, że w środku nie ma bomby
                self.odkryj(self, x, y)
        # umieszczamy flagę
        self.display[y][x] = self.flag_character
        # postawienie flagi na bombie zmniejsza 'pozostale bomby' o 1
        # gdy pozostale bomby wynosi 0 to gra sie konczy, jako ze oznaczylismy wszystkie bomby flagami
        if(self.tablica[y][x] == -1):
            self.pozostale_bomby -= 1
            if(self.pozostale_bomby == 0):
                self.wygrana()
    # funkcja która zmienia odkryte oraz display na wybranym polu
    def odkryj(self, x, y):
        self.odkryte[y][x] = 1
        if(self.tablica[y][x] == -1):
            self.przegrana()
            return
        if(self.display[y][x] != self.flag_character):
            self.display[y][x] = self.tablica[y][x]
    # funkcja która wykonuje ruch na planszy (tj. odkrywa wszystkie pola które powinny być odkryte po kliknięciu pola)
    def wykonaj_ruch(self, x, y):
        self.odkryj(x, y)
        # poniższa pętla rekurencyjnie wykonuje wykonaj_ruch dla wszystkich pól o wartości '0' sąsiednich min
        # zgodnie z zasadami zwyczajnego sapera
        if(self.tablica[y][x] == 0):
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if(x+i < 0 or x+i >= self.wysokosc or y+j < 0 or y+j >= self.szerokosc):
                        continue
                    if(self.odkryte[y+j][x+i] == 1):
                        continue
                    self.wykonaj_ruch(x+i, y+j)
        
P = Plansza()
P.zmien(6, 6, 6)
P.generuj()
P.odkryj(0, 0)
while(True):
    x = input()
    y = input()
    if(x == -1 or y == -1):
        break
    P.odkryj(int(x), int(y))
    P.wyswietl()