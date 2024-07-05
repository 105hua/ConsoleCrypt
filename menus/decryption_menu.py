import os
import time
import secrets

from consolemenu import SelectionMenu
from libs.hashing import SHA3
from libs.encryption import AES

def decryption_menu():
    # Get the file to decrypt.
    in_dir = os.path.join(os.getcwd(), "in")
    out_dir = os.path.join(os.getcwd(), "out")
    files = [str(file) for file in os.listdir(in_dir) if file.endswith(".enc")]
    if len(files) == 0:
        print("No files to decrypt.")
        time.sleep(3)
        return
    file_menu = SelectionMenu(
        files,
        "Select the file to decrypt",
        "Please select a file from the 'in' dir to decrypt.",
    )
    file_menu.show()
    # Get the user's selection.
    try:
        selected_option = files[file_menu.selected_option]
    except IndexError:
        return
    # Get the password for decryption.
    password = input("Enter the password for decryption: ")
    hasher = SHA3(256)
    key = hasher.hash_string(password)
    # Decrypt the file.
    try:
        with open(os.path.join(in_dir, selected_option), "rb") as file:
            data = file.read()
        iv = data[:16]
        data = data[16:]
        aes = AES(key, iv)
        decrypted_data = aes.decrypt(data)
        # Write the decrypted data to a file.
        with open(os.path.join(out_dir, selected_option[:-4]), "wb") as file:
            file.write(decrypted_data)
        print("File decrypted successfully.")
        time.sleep(3)
        return
    except Exception as e:
        print("An error occurred. Please ensure you entered the correct password.")
        print(f"Error:\n{e}")
        time.sleep(3)
        return
