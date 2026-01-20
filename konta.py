
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
    najlepszy_wynik[nazwa] = "l-1s-1t-1"
    zapis_plansza1[nazwa] = "000"
    zapis_plansza2[nazwa] = "000"
    zapis_czas[nazwa] = 0

    return nazwa


def sprawdz_haslo(nazwa, haslo, nazwy_hasla):   ## sprawdzanie hasla 
    haslo_shaszowane = hasz(haslo)
    if(nazwa not in nazwy_hasla):
        return False
    if(nazwy_hasla[nazwa] == haslo_shaszowane):
        return True
    return False



def zaloguj(nazwa, haslo, nazwy_hasla):
    if(sprawdz_haslo(nazwa, haslo, nazwy_hasla) == True):
        return nazwa
    return int(-1)
        

def usun_konto(nazwa, tablica_dane):
    for i in tablica_dane:
        del i[nazwa]

## funkcje zwiazane z najlepszymi wynikami (korzystajace z T[1])

def znajdz_naj(w, nazwy):
    
    indeks = dict()
    
    for i in range(len(w)):
        if(w[i] > 0):
            indeks[nazwy[i]] = w[i]
    
    wartosci = []
    for w1 in w:
        if(w1 > 0):
            wartosci.append(w1)
            
    wartosci.sort()
    wynik = []
    
    if(len(wartosci) > 1):
        s_wartosci = wartosci[:2]
    
        tasma = 2
    
        for i in s_wartosci:
            for x in indeks:
                if(indeks[x] == i):
                    if(tasma == 0):
                        break
                    wynik.append(str(i) + "-" + x)
                    tasma = tasma - 1
                    
    if(len(wartosci) == 1):
        s_wartosci = wartosci[0]
        
        tasma = 2
    
        for x in indeks:
            if(indeks[x] == s_wartosci):
                if(tasma > 0):
                    wynik.append(str(s_wartosci) + "-" + x)
                    tasma = tasma - 1
                    
        if(len(wynik) < 2):
            wynik.append("-")
            
    if(len(wartosci) == 0):
        wynik.append("-")
        wynik.append("-")
    
    return wynik



def tablica_wynikow(nazwy_wynik):
    
    latwy = []
    sredni = []
    trudny = []
    nazwy = []
    wynik = []
    for x in nazwy_wynik:
        lista = wyniki(x, nazwy_wynik)
        latwy.append(int(lista[0]))
        sredni.append(int(lista[1]))
        trudny.append(int(lista[2]))
        nazwy.append(x)
    
    a = znajdz_naj(latwy, nazwy)
    
    for i in range(2):
        wynik.append(a[i])
    
    a = znajdz_naj(sredni, nazwy)
    
    for i in range(2):
        wynik.append(a[i])
        
    a = znajdz_naj(trudny, nazwy)
    
    for i in range(2):
        wynik.append(a[i])
        
    return wynik

def nadpisz_wynik(nazwa, indeks, nazwy_wynik):
    napis = ""
    for x in indeks:
        napis = napis + x
        napis = napis + indeks[x]
    
    nazwy_wynik[nazwa] = napis


def naj_wynik(wynik, poziom, nazwa, nazwy_wynik):    ##    l000000s000000t000000
    
    tab = wyniki(nazwa, nazwy_wynik)
    
    indeks = {"l": tab[0], "s": tab[1], "t": tab[2]}
    
    if(int(indeks[poziom]) < 0):
        indeks[poziom] = str(wynik)
        nadpisz_wynik(nazwa, indeks, nazwy_wynik)
    
    elif(int(indeks[poziom]) > wynik):
        indeks[poziom] = str(wynik)
        nadpisz_wynik(nazwa, indeks, nazwy_wynik)
        
        
def wyniki(nazwa, nazwy_wynik):
    wyniki = nazwy_wynik[nazwa]
    i = 1
    latwy = ""
    sredni = ""
    trudny = ""

    
    while(wyniki[i] != 's'):
        latwy = latwy + wyniki[i]
        i = i + 1
        
    i = i + 1
    
    
    while(wyniki[i] != 't'):
        sredni = sredni + wyniki[i]
        i = i + 1
        
    i = i + 1
    
    while(i < len(wyniki)):
        trudny = trudny + wyniki[i]
        i = i + 1
        
    return [latwy, sredni, trudny]

##funkcje związane z zapisem 

def str_ll_przetlumacz(napis):
    
    dl_rozmiar = int(napis[0])
    
    rozmiar = napis[1:dl_rozmiar+1]
    wynik = []
    temp = []
    
    wynik = []
    temp = []
    i = dl_rozmiar+1
    while (i < len(napis)):
        if(napis[i] != '-' and napis[i] != 'f'):
            temp.append(int(napis[i]))
        elif(napis[i] == '-'):
            temp.append(-int(napis[i+1]))
            i = i + 1
        elif(napis[i] == 'f'):
            temp.append(10)
        if(len(temp) == int(rozmiar)):
            wynik.append(temp)
            temp = []
        i = i + 1
    return wynik
    

def ll_str_przetlumacz(lista):
    ## bierze długość listy i daje na początek
    wynik = ""
    rozmiar = len(lista)
    
    if(rozmiar <10):
        wynik =  wynik + '1'
    else:
        wynik = wynik + '2'
    wynik = wynik + str(rozmiar)
    
    ##wczytuje elementy z list 
    
    for x in lista:
        for y in x:
            wynik = wynik + str(y)
    
    return wynik

def usun_zapis(nazwa, tablica):
    tablica[2][nazwa] = "000"
    tablica[3][nazwa] = "000"
    tablica[4][nazwa] = 0

def usun_dz(lista):
    lista1 = []
    temp = []
    for x in lista:
        for y in x:
            if(y == 10):
                temp.append('f')
            else:
                temp.append(y)
        lista1.append(temp)
        temp = []
                
    return lista1


        ## nazwa, og plansza, plansza z odkrytymi polami, pozostałe flagi, czas, zapisane_dane[2], zapisane_dane[3], zapisane_dane[4]
def zapisz(nazwa, numery, pola, poz_flagi, czas, nazwy_zapis_num, nazwy_zapis_pola, nazwy_zapis_czas):
    
    e_poz_flagi = str(poz_flagi)
    if(poz_flagi < 10):
        e_poz_flagi = '0' + e_poz_flagi
    
    nazwy_zapis_num[nazwa] = e_poz_flagi + ll_str_przetlumacz(numery)
    nazwy_zapis_pola[nazwa] = e_poz_flagi + ll_str_przetlumacz(usun_dz(pola))
    nazwy_zapis_czas[nazwa] = str(czas)
    
    
        ##  nazwa, zapisane_dane[2], zapisane_dane[3], zapisane_dane[4]
def wczytaj(nazwa, nazwy_zapis_num, nazwy_zapis_pola, nazwy_zapis_czas):
    if(len(nazwy_zapis_num) == 3):
        t = [0]
        
        return t
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
    



    



