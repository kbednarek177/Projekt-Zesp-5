import time
import curses
from curses import wrapper
from saper import postaw_flage, ruch, Plansza
# from konta import zapisz #aktualnie nie istnieje

def rozgrywka(stdscr, poziom):
    wysokosc_ekranu, szerokosc_ekranu = stdscr.getmaxyx()   # pobieranie wymiarow ekranu, zeby wiedziec gdzie jest "prawy gorny rog"

    # Tworzenie kolorow potrzebnych do wyswietlania planszy
    curses.init_pair(2, 238, 235)
    OdkrytePole = curses.color_pair(2)
    curses.init_pair(3, 235, 238)
    OdkrytePoleReverse = curses.color_pair(3)
    curses.init_pair(4, 4, 238)
    Liczba1 = curses.color_pair(4)
    curses.init_pair(5, 2, 238)
    Liczba2 = curses.color_pair(5)
    curses.init_pair(6, 9, 238)
    Liczba3 = curses.color_pair(6)
    curses.init_pair(7, 5, 238)
    Liczba4 = curses.color_pair(7)
    curses.init_pair(8, 1, 238)
    Liczba5 = curses.color_pair(8)
    curses.init_pair(9, 16, 238)
    Liczba6 = curses.color_pair(9)
    curses.init_pair(10, 0, 238)
    Liczba7 = curses.color_pair(10)
    curses.init_pair(11, 6, 238)
    Liczba8 = curses.color_pair(11)
    curses.init_pair(12, 9, 235)
    Flaga = curses.color_pair(12)
    curses.init_pair(13, 15, 235)
    Bomba = curses.color_pair(13)
    curses.init_pair(14, 1, 0)
    Obrys = curses.color_pair(14)
    curses.init_pair(15, 0, 9)
    Boom = curses.color_pair(15)
    curses.init_pair(16, curses.COLOR_BLACK, curses.COLOR_WHITE)
    Miganie = curses.color_pair(16)

    # ustalic z innymi czy ten sposob i wartosci beda ok, bo proszenie uzytkownika o wielkosc planszy jest trudniejsze
    if poziom == 'latwy':    # poziomy
        liczba_flag = 10
    elif poziom == 'sredni':
        liczba_flag = 40
    else:
        liczba_flag = 99

    zegar = curses.newwin(1, 20, 0, 0)    # zegar odliczajacy w sekundach
    zegar.refresh()

    okno_flagi = curses.newwin(1, 20, 0, szerokosc_ekranu - 20)    # 20 to szerokosc okna flagi

    stdscr.erase()
    stdscr.refresh()
 
    czas = 0
    start = time.time()
    
    # boki pojedynczego pola
    bokx = 3 
    boky = 1
    # wspolrzedne srodka pojedynczego pola numerujac od zera
    srodekx = 1
    srodeky = 0

    #tworzenie tymczasowej planszy aby sprobowac ja wyswietlic - zamiast tego pojawi sie tu potem wywolanie funkcji GENEROWANIE
    tablica = [[0, 0, 0, 2, 10, 10, 1, 0, 0], 
               [0, 0, -2, 2, 10, 1, 3, 0, 0], 
               [1, 2, 1, 1, 10, 1, 0, 0, 0], 
               [10, 10, 10, 10, 1, 3, 0, 0, 0], 
               [10, 10, 10, 10, 1, 9, 0, 0, 0], 
               [1, 1, 10, 10, 1, 2, 2, 1, 0], 
               [-1, 1, 10, 10, 10, 10, 10, 10, 0], 
               [0, 1, 10, 10, 10, 10, 10, 10, 00], 
               [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    # Liczba wierszy * wysokosc pola (bok+ramka)
    wys_planszy = len(tablica) * (boky + 1) 
    # Liczba kolumn * szerokosc pola (bok+ramka)
    szer_planszy = len(tablica[0]) * (bokx + 1)

    start_y = (wysokosc_ekranu // 2) - (wys_planszy // 2)
    start_x = (szerokosc_ekranu // 2) - (szer_planszy // 2)

    przykladowa_plansza = curses.newwin(wys_planszy, szer_planszy, start_y, start_x)
    
    szer, wys, bomby = 9,9,10
    plansza = Plansza(szer, wys, bomby)
    # do wyswietlenia: plansza.wyswietlana. plansza.wyzwietlana[y = wiersz][x = kolumna]
    
    #podswietlane pole
    pozycja = (0,0)  #(x = kolumna, y = wiersz)
    wynik = 0

    while not wynik:     # tutaj trzeba pracowac nad wyswietlaniem planszy 
        # ZEGAR:
        zegar.erase()

        sekundy = czas % 60          
        wszystkie_minuty = czas // 60 

        minuty = wszystkie_minuty % 60      
        godziny = wszystkie_minuty // 60
        
        zegar.addstr(f"Czas gry: {godziny:02}:{minuty:02}:{sekundy:02}")    # wyswietlanie czasu w formacie 00:00:00

        zegar.refresh()

        # FLAGI:
        okno_flagi.erase()

        tekst_flagi = f"Pozostale flagi: {liczba_flag}"
        okno_flagi.addstr(0, 0, tekst_flagi)

        okno_flagi.refresh()

        # AKTUALNY STAN PLANSZY
        przykladowa_plansza.erase()

        for rzad in range(len(tablica)):

            for kolumna in range(len(tablica[rzad])):    #Wypelniam prostokaty bokx na boky kolorami i symbolami przedstawiajacymi dane pole

                # pozycjax = rzad*(bokx+1)
                # pozycjay = kolumna*(boky+1)
                pozycjax = kolumna * (bokx + 1)
                pozycjay = rzad * (boky + 1)
                
                if tablica[rzad][kolumna] == 0: #Odkryte pole 

                    for i in range(boky):  

                        for j in range(bokx):

                            przykladowa_plansza.addstr(pozycjay+i, pozycjax+j, ' ', OdkrytePole) 

                elif tablica[rzad][kolumna] == 1: #Pole z jedna sasiadujaca bomba

                    for i in range(boky):

                        for j in range(bokx):

                            przykladowa_plansza.addstr(pozycjay+i, pozycjax+j, ' ', OdkrytePoleReverse)
                    
                    przykladowa_plansza.addstr(pozycjay+srodeky, pozycjax+srodekx, '1', Liczba1)

                elif tablica[rzad][kolumna] == 2:

                    for i in range(boky):

                        for j in range(bokx):

                            przykladowa_plansza.addstr(pozycjay+i, pozycjax+j, ' ', OdkrytePoleReverse)
                    
                    przykladowa_plansza.addstr(pozycjay+srodeky, pozycjax+srodekx, '2', Liczba2)

                elif tablica[rzad][kolumna] == 3:

                    for i in range(boky):

                        for j in range(bokx):

                            przykladowa_plansza.addstr(pozycjay+i, pozycjax+j, ' ', OdkrytePoleReverse)
                    
                    przykladowa_plansza.addstr(pozycjay+srodeky, pozycjax+srodekx, '3', Liczba3)

                elif tablica[rzad][kolumna] == 4:

                    for i in range(boky):

                        for j in range(bokx):

                            przykladowa_plansza.addstr(pozycjay+i, pozycjax+j, ' ', OdkrytePoleReverse)
                    
                    przykladowa_plansza.addstr(pozycjay+srodeky, pozycjax+srodekx, '4', Liczba4)

                elif tablica[rzad][kolumna] == 5:

                    for i in range(boky):

                        for j in range(bokx):

                            przykladowa_plansza.addstr(pozycjay+i, pozycjax+j, ' ', OdkrytePoleReverse)
                    
                    przykladowa_plansza.addstr(pozycjay+srodeky, pozycjax+srodekx, '5', Liczba5)

                elif tablica[rzad][kolumna] == 6:
                    
                    for i in range(boky):

                        for j in range(bokx):

                            przykladowa_plansza.addstr(pozycjay+i, pozycjax+j, ' ', OdkrytePoleReverse)
                    
                    przykladowa_plansza.addstr(pozycjay+srodeky, pozycjax+srodekx, '6', Liczba6)

                elif tablica[rzad][kolumna] == 7:
                    
                    for i in range(boky):

                        for j in range(bokx):

                            przykladowa_plansza.addstr(pozycjay+i, pozycjax+j, ' ', OdkrytePoleReverse)
                    
                    przykladowa_plansza.addstr(pozycjay+srodeky, pozycjax+srodekx, '7', Liczba7)

                elif tablica[rzad][kolumna] == 8:
                    
                    for i in range(boky):

                        for j in range(bokx):

                            przykladowa_plansza.addstr(pozycjay+i, pozycjax+j, ' ', OdkrytePoleReverse)
                    
                    przykladowa_plansza.addstr(pozycjay+srodeky, pozycjax+srodekx, '8', Liczba8)

                elif tablica[rzad][kolumna] == 9: #Oflagowane pole

                    for i in range(boky):

                        for j in range(bokx):

                            przykladowa_plansza.addstr(pozycjay+i, pozycjax+j, ' ', OdkrytePole) 
                    
                    przykladowa_plansza.addstr(pozycjay+srodeky, pozycjax+srodekx, '⚑', Flaga)

                elif tablica[rzad][kolumna] == 10: #Zakryte pole
                    
                    for i in range(boky):

                        for j in range(bokx):

                            przykladowa_plansza.addstr(pozycjay+i, pozycjax+j, ' ', OdkrytePoleReverse)

                elif tablica[rzad][kolumna] == -1: #Bomba
                    
                    for i in range(boky):

                        for j in range(bokx):

                            przykladowa_plansza.addstr(pozycjay+i, pozycjax+j, ' ', OdkrytePole)
                    
                    przykladowa_plansza.addstr(pozycjay+srodeky, pozycjax+srodekx, '◉', Bomba)

                elif tablica[rzad][kolumna] == -2: #Uzytkownik trafil na bombe
                    
                    for i in range(boky):

                        for j in range(bokx):

                            przykladowa_plansza.addstr(pozycjay+i, pozycjax+j, ' ', Boom)
                    
                    przykladowa_plansza.addstr(pozycjay+srodeky, pozycjax+srodekx, '◉', Boom)
        
        # MIGAJACE POLA - GRY UZYTKOWNIK JEST NA DANYM POLU TO ONO  'MIGA'

        if int(time.time() * 2) % 2:
            px_gracza = pozycja[0] * (bokx + 1)
            py_gracza = pozycja[1] * (boky + 1)
            
            wartosc_pola = tablica[pozycja[1]][pozycja[0]]
            znak_do_wyswietlenia = ' '
            
            if wartosc_pola == 9:
                znak_do_wyswietlenia = '⚑'
            elif wartosc_pola == -1 or wartosc_pola == -2:
                znak_do_wyswietlenia = '◉'
            elif 1 <= wartosc_pola <= 8:
                znak_do_wyswietlenia = str(wartosc_pola)
            
            for i in range(boky):
                for j in range(bokx):
                    przykladowa_plansza.addstr(py_gracza + i, px_gracza + j, ' ', Miganie)
            
            if znak_do_wyswietlenia != ' ':
                przykladowa_plansza.addstr(py_gracza + srodeky, px_gracza + srodekx, znak_do_wyswietlenia, Miganie)

        przykladowa_plansza.refresh()

        # AKTUALIZOWANIE WSZYSTKIEGO I ODCZYTYWANIE POSUNIEC UZYTOWNIKA
        if time.time() - start >= 1:
            czas = czas + 1
            start = time.time()

        try:    # zapobieganie blokowaniu sie gry
            klawisz = stdscr.getkey()
        except:
            klawisz = None
       
        #STEROWANIE
        if klawisz == 'q':
            break
            #skoncz gre / wyjdz do menu

        elif klawisz == 'z':
            pass
            # zapisz(plansza) # aktualnie nie istnieje
            # wypisz "zapisano"??
            # zapisuje plansze

        # PORUSZANIE SIE AWSD
        elif klawisz == 'KEY_LEFT':
            pozycja = ((pozycja[0]-1)%plansza.szer, pozycja[1])
            
        elif klawisz == 'KEY_DOWN':
            pozycja = ((pozycja[0]), (pozycja[1]+1)%plansza.wys)
            
        elif klawisz == 'KEY_UP':
            pozycja = ((pozycja[0]), (pozycja[1]-1)%plansza.wys) 
            
        elif klawisz == 'KEY_RIGHT':
            pozycja = ((pozycja[0]+1)%plansza.szer, pozycja[1])
            
        # STAWIANIE FLAG
        elif klawisz == 'f':
            liczba_flag = postaw_flage(pozycja, plansza,liczba_flag)
            
        # (tu Agatka) nie rozumiem co robi to 'e' :(

        # if key == ord('e'): # funkcja bedzie zwracac 0 - kontynuacja, 1 - wygrana, 2 - przegrana
        #     wynik = ruch(pozycja, plansza) # jesli wygrana lub przegrana to przerwie petle gry

        # mozliwy automatyczny restart??    
        # if key == ord('r'):
        #     pass
        #     # koniec i poczatek nowej rozgrywki, restart
            
        curses.napms(50)    # dodalam opoznienie by nie wykorzystywac 100% procesora

    # poza petla, trzeba sprawdzic wartosc wynik. Jesli wynik = 1: wywolac wygrana(). Jesli wynik = 2: wywolac przegrana()
        

def menu_glowne(stdscr):
    curses.curs_set(0)  # niech kursor sie nie wyswietla
    curses.start_color()  # dodaj kolory
    
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)

    stdscr.nodelay(True) # nie czeka na nacisniecie klawisza, dzieki czemu inne funkcje dzieja sie w tle

    #stdscr.timeout(50) -> mozliwe ze to by bylo lepsze zamiast nodelay + napms ???
    
    menu = ['Nowa Gra', 'Wczytaj Gre', 'Ranking', 'Zasady Gry', 'Wyjscie']
    poziomy = ['Latwy  ★☆☆☆☆ ', 'Sredni ★★★☆☆ ', 'Trudny ★★★★★ ']
    tytuly = ["--- SAPER ---", "--- POZIOMY ---"]
    ekran = [menu, poziomy]
    iterator = 0
    obecny_rzad = 0

    while True:
        stdscr.erase()
        
        wysokosc, szerokosc = stdscr.getmaxyx() # pobiera informacje o wysokosci i szerokosci okna terminala
        
        stdscr.addstr(wysokosc // 2 - len(ekran[iterator]) // 2 - 2, szerokosc // 2 - len(tytuly[iterator]) // 2, tytuly[iterator], curses.A_BOLD)

        for indeks, rzad in enumerate(ekran[iterator]):
            x = szerokosc // 2 - len(rzad) // 2
            y = wysokosc // 2 - len(ekran[iterator]) // 2 + indeks  # w curses nie da sie chyba ustawic napisu na wspolrzednej float, wiec jest krzywo
            
            if indeks == obecny_rzad:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, rzad)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, rzad)

        stdscr.refresh()

        try:            # jesli uzytkownik nic nie klika to klawisz = None, aby nie crashowalo
            klawisz = stdscr.getkey()
        except:
            klawisz = None

        if klawisz == 'KEY_UP':
            obecny_rzad = (obecny_rzad - 1) % len(ekran[iterator])
            
        elif klawisz == 'KEY_DOWN':
            obecny_rzad = (obecny_rzad + 1) % len(ekran[iterator])

        elif klawisz == 'q': # cofnij - dokonczyc, gdy zrobimy zasady gry oraz logowanie
            if iterator == 1:
                stdscr.clear()
                iterator = 0
            
        elif klawisz == '\n':
            wybrana_opcja = ekran[iterator][obecny_rzad]
            
            if wybrana_opcja == 'Wyjscie':
                break
            
            elif wybrana_opcja == 'Nowa Gra':
                stdscr.clear()
                iterator = 1

            elif wybrana_opcja == 'Wczytaj Gre':
                pass # wczytaj zapamietana gdzies plansze
            
            elif wybrana_opcja == 'Zasady Gry':
                pass # Zrobic nowego windowa lub pada na zasady, ktore trzeba w README.md uzupelnic
            
            elif wybrana_opcja == poziomy[0]:
                rozgrywka(stdscr, 'latwy')

            elif wybrana_opcja == poziomy[1]:
                rozgrywka(stdscr, 'sredni')

            elif wybrana_opcja == poziomy[2]:
                rozgrywka(stdscr, 'trudny')

wrapper(menu_glowne)