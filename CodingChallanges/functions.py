import pygame
import sys

def option_hello_world(screen, font):
    """Wyświetla okno z napisem Hello, World!"""
    button_rect = pygame.Rect(200, 320, 100, 40)
    
    while True:
        screen.fill((30, 30, 30))
        text_surface = font.render("Hello, World!", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(250, 150))
        screen.blit(text_surface, text_rect)

        pygame.draw.rect(screen, (50, 150, 250), button_rect)
        button_text = font.render("Wróć", True, (255, 255, 255))
        button_text_rect = button_text.get_rect(center=button_rect.center)
        screen.blit(button_text, button_text_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return  # Powrót do menu

def option_factorial(screen, font):
    """Obsługuje wprowadzanie liczby i oblicza jej silnię z limitem do 20."""
    input_active = True
    user_text = ""
    button_rect = pygame.Rect(200, 320, 100, 40)
    
    while input_active:
        screen.fill((30, 30, 30))
        prompt = font.render("Podaj liczbę (max 20):", True, (200, 200, 200))
        prompt_rect = prompt.get_rect(center=(250, 100))
        screen.blit(prompt, prompt_rect)

        # Wyświetlanie wpisanego tekstu
        text_surface = font.render(user_text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(250, 150))
        screen.blit(text_surface, text_rect)

        # Obliczanie silni
        if user_text.isdigit():
            num = int(user_text)
            if num > 20:
                result_text = "Limit: max 20!"
            else:
                fact = 1
                for i in range(1, num + 1):
                    fact *= i
                result_text = f"Silnia: {fact}"
        else:
            result_text = "Podaj liczbę całkowitą!"

        # Wyświetlanie wyniku
        result_surface = font.render(result_text, True, (100, 255, 100))
        result_rect = result_surface.get_rect(center=(250, 200))
        screen.blit(result_surface, result_rect)

        # Przycisk "Wróć"
        pygame.draw.rect(screen, (50, 150, 250), button_rect)
        button_text = font.render("Wróć", True, (255, 255, 255))
        button_text_rect = button_text.get_rect(center=button_rect.center)
        screen.blit(button_text, button_text_rect)

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
                    if len(user_text) < 2:  # Ograniczenie długości do 2 cyfr (max 20)
                        user_text += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return  # Powrót do menu
                
def option_reverse_string(screen, font):
    """Odwraca wprowadzony tekst w czasie rzeczywistym."""
    user_text = ""
    button_rect = pygame.Rect(200, 320, 100, 40)

    while True:
        screen.fill((30, 30, 30))
        prompt = font.render("Wpisz tekst:", True, (200, 200, 200))
        prompt_rect = prompt.get_rect(center=(250, 100))
        screen.blit(prompt, prompt_rect)

        # Wyświetlanie wpisanego tekstu
        text_surface = font.render(user_text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(250, 150))
        screen.blit(text_surface, text_rect)

        # Odwrócony tekst
        reversed_text = user_text[::-1]
        result_surface = font.render(reversed_text, True, (100, 255, 100))
        result_rect = result_surface.get_rect(center=(250, 200))
        screen.blit(result_surface, result_rect)

        # Przycisk "Wróć"
        pygame.draw.rect(screen, (50, 150, 250), button_rect)
        button_text = font.render("Wróć", True, (255, 255, 255))
        button_text_rect = button_text.get_rect(center=button_rect.center)
        screen.blit(button_text, button_text_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return  # Powrót do menu

def exit_program():
    """Zamyka program."""
    pygame.quit()
    sys.exit()
