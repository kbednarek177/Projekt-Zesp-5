from pathlib import Path ## chat gpt mi pomogl z odpowiednim dopasowaniem sciezki
import hashlib           ## tutaj również chat mi podpowiedział żeby haszować hasła za pomocą tej funkcji
directory = Path(__file__).resolve().parent   ##- chat gpt

dane = directory / "test.txt"                 ##- chat gpt


def wczytywanie_danych(dane):
    plik_praca = []                         ## wpisuję sobie tutaj zapisane dane żeby łatwiej było je przekazywać, zakładam, że w mainie będzie trzeba na samym początku wywolac ta funkcje
    for x in open(dane, encoding="utf-8"):
        plik_praca.append(x[:-1])           ## zapisując do pliku tekstowego ZAWSZE dodaję na koniec stringa \n (to jest traktowane jako jeden znak)-tu go usuwam do przetwarzania
    return plik_praca
    
    

##funkcje zwiazane z tworzeniem konta

def hasz(a: str) -> str:      ## jak wyzej, stwierdzilam ze zrobie to faktycznie haszowaniem
    return hashlib.sha256(a.encode("utf-8")).hexdigest()    ##- chat gpt

def czy_wolna(nazwa, plik): ## nazwy użytkownika nie mogą się powtarzać!
    for x in plik:
        if(x == nazwa):
            return False
    return True

def zaloz_konto(plik):    ## pierwsza poważna funkcjonalność - zakładanie konta. do pliku pracowniczego dodaję nowe dane na samym końcu. 
    nazwa = input()
    while(czy_wolna(nazwa,plik)==False):
        print("Nazwa zajęta!")
        nazwa = input()
        
    haslo_nieszyfr = input()
    haslo = hasz(haslo_nieszyfr)
    plik.append(nazwa)
    plik.append(haslo)
    
    return nazwa


def sprawdz_haslo(nazwa, plik):   ## sprawdzanie hasla - jako ze nazwy uzytkownikow nie powtarzaja sie + w pliku trzymam dane bez \n to sprawdzanie hasla jest latwe
    haslo = input()
    for i in range(len(plik)-1):
        if(plik[i] == nazwa):
            a = plik[i+1]
            haslo_hasz = hasz(haslo)
            if(haslo_hasz == a):
                return True
    return False
