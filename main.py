import os

from menus.main_menu import main_menu

if __name__ == "__main__":
    in_dir = os.path.join(os.getcwd(), "in")
    out_dir = os.path.join(os.getcwd(), "out")
    if not os.path.exists(in_dir):
        os.mkdir(in_dir)
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    main_menu()