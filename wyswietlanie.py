import time
import curses
from curses import wrapper
from saper import postaw_flage, ruch, Plansza
# from konta import zapisz #aktualnie nie istnieje
#from curses.textpad import rectangle

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
    curses.init_pair(13, 202, 238)
    Bomba = curses.color_pair(13)


    # ustalic z innymi czy ten sposób i wartosci beda ok, bo proszenie uzytkownika o wielkosc planszy jest trudniejsze
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

    #tworzenie tymczasowej planszy aby spróbowac ja wyswietlic - zamiast tego pojawi sie tu potem wywolanie funkcji GENEROWANIE
    przykladowa_plansza = curses.newwin(10, 27, wysokosc_ekranu//2 - 4, szerokosc_ekranu//2 - 13) # jest o jedną za dużo linie (10 zamiast 9), bo z jakiegoś powodu program jej potrzebuje???
    przykladowa_plansza.refresh()
    tablica = [[10, 10, 10, 10, 10, 10, 10, 10, 10], 
               [10, 0, 0, 0, 0, 0, 0, 0, 10], 
               [10, 10, 10, 10, 10, 10, 10, 10, 10], 
               [10, 10, 1, 10, 5, 10, 9, 10, 10], 
               [10, 10, 2, 10, 6, 10, 9, 10, 10], 
               [10, 10, 3, 10, 7, 10, -1, 10, 10], 
               [10, 10, 4, 10, 8, 10, -1, 10, 10], 
               [10, 10, 10, 10, 10, 10, 10, 10, 10], 
               [10, 10, 10, 10, 10, 10, 10, 10, 10]]
    
    #zainicjowana plansza. na razie nic nie robi.
    szer, wys, bomby = 9,9,10
    plansza = Plansza(szer, wys, bomby)
    # do wyswietlenia: plansza.wyswietlana. plansza.wyzwietlana[y = wiersz][x = kolumna]
    
    #boki pojedynczego pola
    bokx = 3 
    boky = 1
    #wspolrzedne srodka pojedynczego pola numerujac od zera
    srodekx = 1
    srodeky = 0

    #podświetlane pole
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

        # dodac rysowanie siatki obrysow za pomoca funkcji rectangle

        for rzad in range(len(tablica)):

            for kolumna in range(len(tablica[rzad])):    #Wypelniam prostokaty bokx na boky kolorami i symbolami przedstawiajacymi dane pole

                if tablica[rzad][kolumna] == 0: #Odkryte pole 

                    for i in range(boky):  

                        for j in range(bokx):

                            przykladowa_plansza.addstr(kolumna*boky+i, rzad*bokx+j, ' ', OdkrytePole) 

                elif tablica[rzad][kolumna] == 1: #Pole z jedna sasiadujaca bomba

                    for i in range(boky):

                        for j in range(bokx):

                            przykladowa_plansza.addstr(kolumna*boky+i, rzad*bokx+j, ' ', OdkrytePoleReverse)
                    
                    przykladowa_plansza.addstr(kolumna*boky+srodeky, rzad*bokx+srodekx, '1', Liczba1)

                elif tablica[rzad][kolumna] == 2:

                    for i in range(boky):

                        for j in range(bokx):

                            przykladowa_plansza.addstr(kolumna*boky+i, rzad*bokx+j, ' ', OdkrytePoleReverse)
                    
                    przykladowa_plansza.addstr(kolumna*boky+srodeky, rzad*bokx+srodekx, '2', Liczba2)

                elif tablica[rzad][kolumna] == 3:

                    for i in range(boky):

                        for j in range(bokx):

                            przykladowa_plansza.addstr(kolumna*boky+i, rzad*bokx+j, ' ', OdkrytePoleReverse)
                    
                    przykladowa_plansza.addstr(kolumna*boky+srodeky, rzad*bokx+srodekx, '3', Liczba3)

                elif tablica[rzad][kolumna] == 4:

                    for i in range(boky):

                        for j in range(bokx):

                            przykladowa_plansza.addstr(kolumna*boky+i, rzad*bokx+j, ' ', OdkrytePoleReverse)
                    
                    przykladowa_plansza.addstr(kolumna*boky+srodeky, rzad*bokx+srodekx, '4', Liczba4)

                elif tablica[rzad][kolumna] == 5:

                    for i in range(boky):

                        for j in range(bokx):

                            przykladowa_plansza.addstr(kolumna*boky+i, rzad*bokx+j, ' ', OdkrytePoleReverse)
                    
                    przykladowa_plansza.addstr(kolumna*boky+srodeky, rzad*bokx+srodekx, '5', Liczba5)

                elif tablica[rzad][kolumna] == 6:
                    
                    for i in range(boky):

                        for j in range(bokx):

                            przykladowa_plansza.addstr(kolumna*boky+i, rzad*bokx+j, ' ', OdkrytePoleReverse)
                    
                    przykladowa_plansza.addstr(kolumna*boky+srodeky, rzad*bokx+srodekx, '6', Liczba6)

                elif tablica[rzad][kolumna] == 7:
                    
                    for i in range(boky):

                        for j in range(bokx):

                            przykladowa_plansza.addstr(kolumna*boky+i, rzad*bokx+j, ' ', OdkrytePoleReverse)
                    
                    przykladowa_plansza.addstr(kolumna*boky+srodeky, rzad*bokx+srodekx, '7', Liczba7)

                elif tablica[rzad][kolumna] == 8:
                    
                    for i in range(boky):

                        for j in range(bokx):

                            przykladowa_plansza.addstr(kolumna*boky+i, rzad*bokx+j, ' ', OdkrytePoleReverse)
                    
                    przykladowa_plansza.addstr(kolumna*boky+srodeky, rzad*bokx+srodekx, '8', Liczba8)

                elif tablica[rzad][kolumna] == 9: #Oflagowane pole

                    for i in range(boky):

                        for j in range(bokx):

                            przykladowa_plansza.addstr(kolumna*boky+i, rzad*bokx+j, ' ', OdkrytePole) 
                    
                    przykladowa_plansza.addch(kolumna*boky+srodeky, rzad*bokx+srodekx, '⚑', Flaga)

                elif tablica[rzad][kolumna] == 10: #Zakryte pole
                    
                    for i in range(boky):

                        for j in range(bokx):

                            przykladowa_plansza.addstr(kolumna*boky+i, rzad*bokx+j, ' ', OdkrytePoleReverse)

                elif tablica[rzad][kolumna] == -1: #Bomba
                    
                    for i in range(boky):

                        for j in range(bokx):

                            przykladowa_plansza.addstr(kolumna*boky+i, rzad*bokx+j, ' ', OdkrytePoleReverse)
                    
                    przykladowa_plansza.addch(kolumna*boky+srodeky, rzad*bokx+srodekx, '✸', Bomba)
        
        przykladowa_plansza.refresh()

        # AKTUALIZOWANIE WSZYSTKIEGO I ODCZYTYWANIE POSUNIEC UZYTOWNIKA
        if time.time() - start >= 1:
            czas = czas + 1
            start = time.time()

        try:    # zapobieganie blokowaniu sie gry
            key = stdscr.getkey()
       
            #STEROWANIE
            if key == curses.esc:
                break
                #skończ grę/ wyjdź do menu

            elif key == ord('c'):
                pass
                # zapisz(plansza) #aktualnie nie istnieje
                #wypisz "zapisano"??
                #zapisuje planszę

            #PORUSZANIE SIĘ AWSD
            elif key == ord('a'):
                pozycja = ((pozycja[0]-1)%plansza.szer, pozycja[1])
                return True, pozycja
            
            elif key == ord('w'):
                pozycja = ((pozycja[0]), (pozycja[1]+1)%plansza.wys)
                return True, pozycja
            
            elif key == ord('s'):
                pozycja = ((pozycja[0]), (pozycja[1]-1)%plansza.wys)
                return True, pozycja
            
            elif key == ord('d'):
                pozycja = ((pozycja[0]+1)%plansza.szer, pozycja[1])
                return True, pozycja
            
            #INTERAKCJA E I Q
            elif key == ord('q'):
                liczba_flag = postaw_flage(pozycja, plansza,liczba_flag)
            
            # if key == ord('e'): #funkcja będzie zwracać 0 - kontynuacja, 1 - wygrana, 2 - przegrana
            #     wynik = ruch(pozycja, plansza) #jeśli wygrana lub przegrana to przerwie pętlę gry

            #możliwy automatyczny restart??    
            # if key == ord('r'):
            #     pass
            #     #koniec i początek nowej rozgrywki, restart

        except:
            pass

            
        curses.napms(50)    # dodalam opoznienie by nie wykorzystywac 100% procesora

    #poza pętlą, trzeba sprawdzić wartość wynik. Jeśli wynik = 1: wywołać wygrana(). Jeśli wynik = 2: wywołać przegrana()
        

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