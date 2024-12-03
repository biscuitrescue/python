#!/usr/bin/env python3

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
