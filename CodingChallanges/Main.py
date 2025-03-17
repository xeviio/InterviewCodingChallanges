import pygame
import sys
from functions.hello_world import option_hello_world
from functions.factorial import option_factorial
from functions.reverse_string import option_reverse_string
from functions.max_number import option_max_number
from utils import draw_text, draw_back_button, handle_input, check_button_click


pygame.init()

# Ustawienia okna
WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu PyInterview")
font = pygame.font.Font(None, 36)

menu_options = [
    ("Hello, World!", lambda: option_hello_world(screen, font)),
    ("Oblicz silnię", lambda: option_factorial(screen, font)),
    ("Odwróć string", lambda: option_reverse_string(screen, font)),
    ("Znajdź największą cyfrę", lambda: option_max_number(screen, font)),  # Dodana opcja
    ("Wyjdź", sys.exit)
]

def draw_menu():
    """Rysuje menu główne."""
    screen.fill((30, 30, 30))  # Tło ekranu
    for i, (text, _) in enumerate(menu_options):
        draw_text(screen, text, font, 50 + i * 50)  # Równomierne rozmieszczenie opcji
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
                for i, (_, action) in enumerate(menu_options):
                    if 50 <= y <= 50 + i * 50 + 30:  # Wybór opcji
                        action()  # Uruchomienie funkcji powiązanej z opcją
                        break  # Po wykonaniu funkcji wracamy do menu

if __name__ == "__main__":
    main()  # Uruchomienie głównej pętli
