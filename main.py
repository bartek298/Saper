import random
import math

game_w=5# szerokosc planszy
game_h=5# wysokosc planszy
key_x=random.randint(0,game_w)
key_y=random.randint(0,game_h)
zycia=2
door_x=0#wspolrzedne drzwi
door_y=0
odliczanie=10# ilosc pozostalych krokow do wyjscia
player_x=random.randint(0,game_w)
player_y=random.randint(0,game_h)
player_found_key=False
#print(player_x,player_y)
steps=0
bomby=[]

distance_before=math.sqrt((key_x-player_x)**2+ (key_y-player_y)**2)#poczatkowy dystans gracza do klucza
def draw_map():#funkcja rysujaca mape
    for n in range(game_h+1):
        for i in range(game_w+1):
            if (player_y==n) and (player_x==i):
                print("X ",end=' ')
            elif (door_y==n) and (door_x==i):#rysowanie drzwi na mapie
                print("D ",end=' ')
            else:
                print('[]',end=' ')
        print()
while True:
    draw_map()
    if zycia==0:
        print("nie masz juz zyc, przegrales!")
        break
    if player_found_key and odliczanie==0:
        print("Boom!! Czas minął, baza wybuchła! Przegrałeś")
        break
    print("")

    if player_found_key:
        print(f"Znalazles klucz, teraz musisz dotrzeć do drzwi, aby je otworzyć!\n Zostało ci {odliczanie} kroków do wyjścia! ")
    else:
        print("Szukaj klucza! Poruszja się za pomocą WASD")
    move=input("dokad idziesz? ")
    steps+=1
    if move=="w":
        player_y-=1
        if player_y<0:
            print("uderzyles w sciane!")
            player_y=0
    elif move=="s":
        player_y+=1
        if player_y >game_h:
            print("uderzyles w sciane!")
            player_y =game_h
    elif move=="a":
        player_x-=1
        if player_x <0:
            print("uderzyles w sciane!")
            player_x =0
    elif move=="d":
        player_x+=1
        if player_x > game_w:
            print("uderzyles w sciane!")
            player_x = game_w
    else:
        print("nie wiem gdzie chcesz isc")
        #logika znalezienia klucza
    if player_x==key_x and player_y==key_y and not player_found_key:
        print("\n🔑 KLUCZ JEST TWÓJ! Aktywowano system samo-destrukcji!")
        print("Wokół ciebie pojawiły się bomby! Uciekaj do drzwi")
        print(f"potrzebowales {steps} kroków")
        player_found_key=True
        #generowanie bomb
        for i in range(5):
            while True:
                bomba_x = random.randint(0, game_w)
                bomba_y = random.randint(0, game_h)
                if (bomba_x, bomba_y) != (player_x, player_y) and (bomba_x, bomba_y) != (key_x, key_y) and (
                    bomba_x, bomba_y) not in bomby:
                    bomby.append((bomba_x, bomba_y))
                    break
        distance_before=math.sqrt((door_x-player_x)**2+(door_y-player_y)**2)
        continue
    if player_x==door_x and player_y==door_y and player_found_key:
        print(f"Udało ci się! Uciekłeś z bazy w {steps} krokach!")
        break

    if player_found_key:
        odliczanie -=1
    if player_found_key:
        distance_after=math.sqrt((door_x-player_x)**2+(door_y-player_y)**2)
    else:
        distance_after = math.sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)
    if distance_before>distance_after:
        print("ciepło, coraz cieplej")
    else:
        print("zimno")
    distance_before=distance_after
    if (player_x, player_y) in bomby:
        print("wpadles na bombe! straciles jedno zycie")
        zycia-=1
        print(f"Pozostałe życia: {zycia}  ")
        bomby.remove((player_x,player_y))











