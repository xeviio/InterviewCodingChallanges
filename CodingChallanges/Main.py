import pygame
import sys
from functions import option_hello_world, option_factorial, option_reverse_string, exit_program

pygame.init()

WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu PyInterview")
font = pygame.font.Font(None, 36)

menu_options = [
    ("Hello, World!", lambda: option_hello_world(screen, font)),
    ("Oblicz silnię", lambda: option_factorial(screen, font)),
    ("Odwróć string", lambda: option_reverse_string(screen, font)),
    ("Wyjdź", exit_program)
]

def draw_menu():
    """Rysuje menu główne z równomiernie rozstawionymi napisami z 50px przerwą."""
    screen.fill((30, 30, 30))

    # Liczba opcji w menu
    num_options = len(menu_options)
    
    # Wysokość napisu i odstęp między nimi
    line_height = 50
    vertical_spacing = 50  # Odstęp 50px między napisami
    
    # Pozycjonowanie napisów
    for i, (text, _) in enumerate(menu_options):
        text_surface = font.render(text, True, (200, 200, 200))
        text_rect = text_surface.get_rect(center=(WIDTH // 2, vertical_spacing + i * (line_height + vertical_spacing)))
        screen.blit(text_surface, text_rect)

    pygame.display.flip()

def main():
    """Główna pętla menu."""
    while True:
        draw_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for i, (_, action) in enumerate(menu_options):
                    text_rect = pygame.Rect((WIDTH // 2) - 100,  # Pozycjonowanie w lewo
                                            50 + i * 100,  # Wysokość opcji
                                            200, 50)  # Wysokość i szerokość prostokąta, który odwzorowuje miejsce napisu
                    if text_rect.collidepoint(x, y):
                        action()  # Wywołanie funkcji przypisanej do opcji
                        break  # Po kliknięciu opcji, wracamy do menu

if __name__ == "__main__":
    main()
