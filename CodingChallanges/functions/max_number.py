import pygame
import sys
from utils import draw_text, draw_back_button, handle_input

WIDTH=800

def option_max_number(screen, font):
    """Pozwala użytkownikowi wpisać 5 cyfr i zwraca największą z nich."""
    input_active = True
    user_text = ""
    button_rect = pygame.Rect(200, 320, 100, 40)

    while input_active:
        screen.fill((30, 30, 30))
        draw_text(screen, "Wpisz 5 cyfr:", font,WIDTH, 100)

        # Wyświetlanie wpisanego tekstu
        draw_text(screen, user_text, font,WIDTH, 150)

        # Obliczanie największej liczby
        if len(user_text) == 5 and user_text.isdigit():
            numbers = [int(c) for c in user_text]
            max_number = max(numbers)
            result_text = f"Największa cyfra: {max_number}"
        else:
            result_text = "Podaj dokładnie 5 cyfr!"

        # Wyświetlanie wyniku
        draw_text(screen, result_text, font,WIDTH, 200, (0, 255, 0))

        # Przycisk "Wróć"
        button_rect = draw_back_button(screen, font, WIDTH)

        pygame.display.flip()

        # Obsługa zdarzeń
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key in range(pygame.K_0, pygame.K_9 + 1):  # Wpisywanie tylko cyfr
                    if len(user_text) < 5:  # Ograniczenie do 5 cyfr
                        user_text += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return  # Powrót do menu
