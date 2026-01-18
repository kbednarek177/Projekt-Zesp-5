# Saper
## Terminalowa gra wykonana w Pythonie

### Zasady gry:
Po planszy użytkownik porusza się klawiaturą:
* **\[F\]** - postawienie flagi
* **\[Q\]** - wróć do wyboru poziomu trudności
* **\[E\]** - odkrycie pola
* **\[Z\]** - zapisz grę (dostępne tylko po zalogowaniu)
* **\[A/W/S/D\] / strzalki** - poruszanie się po planszy

Pola są dwóch typów:
* pola z cyframi
* pola minowe

Odkrycie **pola minowego** oznacza **przegraną**.

**Cyfra na polu** informuje o tym, ile **min** styka się z nim bezpośrednio (bokami lub rogami).
*Przykład: Jeśli widzisz cyfrę 1, oznacza to, że na polach dookoła niej (maksymalnie 8 sąsiadów) ukryta jest tylko jedna mina.*

Celem gry jest odsłonięcie wszystkich pól na planszy które **nie zawierają min** oraz oznakowanie **flagami** pól minowych.

### Warianty gry:
Dostępne są trzy poziomy trudności:
- **ŁATWY:** 
	- rozmiar planszy: **9x9** 
	- ilość bomb:: **10**
- **ŚREDNI:** 
	- rozmiar planszy: **11x11** 
	- ilość bomb: **18**
- **TRUDNY:** 
	- rozmiar planszy: **13x13**
	- ilość bomb: **35**

### Jak uruchomić program:
W terminalu, po przejściu do właściwego folderu (Projekt-Zesp-5), należy wywołać komendę:
* **MacOC** - `python3 main.py` (nieprzetestowano)
* **Windows** - `python3 main.py`
* **Linux** - `python3 main.py`

### Obsługa programu:
Po programie użytkownik porusza się klawiaturą: 
* **\[Q\]** - wróć
* **\[ENTER\]** - zatwierdź
* **\[W/S\] / strzalki GÓRA i DÓŁ** - poruszanie się po **menu** i **poziomach trudności**

### Dodatkowe funkcje programu:
- **KONTA** - możliwe jest utworzenie konta, zalogowanie się na nie, wylogowanie, usunięcie konta oraz
(dostępne tylko po zalogowaniu) zapisywanie rozgrywki oraz rywalizowanie w rankingu z innymi użytkownikami
- **RANKING** 
	- użytkownicy rywalizują w trzech kategoriach (zależnych od poziomu trudności) - im w krótszym czasie się wygra, tym wyższą pozycję uzyskuje się w rankingu
	- widoczne są 2 najlepsze wyniki na dany poziom trudności
	- jeden użytkownik może zająć jedno miejsce w rankingu

### Dodatkowe biblioteki:
Do poprawnego działania programu należy pobrać:
* bibliotekę **curses** `pip install windows-curses` (powinna być wbudowana w Pythona na systemach Linux i MacOC)

### Informacje:
Repozytorium zostało utworzone na potrzeby projektu z **PWI 2025/2026**.
Autorami są: Karol Bednarek, Kinga Błaszkiewicz, Jakub Chytroń, Jurek Panenka, Agata Raczyk, Zuzanna Żol 

Więcej informacji znajduje się w pliku: **podsumowanie.tex**
