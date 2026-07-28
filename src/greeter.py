"""Small module to greet people in multiple colors, from Alan Turing"""

import colorama


def greet(personal: str, family: str, title: str = "", polite: bool = False):
    """
    Prints a welcome message in multiple colors.
    """
    greeting = "How do you do, " if polite else "Hey, "
    greeting = colorama.Back.BLACK + colorama.Fore.YELLOW + greeting
    if title:
        greeting += colorama.Back.BLUE + colorama.Fore.WHITE + title + " "

    greeting += (
        colorama.Back.WHITE
        + colorama.Style.BRIGHT
        + colorama.Fore.RED
        + personal
        + " "
        + family
    )
    return greeting
