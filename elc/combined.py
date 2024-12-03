#!/usr/bin/env python3

import numpy as np
import pickle


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


def generate_key_matrix(keyword):
    matrix = []
    seen = set()
    for char in keyword.upper() + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in seen and char != 'J':
            seen.add(char)
            matrix.append(char)
    return [matrix[i:i + 5] for i in range(0, 25, 5)]


def find_position(char, matrix):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)


def playfair_cipher(text, key, encrypt=True):
    matrix = generate_key_matrix(key)
    text = text.upper().replace("J", "I")
    if len(text) % 2 != 0:
        text += "X"
    result = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        row1, col1 = find_position(a, matrix)
        row2, col2 = find_position(b, matrix)
        if row1 == row2:
            col1 = (col1 + (1 if encrypt else -1)) % 5
            col2 = (col2 + (1 if encrypt else -1)) % 5
        elif col1 == col2:
            row1 = (row1 + (1 if encrypt else -1)) % 5
            row2 = (row2 + (1 if encrypt else -1)) % 5
        else:
            col1, col2 = col2, col1
        result += matrix[row1][col1] + matrix[row2][col2]
    return result


def mod_inverse(matrix, modulus):
    det = int(round(np.linalg.det(matrix))) % modulus
    det_inv = pow(det, -1, modulus)
    matrix_inv = det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    return matrix_inv


def hill_cipher(text, key, encrypt=True):
    n = int(len(key) ** 0.5)
    matrix_key = np.array(key).reshape(n, n) % 26
    if not encrypt:
        matrix_key = mod_inverse(matrix_key, 26)
    text = text.upper().replace(" ", "")
    if len(text) % n != 0:
        text += "X" * (n - len(text) % n)
    result = ""
    for i in range(0, len(text), n):
        vector = [ord(char) - 65 for char in text[i:i + n]]
        transformed = np.dot(matrix_key, vector) % 26
        result += ''.join(chr(int(num) + 65) for num in transformed)
    return result


def menu():
    while True:
        print("\nChoose a cipher method:")
        print("1. Caesar Cipher")
        print("2. Playfair Cipher")
        print("3. Hill Cipher")
        print("4. Exit")
        choice = input("Enter choice (1-4): ")

        if choice == '1':
            text = input("Enter text: ")
            shift = int(input("Enter shift value: "))
            mode = input("Encrypt or Decrypt (e/d): ").lower()
            result = caesar_cipher(text, shift, encrypt=(mode == 'e'))
            print("Result:", result)

        elif choice == '2':
            text = input("Enter text: ")
            key = input("Enter keyword: ")
            mode = input("Encrypt or Decrypt (e/d): ").lower()
            result = playfair_cipher(text, key, encrypt=(mode == 'e'))
            print("Result:", result)

            with open("file.txt", "w") as f:
                f.write(key)

        elif choice == '3':
            text = input("Enter text: ")
            n = int(input("Enter matrix size (e.g., 2 for 2x2, 3 for 3x3): "))
            key = []
            print("Enter key matrix values row by row:")
            for _ in range(n):
                row = list(map(int, input().split()))
                key.extend(row)
            mode = input("Encrypt or Decrypt (e/d): ").lower()
            result = hill_cipher(text, key, encrypt=(mode == 'e'))
            print("Result:", result)
            with open("file.txt", "wb") as f:
                pickle.dump(key, f)

        elif choice == '4':
            print("Exiting.")
            break

        else:
            print("Invalid choice. Please try again.")


menu()
