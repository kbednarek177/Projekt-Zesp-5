import time
import curses
from curses import wrapper
from saper import generowanie, postaw_flage, ruch, Plansza
from curses.textpad import Textbox
# from konta import zapisz #aktualnie nie istnieje

def rozgrywka(stdscr, plansza, liczba_flag):
    wysokosc_ekranu, szerokosc_ekranu = stdscr.getmaxyx()   # pobieranie wymiarow ekranu, zeby wiedziec gdzie jest "prawy gorny rog"
    klawisze_ruchu = {"w", "a", "s", "d", "W", "A", "S", "D", "KEY_UP", "KEY_DOWN", "KEY_LEFT", "KEY_RIGHT"}

    # Tworzenie kolorow potrzebnych do wyswietlania planszy
    curses.init_pair(2, 238, 235)
    ZakrytePole = curses.color_pair(2)
    curses.init_pair(3, 235, 238)
    OdkrytePole = curses.color_pair(3)
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
    curses.init_pair(15, 0, 9)
    Boom = curses.color_pair(15)
    curses.init_pair(16, curses.COLOR_BLACK, curses.COLOR_WHITE)
    Miganie = curses.color_pair(16)


    # instrukcja na dole ekranu
    instrukcja = curses.newwin(2, szerokosc_ekranu, wysokosc_ekranu - 2, 0)
    instrukcja.refresh()

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

    #tworzenie tymczasowej planszy aby sprobowac ja wyswietlic
    '''
    tablica = [[9, 9, 9, 2, 0, 0, 1, 9, 9], 
               [9, 9, -2, 2, 0, 1, 3, 9, 9], 
               [1, 2, 1, 1, 0, 1, 9, 9, 9], 
               [0, 0, 0, 0, 1, 3, 9, 9, 9], 
               [0, 0, 0, 0, 1, 10, 9, 9, 9], 
               [1, 1, 0, 0, 1, 2, 2, 1, 9], 
               [-1, 1, 0, 0, 0, 0, 0, 0, 9], 
               [9, 1, 0, 0, 0, 0, 0, 0, 9], 
               [9, 9, 9, 9, 9, 9, 9, 9, 9]]
    
    # Liczba wierszy * wysokosc pola (bok+ramka)
    wys_planszy = len(tablica) * (boky + 1) 
    # Liczba kolumn * szerokosc pola (bok+ramka)
    szer_planszy = len(tablica[0]) * (bokx + 1)

    start_y = (wysokosc_ekranu // 2) - (wys_planszy // 2)
    start_x = (szerokosc_ekranu // 2) - (szer_planszy // 2)

    przykladowa_plansza = curses.newwin(wys_planszy, szer_planszy, start_y, start_x)
    '''
    #przeniesione do menu:
    # if poziom == 'latwy':    # poziomy
    #     szer, wys, bomby = 9,9,10
    #     liczba_flag = 10
    # elif poziom == 'sredni':
    #     szer, wys, bomby = 11,11,18
    #     liczba_flag = 40
    # else:
    #     szer, wys, bomby = 13,13,35
    #     liczba_flag = 99

    # #tworzenie planszy do gry
    # plansza = Plansza(szer, wys, bomby)
    # generowanie(plansza)

    wys,szer = plansza.wysokosc, plansza.szerokosc

    wys_okna = wys * (boky + 1)
    szer_okna = szer * (bokx + 1)

    start_y = (wysokosc_ekranu // 2) - (wys_okna // 2)
    start_x = (szerokosc_ekranu // 2) - (szer_okna // 2)

    okno_planszy = curses.newwin(wys_okna, szer_okna, start_y, start_x)
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


        # INSTRUKCJA
        instrukcja.erase()
        try:
            tekst1 = "[A][W][S][D]/STRZALKI - poruszanie sie"
            tekst2 = "[F] - flaga, [E] - odkryj pole, [Z] - zapisz, [Q] - wyjdz"
            
            # srodek wzgledem calego ekranu
            x1 = max(0, (szerokosc_ekranu // 2) - (len(tekst1) // 2))
            x2 = max(0, (szerokosc_ekranu // 2) - (len(tekst2) // 2))

            instrukcja.addstr(0, x1, tekst1, curses.COLOR_WHITE)
            instrukcja.addstr(1, x2, tekst2, curses.COLOR_WHITE)
        except:
            pass
        instrukcja.refresh()

        
        # AKTUALNY STAN PLANSZY
        okno_planszy.erase()

        kolory_liczb = {
            1: Liczba1, 2: Liczba2, 3: Liczba3, 4: Liczba4,
            5: Liczba5, 6: Liczba6, 7: Liczba7, 8: Liczba8
        }

        for rzad in range(szer):
            for kolumna in range(wys):

                pozycjax = kolumna * (bokx + 1)
                pozycjay = rzad * (boky + 1)
                
                wartosc = plansza.wyswietlana[rzad][kolumna]
                
                bg_style = OdkrytePole      
                znak = ' '                  
                znak_style = OdkrytePole    

                if 1 <= wartosc <= 8:       
                    znak = str(wartosc)
                    znak_style = kolory_liczb[wartosc]
                
                elif wartosc == 9:          
                    bg_style = ZakrytePole
                
                elif wartosc == 10:         
                    bg_style = ZakrytePole
                    znak = '⚑'
                    znak_style = Flaga
                
                elif wartosc == -1:         
                    bg_style = ZakrytePole
                    znak = '◉'
                    znak_style = Bomba
                
                elif wartosc == -2:         
                    bg_style = Boom
                    znak = '◉'
                    znak_style = Boom

                for i in range(boky):
                    for j in range(bokx):
                        okno_planszy.addstr(pozycjay+i, pozycjax+j, ' ', bg_style)
                
                if znak != ' ':
                    okno_planszy.addstr(pozycjay+srodeky, pozycjax+srodekx, znak, znak_style)

        try:    # zapobieganie blokowaniu sie gry
            klawisz = stdscr.getkey() # nasluchiwanie ruchow uzytkownika
        except:
            klawisz = None
        

        # MIGAJACE POLA - GRY UZYTKOWNIK JEST NA DANYM POLU TO ONO 'MIGA'

        if int(time.time() * 2) % 2 or klawisz in klawisze_ruchu:
            px_gracza = pozycja[0] * (bokx + 1)
            py_gracza = pozycja[1] * (boky + 1)
            
            wartosc_pola = plansza.wyswietlana[pozycja[1]][pozycja[0]]
            znak_do_wyswietlenia = ' '
            
            if wartosc_pola == 10:
                znak_do_wyswietlenia = '⚑'
            elif wartosc_pola == -1 or wartosc_pola == -2:
                znak_do_wyswietlenia = '◉'
            elif 1 <= wartosc_pola <= 8:
                znak_do_wyswietlenia = str(wartosc_pola)
            
            for i in range(boky):
                for j in range(bokx):
                    okno_planszy.addstr(py_gracza + i, px_gracza + j, ' ', Miganie)
            
            if znak_do_wyswietlenia != ' ':
                okno_planszy.addstr(py_gracza + srodeky, px_gracza + srodekx, znak_do_wyswietlenia, Miganie)

        okno_planszy.refresh()


        # AKTUALIZOWANIE WSZYSTKIEGO I ODCZYTYWANIE POSUNIEC UZYTOWNIKA
        if time.time() - start >= 1:
            czas = czas + 1
            start = time.time()
       

        #STEROWANIE
        if klawisz == 'q' or klawisz == 'Q':
            break
            #skoncz gre / wyjdz do menu

        elif klawisz == 'z' or klawisz == 'Z':
            pass
            # if czy_zalogowano == True:
            #     zapisz(plansza.tablica, plansza.wyswietlana, liczba_flag, czas)
            #     wypisz "zapisano"??
            # zapisuje plansze

            # if czy_zalogowano == True:
            #       przekaz_zuzi_plansze()
            #       wyswietl_zapisano() - w boxie, gdzies na dole ...


        # PORUSZANIE SIE
        elif klawisz == 'KEY_LEFT' or klawisz == 'a' or klawisz == 'A':
            pozycja = ((pozycja[0]-1)%szer, pozycja[1])
            
        elif klawisz == 'KEY_DOWN' or klawisz == 's' or klawisz == 'S':
            pozycja = ((pozycja[0]), (pozycja[1]+1)%wys)
            
        elif klawisz == 'KEY_UP' or klawisz == 'w' or klawisz == 'W':
            pozycja = ((pozycja[0]), (pozycja[1]-1)%wys)
            
        elif klawisz == 'KEY_RIGHT' or klawisz == 'd' or klawisz == 'D':
            pozycja = ((pozycja[0]+1)%szer, pozycja[1])
            
            
        # STAWIANIE FLAG
        elif klawisz == 'f' or klawisz == 'F':
            liczba_flag = postaw_flage(pozycja, plansza, liczba_flag)
            
        elif klawisz == 'e' or klawisz == 'E': # funkcja bedzie zwracac 0 - kontynuacja, 1 - wygrana, 2 - przegrana
            wynik, liczba_flag = ruch(pozycja, plansza, liczba_flag) 
            # jesli wygrana lub przegrana to przerwie petle gry

        # mozliwy automatyczny restart??    
        # elif klawisz == 'r' or klawisz == 'R':
        #     pass
        #     # koniec i poczatek nowej rozgrywki, restart
            
        curses.napms(50)    # dodalam opoznienie by nie wykorzystywac 100% procesora

    # poza petla, trzeba sprawdzic wartosc wynik. Jesli wynik = 1: wywolac wygrana(). Jesli wynik = 2: wywolac przegrana()
    if wynik == 1:
        pass
        # while True:
        #     coś się dzieje 
        #     zapisz wynik do konta
        #     wyswietl plansze
        #     try:    # zapobieganie blokowaniu sie gry
        #         klawisz = stdscr.getkey() # nasluchiwanie ruchow uzytkownika
        #     except:
        #         klawisz = None

        #     if klawisz == 'q' or klawisz == 'Q':
        #         break
            #skoncz gre / wyjdz do menu
     #wygrana
        
    if wynik == 2:
        pass
        # while True:
        #     coś się dzieje 
        #     wyswietl plansze 
        #     try:    # zapobieganie blokowaniu sie gry
        #         klawisz = stdscr.getkey() # nasluchiwanie ruchow uzytkownika
        #     except:
        #         klawisz = None

        #     if klawisz == 'q' or klawisz == 'Q':
        #         break
     #przegrana
        


# FUNKCJE TYMCZASOWE - tylko do testowania ;))
def okno_informacyjne(stdscr, tytul, wiadomosc): # proste okno, czeka na input
    h, w = stdscr.getmaxyx()
    okno = curses.newwin(5, 60, h//2 - 2, w//2 - 30)
    okno.box()
    
    okno.addstr(1, 2, tytul, curses.A_BOLD)
    okno.addstr(2, 2, wiadomosc)
    okno.addstr(3, 2, "Nacisnij dowolny klawisz aby wyjsc :3", curses.A_DIM)
    okno.refresh()
    
    stdscr.nodelay(False) 
    stdscr.getch()        
    stdscr.nodelay(True)



def logowanie_interfejs(stdscr):
    # Tu kiedys bedzie wpisywanie loginu i hasla ...

    okno_informacyjne(stdscr, "LOGOWANIE", "Udalo sie zalogowac!")
    return True


def tworzenie_konta_interfejs(stdscr):
    okno_informacyjne(stdscr, "TWORZENIE KONTA", "Konto utworzone!")
    return True


def usuwanie_konta_interfejs(stdscr):
    # Tu powinno byc pytanie "Czy na pewno?"
    okno_informacyjne(stdscr, "USUWANIE KONTA", "Konto zostalo usuniete")
    return True


def menu_glowne(stdscr):
    curses.curs_set(0)  # niech kursor sie nie wyswietla
    curses.start_color()  # dodaj kolory
    
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)

    stdscr.nodelay(True) # nie czeka na nacisniecie klawisza, dzieki czemu inne funkcje dzieja sie w tle

    #stdscr.timeout(50) -> mozliwe ze to by bylo lepsze zamiast nodelay + napms ???
    
    menu_gosc = ['Nowa Gra', 'Zasady Gry', 'Zaloguj', 'Utworz Konto', 'Wyjscie']
    menu_user = ['Nowa Gra', 'Wczytaj Gre', 'Ranking', 'Zasady Gry', 'Wyloguj', 'Usun Konto', 'Wyjscie']
    poziomy = ['Latwy  ★☆☆☆☆ ', 'Sredni ★★★☆☆ ', 'Trudny ★★★★★ ']
    
    czy_zalogowano = False
    iterator = 0
    obecny_rzad = 0

    while True:
        stdscr.erase()
        wysokosc, szerokosc = stdscr.getmaxyx() # pobiera informacje o wysokosci i szerokosci okna terminala
        
        if czy_zalogowano:
            aktualne_menu = menu_user
        else:
            aktualne_menu= menu_gosc

        ekran = [aktualne_menu, poziomy]
        tytuly = ["--- SAPER ---", "--- POZIOMY ---"]

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

        if klawisz == 'KEY_UP' or klawisz == 'w' or klawisz == 'W':
            obecny_rzad = (obecny_rzad - 1) % len(ekran[iterator])
            
        elif klawisz == 'KEY_DOWN' or klawisz == 's' or klawisz == 'S':
            obecny_rzad = (obecny_rzad + 1) % len(ekran[iterator])

        elif klawisz == 'q' or klawisz == 'Q': # cofnij - dokonczyc, gdy zrobimy zasady gry oraz logowanie
            if iterator == 1:
                stdscr.clear()
                iterator = 0
                obecny_rzad = 0
            
        elif klawisz == '\n':
            wybrana_opcja = ekran[iterator][obecny_rzad]
            
            if wybrana_opcja == 'Wyjscie':
                break
            
            elif wybrana_opcja == 'Nowa Gra':
                stdscr.clear()
                iterator = 1
                obecny_rzad = 0

            elif wybrana_opcja == 'Wczytaj Gre':
                #t1, t2, czas, liczba_flag = wczytaj(konto)
                #wys, szer = len(t1), len(t1[0])
                #plansza = Plansza(szer,wys,99) #nie ma przechowywanej liczby bomb, ale chyba niepotrzebna w kodzie
                #plansza.tablica = t1
                #plansza.wyswietlana = t2
                #rozgrywka(stdscr, plansza, liczba_flag) #,czas) #czy_zalogowano
                pass # wczytaj zapamietana gdzies plansze
            
            elif wybrana_opcja == 'Zasady Gry':
                okno_informacyjne(stdscr, "ZASADY", "Unikaj bomb...") 
                # Zrobic nowego windowa lub pada na zasady, ktore trzeba w README.md uzupelnic
            
            elif wybrana_opcja == 'Zaloguj':
                if logowanie_interfejs(stdscr): # okno na wpisywanie loginu, okno na wpisywanie hasla) + info czy sie udalo
                    czy_zalogowano = True
                    obecny_rzad = 0

            elif wybrana_opcja == 'Utworz Konto':
                if tworzenie_konta_interfejs(stdscr): # okno na wpisywanie loginu, okno na wpisywanie hasla) + info czy sie udalo
                    czy_zalogowano = True
                    obecny_rzad = 0

            elif wybrana_opcja == 'Wyloguj':
                czy_zalogowano = False
                okno_informacyjne(stdscr, "WYLOGOWANO", "Udalo sie wylogowac!")
                obecny_rzad = 0

            elif wybrana_opcja == 'Usun Konto':
                if usuwanie_konta_interfejs(stdscr): # interfejs (czy na pewno chcesz usnac konto? Tak/Nie + trzeba wyrzucic to konto z pliku ...)
                    czy_zalogowano = False
                    obecny_rzad = 0

            elif wybrana_opcja == 'Wczytaj Gre':
                okno_informacyjne(stdscr, "WCZYTYWANIE", "Funkcja w budowie...")
            
            elif wybrana_opcja == 'Ranking':
                okno_informacyjne(stdscr, "RANKING", "1. Agatka: 1 000 000 punktow :3")
            
            elif wybrana_opcja == poziomy[0]:
                szer, wys, bomby = 9,9,10
                liczba_flag = 10
                plansza = Plansza(szer,wys,bomby)
                generowanie(plansza)
                rozgrywka(stdscr, plansza, liczba_flag) # czy_zalogowano

            elif wybrana_opcja == poziomy[1]:
                szer, wys, bomby = 11,11,18
                liczba_flag = 20
                plansza = Plansza(szer,wys,bomby)
                generowanie(plansza)
                rozgrywka(stdscr, plansza, liczba_flag) # czas = 0, czy_zalogowano

            elif wybrana_opcja == poziomy[2]:
                szer, wys, bomby = 13,13,35
                liczba_flag = 40
                plansza = Plansza(szer,wys,bomby)
                generowanie(plansza)
                rozgrywka(stdscr, plansza, liczba_flag) # czas = 0, czy_zalogowano

wrapper(menu_glowne)