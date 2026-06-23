# 🕵️‍♂️ Saper – Projekt Gry w Dwóch Wersjach (Terminal & Pygame)

Gra logiczno-zręcznościowa typu "Ciepło-Zimno" z elementami kultowego Sapera, napisana w języku Python. Gra oferuje dwa niezależne tryby rozgrywki: klasyczny tekstowy w terminalu oraz w pełni graficzny z użyciem biblioteki **Pygame**.

## 🎮 O co chodzi w grze?
Twoim zadaniem jest odnalezienie ukrytego klucza na losowo generowanej mapie o wymiarach 6x6 pól. 
1. **Faza Szukania:** Poruszasz się i na podstawie komunikatów "Ciepło" / "Zimno" próbujesz zlokalizować klucz.
2. **Faza Ucieczki:** Po podniesieniu klucza aktywuje się system samo-destrukcji. Masz dokładnie **10 kroków**, aby dotrzeć do ukrytych drzwi ewakuacyjnych.
3. **Zagrożenie:** W momencie zebrania klucza na mapie pojawia się **5 niewidzialnych min**. Masz tylko 2 życia – wejście na bombę skutkuje wybuchem i utratą punktu zdrowia! Drzwi ewakuacyjne zobaczysz dopiero wtedy, gdy znajdziesz się tuż obok nich.

---

## 🛠️ Wymagania i Instalacja

Przed uruchomieniem upewnij się, że masz zainstalowanego Pythona (wersja 3.8 lub nowsza) oraz bibliotekę Pygame.

```bash
# Instalacja wymaganej biblioteki dla wersji graficznej
pip install pygame

🚀 Jak uruchomić wybraną wersję?
Projekt zawiera dwie wersje gry. Możesz je uruchomić bezpośrednio z poziomu edytora (np. PyCharm) lub za pomocą terminala:

1. Wersja Tekstowa (Terminal)
Klasyczna wersja retro. Sterowanie odbywa się poprzez wpisanie kierunku (W, A, S, D) i zatwierdzenie klawiszem Enter. Mapa oraz komunikaty rysowane są bezpośrednio w konsoli.

2. Wersja Graficzna (Pygame)
Nowoczesne okienkowe wydanie gry z płynnym sterowaniem za pomocą klawiszy WASD (bez konieczności klikania Enter).

Niebieski kwadrat – Gracz 🟦

Zielony kwadrat – Drzwi ewakuacyjne 🟩 (ukryte, pojawiają się tylko 1 kafelek od Ciebie)

Dynamiczny dolny panel informacyjny z licznikami żyć oraz kroków ucieczki.

🛠️ Zastosowane technologie i mechaniki
Python 3 – Główna logika gry.

Pygame – Renderowanie grafiki 2D, obsługa zdarzeń klawiatury i pętli gry.

Algorytmy matematyczne (math.sqrt) – Dynamiczne obliczanie dystansu euklidesowego do celów mechaniki ciepło-zimno.

Algorytmy losujące (random) – Dynamiczne generowanie pozycji startowych oraz unikalnego rozstawienia min przy każdej rozgrywce.
