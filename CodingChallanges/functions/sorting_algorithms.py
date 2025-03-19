import pygame
import random
from utils import draw_back_button, check_button_click

WIDTH = 800
HEIGHT = 600  # Dodanie wysokości okna

def generate_random_array():
    return random.sample(range(1, 101), 100)  # Losowe wartości od 1 do 100, każda unikalna

def quicksort(arr, screen, array, bar_width, max_height, left=0, right=None):
    """ Funkcja QuickSort z wizualizacją kroków """
    if right is None:
        right = len(arr) - 1
    
    if left < right:
        # Partycja
        pivot_index = partition(arr, left, right, array, screen, bar_width, max_height)
        
        # Animacja przed i po podziale
        draw_array(screen, array, bar_width, max_height, left, right)
        pygame.display.update()
        pygame.time.delay(100)  # Opóźnienie dla animacji

        # Rekurencyjne wywołanie dla lewej i prawej części
        quicksort(arr, screen, array, bar_width, max_height, left, pivot_index - 1)
        quicksort(arr, screen, array, bar_width, max_height, pivot_index + 1, right)

def partition(arr, left, right, array, screen, bar_width, max_height):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            # Po zamianie wywołujemy animację zaktualizowanego stanu tablicy
            draw_array(screen, array, bar_width, max_height, i, j)  # Zaznaczamy zamienione elementy
            pygame.display.update()
            pygame.time.delay(5)  # Opóźnienie dla animacji
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    draw_array(screen, array, bar_width, max_height, i + 1, right)  # Pokazanie zamiany pivota
    pygame.display.update()
    pygame.time.delay(5)  # Opóźnienie dla animacji
    return i + 1  # Zwracamy indeks pivota

def draw_array(screen, array, bar_width, max_height, highlight_left=-1, highlight_right=-1):
    """ Funkcja do rysowania słupków na ekranie na podstawie tablicy array """
    start_x = (WIDTH - (len(array) * bar_width)) // 2  # Wyśrodkowanie słupków
    start_y = HEIGHT // 3 + 20  # Przesunięcie słupków na środek ekranu w pionie
    
    for i, value in enumerate(array):
        bar_height = (value / 100) * max_height
        
        # Tworzymy tło dla każdej kolumny, aby zakryć stare wartości
        # Tło rozciąga się od końca poprzedniej kolumny do maksymalnej wysokości
        pygame.draw.rect(screen, (30, 30, 30), (start_x + i * bar_width, start_y - max_height, bar_width, max_height))  # Tło dla kolumny
        
        # Wybieramy kolor dla elementów: zaznaczone porównywane, lub zamieniane
        if i == highlight_left or i == highlight_right:
            color = (255, 0, 0)  # Kolor czerwony dla porównywanych lub zamienianych
        else:
            color = (0, 255, 0)  # Domyślny kolor zielony
        
        # Rysujemy słupek (kolumnę) z odpowiednią wysokością
        pygame.draw.rect(screen, color, (start_x + i * bar_width, start_y - bar_height, bar_width, bar_height))

def option_sorting_algorithms(screen, font):
    """ Funkcja generująca losową tablicę i wizualizującą ją na ekranie """
    array = generate_random_array()
    bar_width = 6
    max_height = 200  # Dostosowanie wysokości słupków
    clock = pygame.time.Clock()
    running = True
    
    # Przyciski poza pętlą animacji
    reset_button_rect = pygame.Rect(150, 250, 200, 50)
    quicksort_button_rect = pygame.Rect(400, 250, 200, 50)  # Nowy przycisk QuickSort
    back_button_rect = draw_back_button(screen, font, WIDTH)  # Rysowanie przycisku powrotu

    while running:
        screen.fill((30, 30, 30))  # Czyszczenie ekranu

        # Rysowanie przycisków na ekranie
        pygame.draw.rect(screen, (100, 200, 100), reset_button_rect)
        reset_text = font.render("Reset Array", True, (0, 0, 0))
        screen.blit(reset_text, (reset_button_rect.x + 30, reset_button_rect.y + 10))
        
        pygame.draw.rect(screen, (200, 100, 100), quicksort_button_rect)
        quicksort_text = font.render("QuickSort", True, (0, 0, 0))
        screen.blit(quicksort_text, (quicksort_button_rect.x + 50, quicksort_button_rect.y + 10))

        # Rysowanie przycisku powrotu
        back_button_rect = draw_back_button(screen, font, WIDTH)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if check_button_click(event, reset_button_rect):
                    array = generate_random_array()
                elif check_button_click(event, quicksort_button_rect):
                    # Wywołanie algorytmu QuickSort z wizualizacją kroków
                    quicksort(array, screen, array, bar_width, max_height)
                elif check_button_click(event, back_button_rect):
                    return  # Powrót do poprzedniego ekranu

        # Rysowanie tablicy z wartościami
        draw_array(screen, array, bar_width, max_height)  # Rysowanie aktualnej tablicy
        
        pygame.display.flip()  # Aktualizacja ekranu
        clock.tick(30)  # Ograniczenie liczby klatek na sekundę
