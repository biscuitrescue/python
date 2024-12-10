#!/usr/bin/env python3

import numpy as np
import pickle
import time
import matplotlib.pyplot as plt
import os

filename = "Text_To_Be_Encrypted.txt"

# Caesar Cipher
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

# Playfair Cipher
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

# Hill Cipher
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

# Plot Encryption and Decryption Times
def plot_times(cipher_names, enc_times, dec_times):
    if len(cipher_names) != len(enc_times) or len(cipher_names) != len(dec_times):
        print("Error: Mismatch between cipher names and time lists")
        return

    x = np.arange(len(cipher_names))  # Create an array of cipher names' indices
    width = 0.35  # Bar width

    fig, ax = plt.subplots()

    # Plotting encryption and decryption times
    ax.bar(x - width/2, enc_times, width, label='Encryption', color='skyblue')
    ax.bar(x + width/2, dec_times, width, label='Decryption', color='lightcoral')

    ax.set_xlabel('Ciphers')
    ax.set_ylabel('Time (seconds)')
    ax.set_title('Encryption and Decryption Times')
    ax.set_xticks(x)
    ax.set_xticklabels(cipher_names)
    ax.legend()
    plt.tight_layout()  # Adjust layout
    plt.show()

# Main Menu
def menu():
    cipher_names = []
    enc_times = []
    dec_times = []

    while True:
        print("\nChoose a cipher method:")
        print("1. Caesar Cipher")
        print("2. Playfair Cipher")
        print("3. Hill Cipher")
        print("4. Show Graph")
        print("5. Exit")
        choice = input("Enter choice (1-5): ")

        if choice == '1':  # Caesar Cipher
            file_input = input("Read text from file? (y/n): ").lower() == 'y'
            if file_input:
                with open(filename, "r") as f:
                    text = f.read().strip()
            else:
                text = input("Enter text: ")

            if os.path.exists("caesar_key.txt"):
                with open("caesar_key.txt", "r") as f:
                    shift = int(f.read().strip())
                print(f"Using previously saved shift value: {shift}")
            else:
                shift = int(input("Enter shift value: "))
                with open("caesar_key.txt", "w") as f:
                    f.write(str(shift))

            encrypt = input("Encrypt or Decrypt (e/d): ").lower() == 'e'

            start = time.time()
            result = caesar_cipher(text, shift, encrypt)
            end = time.time()
            time_taken = end - start

            print("Result:", result)

            cipher_names.append("Caesar")
            if encrypt:
                enc_times.append(time_taken)
                dec_times.append(0)
            else:
                dec_times.append(time_taken)
                enc_times.append(0)

        elif choice == '2':  # Playfair Cipher
            file_input = input("Read text from file? (y/n): ").lower() == 'y'
            if file_input:
                with open(filename, "r") as f:
                    text = f.read().strip()
            else:
                text = input("Enter text: ")

            if os.path.exists("playfair_key.txt"):
                with open("playfair_key.txt", "r") as f:
                    key = f.read().strip()
                print(f"Using previously saved keyword: {key}")
            else:
                key = input("Enter keyword: ")
                with open("playfair_key.txt", "w") as f:
                    f.write(key)

            encrypt = input("Encrypt or Decrypt (e/d): ").lower() == 'e'

            start = time.time()
            result = playfair_cipher(text, key, encrypt)
            end = time.time()
            time_taken = end - start

            print("Result:", result)

            cipher_names.append("Playfair")
            if encrypt:
                enc_times.append(time_taken)
                dec_times.append(0)
            else:
                dec_times.append(time_taken)
                enc_times.append(0)

        elif choice == '3':  # Hill Cipher
            file_input = input("Read text from file? (y/n): ").lower() == 'y'
            if file_input:
                with open(filename, "r") as f:
                    text = f.read().strip()
            else:
                text = input("Enter text: ")

            if os.path.exists("hill_key.bin"):
                with open("hill_key.bin", "rb") as f:
                    key = pickle.load(f)
                print(f"Using previously saved key matrix: {key}")
            else:
                n = int(input("Enter matrix size (e.g., 2 for 2x2, 3 for 3x3): "))
                key = []
                print("Enter key matrix values row by row:")
                for _ in range(n):
                    row = list(map(int, input().split()))
                    key.extend(row)
                with open("hill_key.bin", "wb") as f:
                    pickle.dump(key, f)

            encrypt = input("Encrypt or Decrypt (e/d): ").lower() == 'e'

            start = time.time()
            result = hill_cipher(text, key, encrypt)
            end = time.time()
            time_taken = end - start

            print("Result:", result)

            cipher_names.append("Hill")
            if encrypt:
                enc_times.append(time_taken)
                dec_times.append(0)
            else:
                dec_times.append(time_taken)
                enc_times.append(0)

        elif choice == '4':  # Show Graph
            plot_times(cipher_names, enc_times, dec_times)

        elif choice == '5':  # Exit
            print("Exiting.")
            break

        else:
            print("Invalid choice. Please try again.")

menu()
