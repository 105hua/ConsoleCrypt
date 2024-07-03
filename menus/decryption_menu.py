import os
import time
from consolemenu import *
from consolemenu.items import *
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

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
        "Please select a file from the 'in' dir to decrypt."
    )
    file_menu.show()
    # Get the user's selection.
    try:
        selected_option = files[file_menu.selected_option]
    except IndexError:
        return
    # Get the password for decryption.
    password = input("Enter the password for decryption: ")
    hasher = hashes.Hash(hashes.SHA3_256())
    hasher.update(password.encode("utf-8"))
    key = hasher.finalize()
    # Decrypt the file.
    try:
        with open(os.path.join(in_dir, selected_option), "rb") as file:
            data = file.read()
        cipher = Cipher(algorithms.AES(key), modes.CBC(data[:16]))
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(data[16:]) + decryptor.finalize()
        # Unpad the decrypted data.
        unpadder = padding.PKCS7(256).unpadder()
        unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()
        # Write the decrypted data to a file.
        with open(os.path.join(out_dir, selected_option[:-4]), "wb") as file:
            file.write(unpadded_data)
        print("File decrypted successfully.")
        time.sleep(3)
        return
    except Exception as e:
        print(f"An error occurred. Please ensure you entered the correct password.")
        print(f"Error:\n{e}")
        time.sleep(3)
        return