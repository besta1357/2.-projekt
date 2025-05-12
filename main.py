"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Peter Šebest
email: psebest11@gmail.com
"""

def hraci_pole(pole):
    """
    Vykreslí aktuální stav herního pole.
    """
    print(f"+---+---+---+".center(50))
    print(f"| {pole[1]} | {pole[2]} | {pole[3]} |".center(50))
    print(f"+---+---+---+".center(50))
    print(f"| {pole[4]} | {pole[5]} | {pole[6]} |".center(50))
    print(f"+---+---+---+".center(50))
    print(f"| {pole[7]} | {pole[8]} | {pole[9]} |".center(50))
    print(f"+---+---+---+".center(50))

def vyherna_kombinace(pole, hrac_na_tahu):
    """
    Zkontroluje, zda daný hráč má vítěznou kombinaci.
    """
    kombinace = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),    #kombinace v řádku
        (1, 4, 7), (2, 5, 8), (3, 6, 9),    #kombinace ve sloupci
        (1, 5, 9), (3, 5, 7),               #kombinace v diagonále  
    ]
    for x, y, z in kombinace:
        if pole[x] == pole[y] == pole[z] == hrac_na_tahu:
            return True
    return False

def remiza(pole):
    """
    Zjistí, zda je hra remízou (žádná volná pole).
    """
    return " " not in pole.values()

def hrej_tah(tah, hrac_na_tahu, pole):
    """
    Provede tah hráče a vykreslí nové pole.
    """
    tah_int = int(tah)
    pole[tah_int] = hrac_na_tahu            # označí pole hráčem
    hraci_pole(pole)

def kontrola_vstupu(tah, pole):
    """
    Ověří, zda je vstup hráče platný.
    """
    if not tah.isdigit():
       return("Zadej číslo")
    tah_int = int(tah)   
    if not 1 <= tah_int <= 9:    
       return("Zadej číslo 1-9")
    if pole[tah_int] != " ":
       return("Pozice je obsazena")

def zmena_hrace(hrac_na_tahu):
    """
    Přepne hráče z X na O nebo z O na X.
    """
    return "O" if hrac_na_tahu == "X" else "X"

def hlavni_hra():
    """
    Spustí celou hru: inicializuje pole a předá řízení do herní smyčky.
    """
    pole = {i: " " for i in range(1, 10)}
    hrac_na_tahu = "X"
    dvojita_cara = "=" * 50
    print(dvojita_cara)
    print("Welcome to Tic Tac Toe".center(50))
    print(dvojita_cara)
    print(
        """GAME RULES:
    Each player can place one mark (or stone)
    per turn on the 3x3 grid. The WINNER is
    who succeeds in placing three of their
    marks in a:
    * horizontal,
    * vertical or
    * diagonal row"""
    )
    print(dvojita_cara)
    print("Let's start the game".center(50))
    print(dvojita_cara)
    hraci_pole(pole)
    print(dvojita_cara)
    prubeh_hry(pole, hrac_na_tahu)

def prubeh_hry(pole, hrac_na_tahu):
    """
    Obsahuje hlavní smyčku hry: zpracování tahů, kontrola výhry nebo remízy.
    """
    hra_bezi = True
    dvojita_cara = "=" * 50
    
    while hra_bezi:
        tah = input(f"Player {hrac_na_tahu} | Please enter your move number: ")
        print(dvojita_cara)
        chyba = kontrola_vstupu(tah, pole)
        if chyba:
            print(chyba)
            print(dvojita_cara)
            continue

        hrej_tah(tah, hrac_na_tahu, pole)
        print(dvojita_cara)

        if vyherna_kombinace(pole, hrac_na_tahu):
            print(f"Congratulations, the player {hrac_na_tahu} WON!".center(50))
            print(dvojita_cara)
            hra_bezi = False

        elif remiza(pole):
            print(f"The game is draw!".center(50))
            print(dvojita_cara)
            hra_bezi = False

        else:
            hrac_na_tahu = zmena_hrace(hrac_na_tahu)

    print(f"GAME OVER".center(50))
    print()

if __name__ == "__main__":
   hlavni_hra()
