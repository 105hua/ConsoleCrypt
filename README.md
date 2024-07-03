# ConsoleCrypt

## Introduction

ConsoleCrypt is a Console Application, written in Python, that provides a simple way for
the user to encrypt and decrypt files. The main intention of ConsoleCrypt is to simplify
the process of securing sensitive files while also providing no compromises on the
security of the file itself. It achieves this effectively through hashing the encryption
key with the SHA3-256 Hash Function, which is then used to encrypt the file with the
AES-256 Encryption Algorithm.

## Structure

The structure of the application is like so:

```
main.py
menus
    \ - decryption_menu.py
    \ - encryption_menu.py
    \ - main_menu.py
```

The application is started through the `main.py` script, where the menus of the application
are then accessed. Each of the menus within the application are stored within their own
script for organisational purposes:

- `main.py` : The main script is responsible for the creation of the `in` and `out` dirs, as
well as displaying the main menu. The `in` directory is the location in which the user will
place the files that they would like to encrypt with the application, while the `out`
directory is used to save files after they are encrypted.

- `decryption_menu.py` : The decryption menu is responsible for guiding the user through the
decryption of their encrypted file.

- `encryption_menu.py` : The encryption menu is responsible for guiding the user through the
encryption of their file.

- `main_menu.py` : The main menu acts as a bridge towards the main functionalities of the
application, which is the encryption and decryption menus. Within this menu, the user is
also encouraged to place the file they want to encrypt/decrypt into the `in` directory
before continuing forward with the application.

## Setup

To setup this application, please follow these steps:

- Setup a Virtual Environment by running `py -m venv venv` in a terminal of your
choice.

- Activate the Virtual Environment by running `venv\Scripts\activate`. If you are
running on a Linux Machine, then you will need to run `source venv/bin/activate`.

- Install the dependencies for the application through running
`pip install -r requirements.txt`.

- Start the application by running `py main.py`.

- When you are done using the application, you may deactivate the Virtual Environment
by running `venv\Scripts\deactivate`. If you're running on a Linux Machine, then you
will need to run `source venv/bin/activate`.

## Future Ideas

Ideas that may be considered for implementation into this program in the future are as
follows:

- `Batch Encryption` : To simplify the process of encrypting multiple files at once with
the application, a feature may be added in which the user can select several files from
the `in` directory to encrypt all at once. The files will then be encrypted one-by-one
until there are no remaining files to encrypt.

- `Different Algorithms` : There may be a case in which the user may wish to use an
encryption algoritm and/or a hash function that is different to that of AES-256 and
SHA3-256. Therefore, giving the user the option to select from different algorithms
may be a good feature to consider for future implementation.