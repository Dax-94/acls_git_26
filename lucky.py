
import random
import time
import os

GREEN = "\033[92m"
GOLD = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def slow_print(text, delay=0.025):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def show_logo():
    print(GREEN + BOLD + r"""
     ██╗     ██╗   ██╗ ██████╗██╗  ██╗██╗   ██╗
     ██║     ██║   ██║██╔════╝██║ ██╔╝╚██╗ ██╔╝
     ██║     ██║   ██║██║     █████╔╝  ╚████╔╝
     ██║     ██║   ██║██║     ██╔═██╗   ╚██╔╝
     ███████╗╚██████╔╝╚██████╗██║  ██╗   ██║
     ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝   ╚═╝
    """ + RESET)
    print(GOLD + "          ✦ YOUR DESTINY STARTS HERE ✦" + RESET)
    print()

def main():
    clear()
    show_logo()

    name = input("Wie heisst du, Glückspilz? ").strip()
    if not name:
        name = "Lucky"

    clear()
    show_logo()

    slow_print(f"Willkommen, {name}.")
    slow_print("Das Universum hat eine Nachricht für dich ...")
    print()

    for i in range(3):
        symbols = ["✦", "☘", "★", "✧", "🍀"]
        print(CYAN + " ".join(
            random.choice(symbols) for _ in range(12)
        ) + RESET)
        time.sleep(0.45)

    print()
    slow_print(GOLD + "Analysiere deine kosmische Glücksfrequenz..." + RESET)
    time.sleep(1)

    luck = random.randint(1, 100)
    lucky_number = random.randint(1, 99)

    messages = [
        "Eine unerwartete Chance wartet auf dich.",
        "Heute ist Mut wertvoller als Perfektion.",
        "Etwas, das du suchst, ist näher als du denkst.",
        "Deine nächste Entscheidung könnte alles verändern.",
        "Manchmal ist der Zufall nur eine Chance in Verkleidung.",
        "Du bist bereit für etwas, das du dir bisher kaum zugetraut hast."
    ]

    print()
    print(GOLD + "╔══════════════════════════════════════╗")
    print("║          DEIN GLÜCKSBERICHT          ║")
    print("╚══════════════════════════════════════╝" + RESET)

    print(f"\n  Name:        {name}")
    print(f"  Glückszahl:  {GOLD}{lucky_number}{RESET}")
    print(f"  Glückslevel: {GREEN}{luck}%{RESET}")

    bars = int(luck / 5)
    print("\n  Glücksenergie:")
    print("  [" + GREEN + "█" * bars + RESET +
          "░" * (20 - bars) + f"] {luck}%")

    print("\n" + CYAN + "  Deine Botschaft:" + RESET)
    slow_print("  " + random.choice(messages))

    if luck >= 80:
        slow_print("\n  🍀 Ein aussergewöhnlicher Tag erwartet dich!")
    elif luck >= 50:
        slow_print("\n  ✨ Halte die Augen offen für Möglichkeiten.")
    else:
        slow_print("\n  🌙 Auch kleine Schritte bringen dich weiter.")

    print("\n" + GREEN + "  REMEMBER: CREATE YOUR OWN LUCK." + RESET)
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nBis zum nächsten Mal, Lucky! 🍀")
