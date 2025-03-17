import pygame
import sys
from utils import draw_text, draw_back_button, handle_input, check_button_click

def option_factorial(screen, font):
    """Wyświetla okno do obliczania silni z podanej liczby oraz przycisk powrotu."""
    input_active = True
    user_text = ""
    result_text= ""
    while input_active:
        screen.fill((30, 30, 30))  # Tło ekranu
        
        # Tworzenie napisu i prośby o wprowadzenie liczby
        draw_text(screen, "Podaj liczbę (max 20):", font, 100)
        
        # Wyświetlanie wpisanego tekstu
        draw_text(screen, user_text, font, 150)

        # Obsługa silni
        if user_text.isdigit():
            num = int(user_text)
            if num > 20:
                result_text = "Limit: max 20!"
            else:
                fact = 1
                for i in range(1, num + 1):
                    fact *= i
                result_text = f"{fact}"
        
        # Wyświetlanie wyniku
        draw_text(screen, result_text, font, 200,(144, 238, 144))

        # Wywołanie funkcji do rysowania przycisku "Wróć"
        button_rect = draw_back_button(screen, font)

        pygame.display.flip()  # Aktualizacja ekranu

        # Obsługa zdarzeń
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            user_text = handle_input(event, user_text)  # Obsługa wprowadzania tekstu
            if check_button_click(event, button_rect):  # Jeśli kliknięto w przycisk
                return  # Powrót do menu
