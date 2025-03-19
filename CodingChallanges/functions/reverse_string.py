import pygame
import sys
from utils import draw_text, draw_back_button, handle_input, check_button_click

WIDTH=800

def option_reverse_string(screen, font):
    """Wyświetla okno do wprowadzania tekstu i odwracania go."""
    user_text = ""  # Inicjalizacja zmiennej na tekst
    while True:
        screen.fill((30, 30, 30))  # Tło ekranu

        # Wyświetlanie napisu i prośby o wprowadzenie tekstu
        draw_text(screen, "Wpisz tekst do odwrócenia:", font,WIDTH, 100)

        # Wyświetlanie wprowadzonego tekstu
        draw_text(screen, user_text, font,WIDTH, 150)

        # Odwrócenie tekstu
        reversed_text = user_text[::-1]
        draw_text(screen, f"{reversed_text}", font,WIDTH, 200,(144, 238, 144))

        # Rysowanie przycisku "Wróć"
        button_rect = draw_back_button(screen, font, WIDTH)

        pygame.display.flip()  # Aktualizacja ekranu

        # Obsługa zdarzeń
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Obsługuje wprowadzanie tekstu, pozwala na wszystkie znaki
            user_text = handle_input(event, user_text)

            # Sprawdzenie, czy kliknięto przycisk powrotu
            if check_button_click(event, button_rect):
                return  # Powrót do menu
