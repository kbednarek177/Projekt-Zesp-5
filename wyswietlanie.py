import time
import curses
from curses import wrapper

def rozgrywka(stdscr, poziom):

    zegar = curses.newwin(1, 20, 0, 0) #zegar odliczajacy sekundy
    zegar.refresh()

    stdscr.erase()
    stdscr.refresh()
 
    czas = 0
    start = time.time()
    while True:             #tutaj trzeba pracowac nad wyswietlaniem planszy
        zegar.erase()

        zegar.addstr(f"Time: {czas}")
        zegar.refresh()

        if time.time() - start >= 1:
            czas = czas + 1
            start = time.time()
        

def menu_glowne(stdscr):
    curses.curs_set(0)  # niech kursor sie nie wyswietla
    curses.start_color()  # dodaj kolory
    
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)

    stdscr.nodelay(True) #nie czeka na nacisniecie klawisza, dzieki czemu inne funkcje dzieja sie w tle
    
    menu = ['Nowa Gra', 'Wczytaj Gre', 'Zasady Gry', 'Wyjscie']
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

        elif klawisz == 'q': #cofnij - dokonczyc, gdy zrobimy zasady gry oraz logowanie
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
                pass #wczytaj zapamietana gdzies plansze
            elif wybrana_opcja == 'Zasady Gry':
                pass #Zrobic nowego windowa lub pada na zasady, ktore trzeba w README.md uzupelnic
            elif wybrana_opcja == poziomy[0]:
                rozgrywka(stdscr, 'latwy')
            elif wybrana_opcja == poziomy[1]:
                rozgrywka(stdscr, 'sredni')
            elif wybrana_opcja == poziomy[2]:
                rozgrywka(stdscr, 'trudny')

wrapper(menu_glowne)