import math
import pygame
import sys
import random

pygame.init()
czcionka = pygame.font.SysFont("Arial", 24)
rozmiar_kafelka = 80
GAME_W = 5
GAME_H = 5

SZEROKOSC = (GAME_W + 1) * rozmiar_kafelka
WYSOKOSC = (GAME_H + 1) * rozmiar_kafelka + 100

ekran = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
pygame.display.set_caption("Saper")
zegar = pygame.time.Clock()

# --- ZMIENNE GRY ---
player_x = random.randint(0, GAME_W)
player_y = random.randint(0, GAME_H)

# Losujemy drzwi tak, aby nie nakładały się na gracza
while True:
    door_x = random.randint(0, GAME_W)
    door_y = random.randint(0, GAME_H)
    if (door_x, door_y) != (player_x, player_y):
        break

# Losujemy klucz tak, aby nie był na graczu ani na drzwiach
while True:
    key_x = random.randint(0, GAME_W)
    key_y = random.randint(0, GAME_H)
    if (key_x, key_y) != (player_x, player_y) and (key_x, key_y) != (door_x, door_y):
        break

player_found_key = False
gra_skonczona = False
bomby = []
zycia = 2
odliczanie = 10

# --- KOLORY ---
KOLOR_TLA = (30, 30, 30)
KOLOR_GRACZA = (0, 120, 255)
KOLOR_SIATKI = (50, 50, 50)
KOLOR_DRZWI = (0, 200, 100)
KOLOR_BOMB = (255, 50, 50)
KOLOR_ALERTU = (255, 100, 100)

uruchomiona = True

komunikat_cieplo_zimno = "Szukaj klucza, poruszaj się za pomocą WASD"
komunikat_kroki = f"Pozostałe życia: {zycia}"
distance_before = math.sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)

# --- GŁÓWNA PĘTLA GRY ---
while uruchomiona:
    zegar.tick(60)
    wykonano_ruch = False

    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            uruchomiona = False
        elif zdarzenie.type == pygame.KEYDOWN and not gra_skonczona:
            if zdarzenie.key == pygame.K_w:
                player_y -= 1
                if player_y < 0: player_y = 0
                wykonano_ruch = True
            elif zdarzenie.key == pygame.K_s:
                player_y += 1
                if player_y > GAME_H: player_y = GAME_H
                wykonano_ruch = True
            elif zdarzenie.key == pygame.K_a:
                player_x -= 1
                if player_x < 0: player_x = 0
                wykonano_ruch = True
            elif zdarzenie.key == pygame.K_d:
                player_x += 1
                if player_x > GAME_W: player_x = GAME_W
                wykonano_ruch = True

    # --- PEŁNA LOGIKA PO KROKU GRACZA ---
    if wykonano_ruch and not gra_skonczona:
        bomba_wybuchla = False
        wlasnie_zebrano_klucz = False

        # 1. Sprawdzenie bomb
        if (player_x, player_y) in bomby:
            zycia -= 1
            bomba_wybuchla = True
            bomby.remove((player_x, player_y))
            komunikat_cieplo_zimno = "💥 BUM! Wpadłeś na minę! Uważaj pod nogi!"

            if zycia <= 0:
                komunikat_cieplo_zimno = "💀 PRZEGRAŁEŚ! Brak żyć. Spróbuj ponownie!"
                gra_skonczona = True
            else:
                pygame.time.wait(200)

        # 2. Sprawdzenie wygranej (Dojście do wylosowanych drzwi)
        elif player_x == door_x and player_y == door_y and player_found_key:
            komunikat_cieplo_zimno = "🎉 WYGRAŁEŚ! Bezpieczna ewakuacja!"
            gra_skonczona = True

        # 3. Sprawdzenie czy zebrano klucz
        elif player_x == key_x and player_y == key_y and not player_found_key:
            player_found_key = True
            wlasnie_zebrano_klucz = True
            komunikat_cieplo_zimno = "🔑 Znalazłeś klucz! UCIEKAJ DO DRZWI!"

            for i in range(5):
                attempts = 0
                while attempts < 100:
                    bomba_x = random.randint(0, GAME_W)
                    bomba_y = random.randint(0, GAME_H)
                    # Bomby nie mogą też pojawić się na losowych drzwiach
                    if (bomba_x, bomba_y) != (player_x, player_y) and (bomba_x, bomba_y) != (door_x, door_y) and (
                    bomba_x, bomba_y) not in bomby:
                        bomby.append((bomba_x, bomba_y))
                        break
                    attempts += 1

            distance_before = math.sqrt((door_x - player_x) ** 2 + (door_y - player_y) ** 2)

        # 4. Odliczanie kroków ucieczki
        elif player_found_key:
            odliczanie -= 1
            if odliczanie <= 0:
                komunikat_cieplo_zimno = "💥 BAZA WYBUCHŁA! Nie zdążyłeś!"
                gra_skonczona = True

        # 5. Dynamiczne Ciepło-Zimno
        if not gra_skonczona and not bomba_wybuchla and not wlasnie_zebrano_klucz:
            if player_found_key:
                distance_after = math.sqrt((door_x - player_x) ** 2 + (door_y - player_y) ** 2)
            else:
                distance_after = math.sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)

            if distance_before > distance_after:
                komunikat_cieplo_zimno = "🔥 Ciepło, coraz cieplej..."
            else:
                komunikat_cieplo_zimno = "❄️ Zimno!"
            distance_before = distance_after

        # Aktualizacja dolnego tekstu o statusie
        if gra_skonczona:
            komunikat_kroki = "Koniec gry. Zamknij okno krzyżykiem."
        elif player_found_key:
            komunikat_kroki = f"Życia: {zycia} | ⚠️ Ewakuacja: {odliczanie} kroków!"
        else:
            komunikat_kroki = f"Życia: {zycia} | Szukaj klucza..."

    # --- RYSOWANIE EKRANU ---
    if uruchomiona:
        ekran.fill(KOLOR_TLA)

        # 1. Rysowanie siatki
        for x in range(0, SZEROKOSC, rozmiar_kafelka):
            pygame.draw.line(ekran, KOLOR_SIATKI, (x, 0), (x, WYSOKOSC - 100))
        for y in range(0, WYSOKOSC - 100, rozmiar_kafelka):
            pygame.draw.line(ekran, KOLOR_SIATKI, (0, y), (SZEROKOSC, y))

        # 2. Rysowanie drzwi ewakuacyjnych w losowych współrzędnych
        #drzwi_rect = pygame.Rect(door_x * rozmiar_kafelka, door_y * rozmiar_kafelka, rozmiar_kafelka, rozmiar_kafelka)
        #pygame.draw.rect(ekran, KOLOR_DRZWI, drzwi_rect)

        # 3. Rysowanie bomb (Zakomentowane)
        # for b_x, b_y in bomby:
        #     bomba_rect = pygame.Rect(b_x * rozmiar_kafelka, b_y * rozmiar_kafelka, rozmiar_kafelka, rozmiar_kafelka)
        #     pygame.draw.rect(ekran, KOLOR_BOMB, bomba_rect)

        # 4. Rysowanie gracza
        pozycja_piksele_x = player_x * rozmiar_kafelka
        pozycja_piksele_y = player_y * rozmiar_kafelka
        gracz_rect = pygame.Rect(pozycja_piksele_x, pozycja_piksele_y, rozmiar_kafelka, rozmiar_kafelka)
        pygame.draw.rect(ekran, KOLOR_GRACZA, gracz_rect)

        # 5. Rysowanie panelu informacyjnego
        if "BUM" in komunikat_cieplo_zimno or "PRZEGRAŁEŚ" in komunikat_cieplo_zimno:
            kolor_tekstu_1 = KOLOR_ALERTU
        else:
            kolor_tekstu_1 = (255, 255, 255)

        tekst_1 = czcionka.render(komunikat_cieplo_zimno, True, kolor_tekstu_1)
        tekst_2 = czcionka.render(komunikat_kroki, True, (200, 200, 200))

        ekran.blit(tekst_1, (20, (GAME_H + 1) * rozmiar_kafelka + 15))
        ekran.blit(tekst_2, (20, (GAME_H + 1) * rozmiar_kafelka + 55))

        pygame.display.flip()

pygame.quit()
sys.exit()