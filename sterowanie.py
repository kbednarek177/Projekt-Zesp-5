from pynput.keyboard import Key, KeyCode, Listener


def sterowanie_saper(key, pozycja, wymiary, wygrana):
    #funkcja zwraca True/False, które mówi czy rozgrywka nadal trwa
    #oraz zmienioną pozycję
    if key == Key.esc:
        return False, pozycja
        #skończ grę/ wyjdź do menu

    if key == KeyCode.from_char('c'):
        Zapisz_Planszę()
        return True, pozycja
        #zapisuje planszę

    #poruszanie się awsd
    if key == KeyCode.from_char('a'):
        pozycja = ((pozycja[0]-1)%wymiary[0], pozycja[1])
        return True, pozycja
    
    if key == KeyCode.from_char('w'):
        pozycja = ((pozycja[0]), (pozycja[1]+1)%wymiary[1])
        return True, pozycja
    
    if key == KeyCode.from_char('s'):
        pozycja = ((pozycja[0]), (pozycja[1]-1)%wymiary[1])
        return True, pozycja
    
    if key == KeyCode.from_char('d'):
        pozycja = ((pozycja[0]+1)%wymiary[0], pozycja[1])
        return True, pozycja
    
    #interakcja e i q 
    if key == KeyCode.from_char('q'):
        Postaw_Flagę(pozycja)
        return True, pozycja
    
    if key == KeyCode.from_char('e'):
        wynik = Odkryj(pozycja)
        return wynik, pozycja
    

    









