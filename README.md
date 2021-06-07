
# 3. Automat sprzedajacy napoje 

## Opis zadania


* Automat przechowuje informacje o monetach znajdujących sie w nim (1, 2, 5,
10, 20, 50gr, 1, 2, 5zt)
    
* Automat przechowuje informacje o towarach znajdujacych sie w nim (przedmioty o
numerach od 30 do 50), kazdy o określonej cenie w określonej liczbie (domyślinie
po 5 sztuk każdego towaru)
* Okno z przyciskami pozwalającymi na wrzucanie monet, polem wyświetlającym
kwotę wrzuconych monet, przyciskiem przerywającym transakcje (wyrzuca
wrzucone monety), przyciskami 0-9 pozwalającymi wpisać numer wybranego
towaru oraz polem wyswietlającym wpisany numer towaru.
* Po wybraniu poprawnego numeru towaru:
    * Jesli wrzucono za mało monet, wyskakuje okno z informacją o cenie towaru
oraz (jesli towar sie skonczył) o jego braku w automacie.
    * Jesli wrzucono monety, których wartosć jest większa lub równa cenie wybranego
towaru, automat sprawdza czy towarjest dostępny i czy może wydać resztę
        * Brak towaru: wyskakuje okienko z informacją o braku w automacie.
        * Brak reszty/może wydać: wyskakuje okienko z informacją o
zakupach, wydaje resztę (dolicza wrzucone monety, odlicza wydane
jako reszta, odlicza wydany towar), odejmuje towar.
        * Nie może wydać: wyskakuje okienko z napisem "Tylko odliczona kwota".

## Testy

1. Sprawdzenie ceny jednego towaru - oczekiwana informacja o cenie.
2. Wrzucenie odliczonej kwoty, zakup towaru - oczekiwany brak reszty.
3. Wrzucenie większej kwoty, zakup towaru - oczekiwana reszta.
4. Wykupienie całego asortymentu, próba zakupu po wyczerpaniu towaru oczekiwana informacja o braku.
5. Sprawdzenie ceny towaru o nieprawidłowym numerze (<30 lub >50) - oczekiwana informacja o błedzie.
6. Wrzucenie kilku monet, przerwanie transakcji - oczekiwany zwrot monet.
7. Wrzucenie za małej kwoty, wybranie poprawnego numeru towaru, wrzucenie
reszty monet do odliczonej kwoty, ponowne wybranie poprawnego numeru towaru - oczekiwany brak reszty.
8. Zakup towaru płacąc po 1 gr - suma stu monet ma być równa 12! (dla floatów
sumasto razy 0.01+0.01+...+0.01 nie będzie równa 1.0). Płatności mozna dokonać
za pomocą pętli for w interpreterze.


### Repozytorium [GitHub](https://github.com/wrobel2131/Automat-sprzedajacy-napoje).

