import time
import curses
from curses import wrapper

def rozgrywka(stdscr, poziom):
    wysokosc_ekranu, szerokosc_ekranu = stdscr.getmaxyx()   # pobieranie wymiarow ekranu, zeby wiedziec gdzie jest "prawy gorny rog"

    # te wartosci sa jeszcze do zmienienia ...
    if poziom == 'latwy':
        liczba_flag = 15
    elif poziom == 'sredni':
        liczba_flag = 30
    else:
        liczba_flag = 45

    zegar = curses.newwin(1, 20, 0, 0)    # zegar odliczajacy w sekundach
    zegar.refresh()

    okno_flagi = curses.newwin(1, 20, 0, szerokosc_ekranu - 20)    # 20 to szerokosc okna flagi

    stdscr.erase()
    stdscr.refresh()
 
    czas = 0
    start = time.time()

    while True:     # tutaj trzeba pracowac nad wyswietlaniem planszy
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

        if time.time() - start >= 1:
            czas = czas + 1
            start = time.time()

        try:    # zapobieganie blokowaniu sie gry
            klawisz = stdscr.getkey()
            if klawisz == 'q':
                break
            
            # (Tutaj w przyszlosci dodamy stawianie flag)
            # if klawisz == 'f':
            #     liczba_flag -= 1

        except:
            pass
            
        curses.napms(50)    # dodalam opoznienie by nie wykorzystywac 100% procesora
        

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