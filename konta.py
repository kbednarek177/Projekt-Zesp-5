
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


def zaloz_konto(wczytane_dane, nazwa, haslo_nieszyfr):    ## zakładanie konta. do pliku dodaję nowe dane na samym końcu. 
    
    hasla = wczytane_dane[0]
    najlepszy_wynik = wczytane_dane[1]
    zapis_plansza1 = wczytane_dane[2]
    zapis_plansza2 = wczytane_dane[3]
    zapis_czas = wczytane_dane[4]
    
    haslo = hasz(haslo_nieszyfr)
    
    hasla[nazwa] = haslo
    najlepszy_wynik[nazwa] = "0"
    zapis_plansza1[nazwa] = "000"
    zapis_plansza2[nazwa] = "000"
    zapis_czas[nazwa] = 0

    return nazwa


def sprawdz_haslo(nazwa, haslo, nazwy_hasla):   ## sprawdzanie hasla 
    haslo_shaszowane = hasz(haslo)
    if(nazwy_hasla[nazwa] == haslo_shaszowane):
        return True
    return False



def zaloguj(nazwa, haslo, nazwy_hasla):
    if(sprawdz_haslo(nazwa, haslo, nazwy_hasla) == True):
        return nazwa
    return int(-1)
        


## funkcje zwiazane z najlepszymi wynikami (korzystajace z T[1])

def tablica_wynikow(nazwy_wynik):
    
    nazwy_wynik_int = dict()
    
    for x in nazwy_wynik:
        y = int(nazwy_wynik[x])
        nazwy_wynik_int[x] = y
    
    wartosci = []
    for x in nazwy_wynik_int:
        wartosci.append(nazwy_wynik_int[x])
    
    
    wartosci.sort()
    wartosci.reverse()
    
    s_wartosci = wartosci[:3]           
    wynik = dict()
    
    tasma = 3
    
    for i in s_wartosci:
        for x in nazwy_wynik_int:
            if(nazwy_wynik_int[x] == i):
                wynik[x] = i
                tasma = tasma - 1
            
    return wynik


def naj_wynik(wynik, nazwa, nazwy_wynik):
    if(nazwa not in nazwy_wynik):
        nazwy_wynik[nazwa] = wynik
    elif(wynik > int(nazwy_wynik[nazwa])):
        nazwy_wynik[nazwa] = wynik


##funkcje związane z zapisem 

def str_ll_przetlumacz(napis):
    
    rozmiar = napis[0]
    
    wynik = []
    temp = []
    
    for i in range(1,len(napis)):
        temp.append(int(napis[i]))
        if(i % int(rozmiar) == 0):
            wynik.append(temp)
            temp = []
            
    return wynik
    

def ll_str_przetlumacz(lista):
    ## bierze długość listy i daje na początek
    wynik = ""
    rozmiar = len(lista)
    wynik = wynik + str(rozmiar)
    
    ##na chama wczytuje elementy z list 
    
    for x in lista:
        for y in x:
            wynik = wynik + str(y)
    
    return wynik


        ## nazwa, og plansza, plansza z odkrytymi polami, pozostałe flagi, czas, zapisane_dane[2], zapisane_dane[3], zapisane_dane[4]
def zapisz(nazwa, numery, pola, poz_flagi, czas, nazwy_zapis_num, nazwy_zapis_pola, nazwy_zapis_czas):
    
    e_poz_flagi = str(poz_flagi)
    if(poz_flagi < 10):
        e_poz_flagi = '0' + e_poz_flagi
    
    nazwy_zapis_num[nazwa] = e_poz_flagi + ll_str_przetlumacz(numery)
    nazwy_zapis_pola[nazwa] = e_poz_flagi + ll_str_przetlumacz(pola)
    nazwy_zapis_czas[nazwa] = str(czas)
    
    
        ##  nazwa, zapisane_dane[2], zapisane_dane[3], zapisane_dane[4]
def wczytaj(nazwa, nazwy_zapis_num, nazwy_zapis_pola, nazwy_zapis_czas):
    poz_flagi = int(nazwy_zapis_num[nazwa][:2])
    numery = str_ll_przetlumacz(nazwy_zapis_num[nazwa][2:])
    pola = str_ll_przetlumacz(nazwy_zapis_pola[nazwa][2:])
    czas = int(nazwy_zapis_czas[nazwa])
    
    t = []
    t.append(numery)
    t.append(pola)
    t.append(poz_flagi)
    t.append(czas)
    
    return t


##funkcje zwiazane z nadpisywaniem pliku z danymi

def nadpisz_plik(tablica_dane, dane):
    dane_do_zapisu = []
    dane_do_zapisu.append(tablica_dane[0])
    dane_do_zapisu.append(tablica_dane[1])
    dane_do_zapisu.append(tablica_dane[2])
    dane_do_zapisu.append(tablica_dane[3])
    dane_do_zapisu.append(tablica_dane[4])
    
    zapis = json.dumps(dane_do_zapisu)
    with open(dane, mode="w", encoding="utf-8") as d:
        json.dump(zapis, d)


directory = Path(__file__).resolve().parent   ##- chat gpt

dane = directory / "zapisane_dane.json"       ##- chat gpt

if(dane.stat().st_size != 0):
    tablica_dane = wczytaj_dane(dane)
    
    
else:
    tablica_dane = [dict(), dict(), dict(), dict(), dict()]
    
if(len(tablica_dane) < 5):
    for i in range(5-len(tablica_dane)):
        tablica_dane.append(dict())
    


nadpisz_plik(tablica_dane, dane)
    



