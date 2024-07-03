from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem

from menus.decryption_menu import decryption_menu
from menus.encryption_menu import encryption_menu


def main_menu():
    menu = ConsoleMenu(
        "ConsoleCrypt",
        "Welcome to ConsoleCrypt, a simple cryptography program, ran straight from your terminal. Please add your files to the 'in' directory and select an option below.",
    )
    menu.append_item(FunctionItem("Encrypt a file", encryption_menu))
    menu.append_item(FunctionItem("Decrypt a file", decryption_menu))
    menu.show()
