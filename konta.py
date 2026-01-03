
## Plik z danymi składa się z listy L słowników (w każdym kluczami są nazwy użyt.), gdzie L[0] - hasła, L[1] - najlepsze wyniki itd.

from pathlib import Path ## chat gpt mi pomogl z odpowiednim dopasowaniem sciezki
import hashlib           ## tutaj również chat mi podpowiedział żeby haszować hasła za pomocą tej funkcji
import json 





def wczytaj_dane(dane):
    with open(dane,  mode="r", encoding="utf-8") as dane:
        d = json.load(dane)
        d1 = json.loads(d)
    return d1
        

##funkcje zwiazane z tworzeniem konta i logowaniem (uzywa L[0])

def hasz(a: str) -> str:                                    ## patrz import hashlib
    return hashlib.sha256(a.encode("utf-8")).hexdigest()    ##- chat gpt

def czy_wolna(nazwa, nazwy_hasla): ## nazwy użytkownika nie mogą się powtarzać
    for x in nazwy_hasla.keys():
        if(x == nazwa):
            return False
    return True


def zaloz_konto(nazwy_hasla):    ## zakładanie konta. do pliku dodaję nowe dane na samym końcu. 
    nazwa = input()
    
    while(czy_wolna(nazwa,nazwy_hasla)==False):
        print("Nazwa zajęta!")
        nazwa = input()

    haslo_nieszyfr = input()
    haslo = hasz(haslo_nieszyfr)
    
    nazwy_hasla[nazwa] = haslo

    return nazwa


def sprawdz_haslo(nazwa, haslo, nazwy_hasla):   ## sprawdzanie hasla 
    haslo_shaszowane = hasz(haslo)
    if(nazwy_hasla[nazwa] == haslo_shaszowane):
        return True
    return False


def zaloguj(nazwa, haslo, nazwy_hasla):
    if(sprawdz_haslo(nazwa, haslo, nazwy_hasla) == True):
        return True
    return False
        

##funkcje zwiazane z nadpisywaniem pliku z danymi

def nadpisz_plik(nazwy_hasla, nazwy_wynik, dane):
    dane_do_zapisu = []
    dane_do_zapisu.append(nazwy_hasla)
    dane_do_zapisu.append(nazwy_wynik)
    zapis = json.dumps(dane_do_zapisu)
    with open(dane, mode="w", encoding="utf-8") as d:
        json.dump(zapis, d)


directory = Path(__file__).resolve().parent   ##- chat gpt

dane = directory / "zapisane_dane.json"       ##- chat gpt
