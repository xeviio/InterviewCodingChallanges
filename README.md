# PyInterview Coding Challenges

PyInterview to aplikacja stworzona w Pythonie, której celem jest przygotowanie do rozmów kwalifikacyjnych poprzez implementację różnych algorytmów i zadań programistycznych. Program pozwala na interaktywne wypróbowanie takich funkcji jak obliczanie silni, odwracanie tekstu, obliczanie największej liczby z zestawu i inne. Wszystko to w graficznym interfejsie użytkownika stworzonym z użyciem biblioteki Pygame.

## Funkcjonalności
- **Hello World** – Program wyświetla komunikat "Hello, World!".
- **Silnia** – Umożliwia obliczenie silni z liczby (max 20).
- **Odwracanie tekstu** – Odwraca wprowadzony tekst w czasie rzeczywistym.
- **Największa liczba** – Wprowadź 5 liczb i otrzymaj największą z nich.
- **Quick sort** – Algorytm sortujący sposobem Quick sort losowo wygenerowanego ciągu liczb.
- **Powrót do menu** – Możliwość powrotu do głównego menu aplikacji.


## Wymagania
- Python 3.x
- Biblioteka Pygame

Aby uruchomić aplikację, musisz mieć zainstalowanego Pythona 3 oraz bibliotekę Pygame. Możesz zainstalować ją przy pomocy poniższego polecenia:

```bash
pip install pygame
```
## Struktura Projektu
```bash
pyinterview-coding-challenges/
│
├── main.py              # Główny plik uruchamiający aplikację
├── utils.py         # Funkcje pomocnicze do obsługi przycisków i rysowania
│
├── functions/           # Folder zawierający wszystkie funkcje aplikacji
│   ├── hello_world.py   # Funkcja wyświetlająca "Hello World"
│   ├── factorial.py     # Funkcja obliczająca silnię
│   ├── reverse_string.py # Funkcja odwracająca tekst
│   ├── max_number.py    # Funkcja znajdująca największą liczbę z 5
│   └── exit_program.py  # Funkcja kończąca działanie programu
│
└── README.md            # Dokumentacja projektu
```
