import curses
from curses import wrapper

def menu_glowne(stdscr):
    curses.curs_set(0)  # niech kursor sie nie wyswietla
    curses.start_color()  # dodaj kolory
    
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
    
    menu = ['Nowa Gra', 'Wczytaj Gre', 'Zasady Gry', 'Wyjscie']
    obecny_rzad = 0

    while True:
        stdscr.clear()
        
        wysokosc, szerokosc = stdscr.getmaxyx() # pobiera informacje o wysokosci i szerokosci okna terminala
        
        tytul = "--- SAPER ---"
        stdscr.addstr(wysokosc // 2 - len(menu) // 2 - 2, szerokosc // 2 - len(tytul) // 2, tytul, curses.A_BOLD)

        for indeks, rzad in enumerate(menu):
            x = szerokosc // 2 - len(rzad) // 2
            y = wysokosc // 2 - len(menu) // 2 + indeks
            
            if indeks == obecny_rzad:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, rzad)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, rzad)

        stdscr.refresh()

        klawisz = stdscr.getkey()

        if klawisz == 'KEY_UP':
            obecny_rzad = (obecny_rzad - 1) % len(menu)
            
        elif klawisz == 'KEY_DOWN':
            obecny_rzad = (obecny_rzad + 1) % len(menu)
            
        elif klawisz == '\n':
            wybrana_opcja = menu[obecny_rzad]
            
            if wybrana_opcja == 'Wyjscie':
                break
            elif wybrana_opcja == 'Nowa Gra':
                stdscr.clear()
                stdscr.addstr(0, 0, "Tu uruchomi sie gra... Nacisnij cos by wrocic.")
                stdscr.getch()

wrapper(menu_glowne)