import os
import secrets
import time

from consolemenu import SelectionMenu
from libs.encryption import AES
from libs.hashing import SHA3

possible_chars = [
    *"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{}|;':,.<>?/"
]


def generate_key(length: int) -> str:
    key = ""
    for _ in range(length):
        key += secrets.choice(possible_chars)
    return key


def encryption_menu():
    # Ask user if they want to enter a password for encryption.
    options = ["Yes", "No"]
    menu = SelectionMenu(
        options,
        "Password for Encryption",
        "Would you like to enter a password for encryption? If not, a random password will be generated.",
    )
    menu.show()
    # Get the user's selection and generate a password if they choose not to enter one.
    # If an IndexError is raised, assume the user exited the menu.
    try:
        selection_option = options[menu.selected_option]
        if selection_option == "Yes":
            password = input("Enter a password: ")
        else:
            password = generate_key(32)
    except IndexError:
        return
    # Hash the password using SHA3-256.
    hasher = SHA3(256)
    key = hasher.hash_string(password)
    # Get the file to encrypt.
    in_dir = os.path.join(os.getcwd(), "in")
    out_dir = os.path.join(os.getcwd(), "out")
    files = os.listdir(in_dir)
    if len(files) == 0:
        print("No files to encrypt.")
        time.sleep(3)
        return
    menu = SelectionMenu(
        files, "File Selection", "Please select a file from the 'in' dir to encrypt."
    )
    menu.show()
    # Get the user's selection.
    try:
        file = files[menu.selected_option]
    except IndexError:
        return
    # Read the file's contents.
    with open(os.path.join(in_dir, file), "rb") as f:
        data = f.read()
    # Generate a random IV.
    iv = secrets.token_bytes(16)
    # Encrypt the data.
    aes = AES(key, iv)
    encrypted_data = aes.encrypt(data)
    # Write the encrypted data to a file.
    with open(os.path.join(out_dir, str(file + ".enc")), "wb") as f:
        f.write(iv)
        f.write(encrypted_data)
    with open(os.path.join(out_dir, str(file + ".key")), "w") as f:
        f.write(password)
    # Print a success message.
    print("Your file has been encrypted successfully.")
    print("Your key has also been saved alongside the encrypted file.")
    print(
        "Please save this key in a safe space and then delete it from your computer as soon as possible."
    )
    print("If you lose this key, you will not be able to decrypt your file.")
    # Return after 10 seconds.
    time.sleep(10)
    return
