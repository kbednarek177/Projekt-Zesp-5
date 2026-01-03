from random import randint

class Plansza:
    # tablica zawiera nasze dane o minach, display to ta, którą wyświetlamy użytkownikowi
    # (puste pole oznacza brak wiedzy o polu dla gracza)
    # pierwszy indeks to wysokość (współrzędna y), drugi indeks to szerokość (współrzędna x)
    tablica = []
    display = []
    def __init__(self, szerokosc, wysokosc, ilosc_bomb):
        # tworzenie planszy jako tablicy dwuwymiarowej
        for i in range(wysokosc):
            temp = []
            temp2 = []
            for j in range(szerokosc):
                temp.append(0)
                temp2.append(" ")
            self.tablica.append(temp)
            self.display.append(temp2)
        # wypełnianie planszy bombami
        for k in range(ilosc_bomb):
            sel_x = randint(0, szerokosc-1)
            sel_y = randint(0, wysokosc-1)
            # rerollujemy wybór z tablicy aż trafimy na pole bez bomby
            while(self.tablica[sel_y][sel_x] == -1):
                sel_x = randint(0, szerokosc-1)
                sel_y = randint(0, wysokosc-1)
            self.tablica[sel_y][sel_x] = -1
            # i oraz j dają nam wszystkich sąsiadów pola, aby je uaktualnić
            for i in range(-1, 2):
                for j in range(-1, 2):
                    # nie chcemy wyjść poza tablicę
                    if(sel_x+i < 0 or sel_x+i >= wysokosc or sel_y+j < 0 or sel_y+j >= szerokosc):
                        continue
                    # nie chcemy nadpisać min
                    if(self.tablica[sel_y+j][sel_x+i] > -1):
                        self.tablica[sel_y+j][sel_x+i] += 1
    # funkcja, która "wyświetla" użytkownikowi pole o współrzędnych x, y
    # należy ją wywołać za *każdym* razem gdy pola są wyświetlane dla gracza dla *każdego* pola wyświetlonego
    def toggled(self, x, y):
        stan = self.tablica[y][x]
        # zachęcam gorąco do zastąpienia znaków innymi wybranymi tak, aby wszystko ładnie wyglądało
        if(stan >= 0):
            self.display[y][x] = stan
        if(stan == -1):
            self.display[y][x] = "X"
        

