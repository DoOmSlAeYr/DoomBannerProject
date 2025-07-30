# doom_banner.py

import pyfiglet
from termcolor import colored
import os
import random

# Available colors
colors = {
    "1": "red",
    "2": "green",
    "3": "blue",
    "4": "cyan",
    "5": "yellow",
    "6": "magenta",
    "7": "white"
}

# Loop forever
while True:
    os.system("clear")

    #  Title in big text
    title = pyfiglet.figlet_format("Doom Banner", font="slant")
    print(colored(title, "cyan"))
    print(colored("by DoomSlayer", "red", attrs=["bold"]))
    print()

    # Text input
    text = input(colored("Enter your text (or type 'exit' to quit): ", "yellow")).strip()
    if text.lower() in ["exit", "quit"]:
        print(colored("\nExiting Doom Banner Generator... Goodbye! ☠️", "magenta"))
        break
    if not text:
        print(colored("Text cannot be empty!", "red"))
        continue

    # Font selection
    fonts = pyfiglet.FigletFont.getFonts()
    print(colored("\nAvailable fonts (examples):", "cyan"))
    print(colored("slant, banner, big, block, bubble, digital, standard, doom", "grey"))
    font_name = input(colored("Choose a font (leave blank for default): ", "yellow")).strip()
    if font_name not in fonts:
        font_name = "standard"

    # Color selection
    print(colored("\nChoose a color:", "cyan"))
    for num, color in colors.items():
        print(f"{num}) {color}")
    color_choice = input(colored("Enter number (leave blank for random): ", "yellow")).strip()
    color = colors.get(color_choice, random.choice(list(colors.values())))

    # Generate banner
    banner = pyfiglet.Figlet(font=font_name).renderText(text)
    print()
    print(colored(banner, color=color))
    print(colored("─" * 50, "grey"))
    print(colored("by DoomSlayer", "red", attrs=["bold"]))
    print()

    # Ask if user wants to continue
    again = input(colored("Generate another banner? (y/n): ", "cyan")).lower().strip()
    if again not in ["y", "yes"]:
        print(colored("\nExiting Doom Banner, see ya!", "magenta"))
        break
