from pynput.keyboard import Key, KeyCode, Listener
from saper import postaw_flage, ruch


def sterowanie_saper(key, plansza, pozycja, wygrana):
    #funkcja zwraca True/False, które mówi czy rozgrywka nadal trwa
    #oraz zmienioną pozycję
    #Aktualny problem: jak przekazać informację czy wygrana/przegrana. Mozliwe rozwiązanie: przypisanie wartości(1,2,3, ...) do wygrana, przegrana, wyjście, reset, kontynuacja, która będzie zwracana zamiast True/False.
    if key == Key.esc:
        #zapisz planszę??
        return False, pozycja
        #skończ grę/ wyjdź do menu

    if key == KeyCode.from_char('c'):
        Zapisz_Plansze(plansza)
        return True, pozycja
        #zapisuje planszę

    #poruszanie się awsd
    if key == KeyCode.from_char('a'):
        pozycja = ((pozycja[0]-1)%plansza.szer, pozycja[1])
        return True, pozycja
    
    if key == KeyCode.from_char('w'):
        pozycja = ((pozycja[0]), (pozycja[1]+1)%plansza.wys)
        return True, pozycja
    
    if key == KeyCode.from_char('s'):
        pozycja = ((pozycja[0]), (pozycja[1]-1)%plansza.wys)
        return True, pozycja
    
    if key == KeyCode.from_char('d'):
        pozycja = ((pozycja[0]+1)%plansza.szer, pozycja[1])
        return True, pozycja
    
    #interakcja e i q 
    if key == KeyCode.from_char('q'):
        postaw_flage(pozycja, plansza)
        return True, pozycja
    
    if key == KeyCode.from_char('e'):
        wynik = ruch(pozycja, plansza)
        return wynik, pozycja
    
    if key == KeyCode.from_char('r'):
        pass
        #koniec i początek nowej rozgrywki, restart
    

    









