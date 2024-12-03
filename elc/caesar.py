#!/usr/bin/env python3

def caesar_cipher(text, shift, encrypt=True):
    shift = shift if encrypt else -shift
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result


def menu():
    while True:
        print("\nChoose a cipher method:")
        print("1. Caesar Cipher")
        print("2. Exit")
        choice = input("Enter choice (1-2): ")

        if choice == '1':
            text = input("Enter text: ")
            shift = int(input("Enter shift value: "))
            mode = input("Encrypt or Decrypt (e/d): ").lower()
            result = caesar_cipher(text, shift, encrypt=(mode == 'e'))
            print("Result:", result)
        else:
            exit("incorrect input")


menu()
