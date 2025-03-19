import pygame


# Funkcja rysująca tekst na ekranie
def draw_text(screen, text, font, WIDTH, y_position, color=(255, 255, 255)):
    """
    Funkcja rysująca tekst na ekranie w zadanej pozycji.
    
    Parameters:
    - screen: ekran gry (pygame.Surface)
    - text: tekst do wyświetlenia (str)
    - font: czcionka (pygame.font.Font)
    - WIDTH: szerokość ekranu do obliczenia pozycji X
    - y_position: pozycja Y dla tekstu
    - color: kolor tekstu w formacie RGB (domyślnie biały)
    """
    x_position = WIDTH // 2  # Środek ekranu
    text_surface = font.render(text, True, color)  # Renderowanie tekstu
    text_rect = text_surface.get_rect(center=(x_position, y_position))  # Ustawienie pozycji
    screen.blit(text_surface, text_rect)  # Rysowanie tekstu na ekranie

# Funkcja rysująca przycisk 'Wróć' oraz zwracająca jego prostokąt
def draw_back_button(screen, font, WIDTH):
    """Rysuje przycisk 'Wróć' na ekranie i zwraca jego prostokąt."""
    button_x = WIDTH // 2 - 50  # Centrowanie przycisku
    button_rect = pygame.Rect(button_x, 320, 100, 40)  # Współrzędne przycisku
    pygame.draw.rect(screen, (50, 150, 250), button_rect)  # Rysowanie niebieskiego prostokąta
    
    button_text = font.render("Wróć", True, (255, 255, 255))  # Tekst przycisku
    button_text_rect = button_text.get_rect(center=button_rect.center)  # Tekst na środku przycisku
    screen.blit(button_text, button_text_rect)  # Rysowanie tekstu na przycisku
    
    return button_rect  # Zwracamy prostokąt przycisku

# Funkcja obsługująca klawiaturę
def handle_input(event, user_text):
    """Obsługuje wprowadzanie tekstu przez użytkownika."""
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_BACKSPACE:  # Usuwanie ostatniego znaku
            user_text = user_text[:-1]
        elif event.key != pygame.K_RETURN:  # Ignorowanie Enter
            user_text += event.unicode  # Dodawanie wprowadzonego znaku
    return user_text

# Funkcja do obsługi kliknięć w przyciski
def check_button_click(event, button_rect):
    """Sprawdza, czy kliknięto w przycisk."""
    if event.type == pygame.MOUSEBUTTONDOWN:
        if button_rect.collidepoint(event.pos):  # Sprawdza, czy kliknięto w prostokąt
            return True
    return False
