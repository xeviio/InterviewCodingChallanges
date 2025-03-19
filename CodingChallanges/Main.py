import pygame
import sys
from functions.hello_world import option_hello_world
from functions.factorial import option_factorial
from functions.reverse_string import option_reverse_string
from functions.max_number import option_max_number
from functions.sorting_algorithms import option_sorting_algorithms
from utils import draw_text

pygame.init()

# Ustawienia okna
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu PyInterview")
font = pygame.font.Font(None, 36)

menu_options = [
    ("Hello, World!", lambda: option_hello_world(screen, font)),
    ("Oblicz silnię", lambda: option_factorial(screen, font)),
    ("Odwróć string", lambda: option_reverse_string(screen, font)),
    ("Znajdź największą cyfrę", lambda: option_max_number(screen, font)),
    ("Algorytmy sortujące", lambda: option_sorting_algorithms(screen, font)),
    ("Wyjdź", sys.exit)
]

def draw_menu():
    """Rysuje menu główne."""
    screen.fill((30, 30, 30))  # Tło ekranu

    # Obliczanie wysokości dla opcji menu na podstawie proporcji ekranu
    option_height = HEIGHT // (len(menu_options) + 1)  # Dzielimy wysokość na liczbę opcji
    
    for i, (text, _) in enumerate(menu_options):
        # Wysokość opcji menu to proporcja wysokości okna
        y_position = (i + 1) * option_height
        draw_text(screen, text, font, WIDTH, y_position)  # Równomierne rozmieszczenie opcji

    pygame.display.flip()

def main():
    """Główna pętla menu."""
    while True:
        draw_menu()  # Rysowanie menu głównego
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                option_height = HEIGHT // (len(menu_options) + 1)  # Obliczamy wysokość dla opcji

                # Sprawdzanie kliknięcia na odpowiednią opcję
                for i, (_, action) in enumerate(menu_options):
                    if (i + 1) * option_height - 30 <= y <= (i + 1) * option_height + 30:
                        action()  # Uruchomienie funkcji powiązanej z opcją
                        break  # Po wykonaniu funkcji wracamy do menu

if __name__ == "__main__":
    main()  # Uruchomienie głównej pętli
 
