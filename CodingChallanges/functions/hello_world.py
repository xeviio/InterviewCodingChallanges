import pygame
import sys
from utils import draw_text, draw_back_button, check_button_click

def option_hello_world(screen, font):
    """Wyświetla okno z napisem 'Hello, World!' oraz przyciskiem powrotu."""
    while True:
        screen.fill((30, 30, 30))  # Tło ekranu
        
        # Tworzenie napisu "Hello, World!" na środku ekranu
        draw_text(screen, "Hello, World!", font, 150)

        # Wywołanie funkcji do rysowania przycisku "Wróć"
        button_rect = draw_back_button(screen, font)

        pygame.display.flip()  # Aktualizacja ekranu

        # Obsługa zdarzeń
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif check_button_click(event, button_rect):  # Jeśli kliknięto w przycisk
                return  # Powrót do menu
