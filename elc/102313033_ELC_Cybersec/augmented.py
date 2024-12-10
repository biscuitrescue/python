#!/usr/bin/env python3

import time
import pickle
import numpy as np
import matplotlib.pyplot as plt


def save_key_to_file(file_path, key):
    with open(file_path, 'wb') as f:
        pickle.dump(key, f)


def load_key_from_file(file_path):
    try:
        with open(file_path, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        print(f"Key file {file_path} not found. Ensure the key exists.")
        return None


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
    raise ValueError(f"Character {char} not found in matrix")


def playfair_cipher(text, key, encrypt=True):
    matrix = generate_key_matrix(key)
    text = ''.join([char for char in text.upper() if char.isalpha()])
    text = text.replace("J", "I")
    processed_text = []
    i = 0
    while i < len(text):
        if i == len(text) - 1 or text[i] == text[i + 1]:
            processed_text.append(text[i] + 'X')
            i += 1
        else:
            processed_text.append(text[i:i + 2])
            i += 2
    result = ""
    for pair in processed_text:
        a, b = pair[0], pair[1]
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
    det = int(round(np.linalg.det(matrix)))
    if det % modulus == 0 or np.gcd(det % modulus, modulus) != 1:
        raise ValueError("Key matrix is not invertible modulo 26.")
    det_inv = pow(det % modulus, -1, modulus)
    adjugate = np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    matrix_inv = (det_inv * adjugate) % modulus
    return matrix_inv


def hill_cipher(text, key, encrypt=True):
    n = int(np.sqrt(len(key)))
    matrix_key = np.array(key).reshape(n, n) % 26
    if not encrypt:
        matrix_key = mod_inverse(matrix_key, 26)
    text = text.upper().replace(" ", "")
    if len(text) % n != 0:
        text += "X" * (n - len(text) % n)
    result = ""
    for i in range(0, len(text), n):
        vector = np.array([ord(char) - 65 for char in text[i:i + n]])
        transformed = np.dot(matrix_key, vector) % 26
        result += ''.join(chr(int(num) + 65) for num in transformed)
    return result


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return ""


def write_to_file(file_path, text):
    try:
        with open(file_path, 'w') as file:
            file.write(text)
    except IOError:
        pass


def measure_time(cipher_func, text, *args):
    start_time = time.time()
    cipher_func(text, *args)
    return time.time() - start_time


def run_timing_tests(file_path):
    input_text = read_file(file_path)
    if not input_text:
        print("No text to process. Exiting test.")
        return None
    shift = load_key_from_file('caesar_key.bin')
    playfair_key = load_key_from_file('playfair_key.bin')
    hill_key = load_key_from_file('hill_key.bin')

    caesar_encrypt_time = measure_time(caesar_cipher, input_text, shift, True)
    caesar_decrypt_time = measure_time(caesar_cipher, input_text, shift, False)
    playfair_encrypt_time = measure_time(playfair_cipher, input_text,
                                         playfair_key, True)
    playfair_decrypt_time = measure_time(playfair_cipher, input_text,
                                         playfair_key, False)
    hill_encrypt_time = measure_time(hill_cipher, input_text, hill_key, True)
    hill_decrypt_time = measure_time(hill_cipher, input_text, hill_key, False)
    text_length = len(input_text)

    encryption_times = [caesar_encrypt_time, playfair_encrypt_time,
                        hill_encrypt_time]
    decryption_times = [caesar_decrypt_time, playfair_decrypt_time,
                        hill_decrypt_time]

    return encryption_times, decryption_times, text_length


def plot_graph(encryption_times, decryption_times, text_length):
    bar_width = 0.35
    index = np.arange(len(encryption_times))

    fig, ax = plt.subplots(figsize=(10, 6))

    bar1 = ax.bar(index, encryption_times, bar_width,
                  label='Encryption Time', color='blue')
    bar2 = ax.bar(index + bar_width, decryption_times, bar_width,
                  label='Decryption Time', color='green')

    ax.set_xlabel('Cipher Type')
    ax.set_ylabel('Time (seconds)')
    ax.set_title(f'Encryption and Decryption Times for {text_length} characters')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(['Caesar', 'Playfair', 'Hill'])
    ax.legend()

    plt.tight_layout()
    plt.show()


def menu():
    while True:
        print("\nChoose an action:")
        print("1. Encrypt and Save All Ciphers (Caesar, Playfair, Hill) to Files")
        print("2. Decrypt and Save All Ciphers (Caesar, Playfair, Hill) from Files")
        print("3. Test Encryption/Decryption Time for a File")
        print("4. Plot Encryption/Decryption Times")
        print("5. Exit")
        choice = input("Enter choice (1-5): ")

        try:
            if choice == '1':
                input_text = read_file('text.txt')
                caesar_encrypted = caesar_cipher(input_text, 3, encrypt=True)
                playfair_encrypted = playfair_cipher(input_text, "WHICH", encrypt=True)
                hill_encrypted = hill_cipher(input_text, [11, 2, 19, 5, 23, 25, 20, 7, 17], encrypt=True)

                write_to_file('caesar_encrypted.txt', caesar_encrypted)
                write_to_file('playfair_encrypted.txt', playfair_encrypted)
                write_to_file('hill_encrypted.txt', hill_encrypted)

                save_key_to_file('caesar_key.bin', 3)
                save_key_to_file('playfair_key.bin', "WHICH")
                save_key_to_file('hill_key.bin', [11, 2, 19, 5, 23, 25, 20, 7, 17])

            elif choice == '2':
                caesar_encrypted = read_file('caesar_encrypted.txt')
                playfair_encrypted = read_file('playfair_encrypted.txt')
                hill_encrypted = read_file('hill_encrypted.txt')

                caesar_decrypted = caesar_cipher(caesar_encrypted, load_key_from_file('caesar_key.bin'), encrypt=False)
                playfair_decrypted = playfair_cipher(playfair_encrypted, load_key_from_file('playfair_key.bin'), encrypt=False)
                hill_decrypted = hill_cipher(hill_encrypted, load_key_from_file('hill_key.bin'), encrypt=False)

                write_to_file('caesar_decrypted.txt', caesar_decrypted)
                write_to_file('playfair_decrypted.txt', playfair_decrypted)
                write_to_file('hill_decrypted.txt', hill_decrypted)

            elif choice == '3':
                file_path = './text.txt'
                times = run_timing_tests(file_path)
                if times:
                    encryption_times, decryption_times, text_length = times
                    print(f"Encryption Times: {encryption_times}")
                    print(f"Decryption Times: {decryption_times}")

            elif choice == '4':
                file_path = './text.txt'
                times = run_timing_tests(file_path)
                if times:
                    encryption_times, decryption_times, text_length = times
                    plot_graph(encryption_times, decryption_times, text_length)

            elif choice == '5':
                break

        except ValueError:
            pass

menu()
