from pathlib import Path ## chat gpt mi pomogl z odpowiednim dopasowaniem sciezki
import hashlib           ## tutaj również chat mi podpowiedział żeby haszować hasła za pomocą tej funkcji
directory = Path(__file__).resolve().parent   ##- chat gpt

dane = directory / "test.txt"                 ##- chat gpt


def wczytywanie_danych(dane, nazwy, hasla_hasz):
            
    for x in open(dane, encoding="utf-8"):
        y = x.split()
        if y[0] == "NAZWA:":
            nazwy.append(y[1])
        elif y[0] == "HASLO:":
            hasla_hasz.append(y[1])
    

##funkcje zwiazane z tworzeniem konta

def hasz(a: str) -> str:                                    ## jak wyzej, stwierdzilam ze zrobie to faktycznie haszowaniem
    return hashlib.sha256(a.encode("utf-8")).hexdigest()    ##- chat gpt

def czy_wolna(nazwa, nazwy): ## nazwy użytkownika nie mogą się powtarzać!
    for x in nazwy:
        if(x == nazwa):
            return False
    return True


def zaloz_konto(nazwy, hasla_hasz):    ## pierwsza poważna funkcjonalność - zakładanie konta. do pliku pracowniczego dodaję nowe dane na samym końcu. 
    nazwa = input()
    
    while(czy_wolna(nazwa,nazwy)==False):
        print("Nazwa zajęta!")
        nazwa = input()

    haslo_nieszyfr = input()
    haslo = hasz(haslo_nieszyfr)
    
    nazwy.append(nazwa)
    hasla_hasz.append(haslo)

    return nazwa
