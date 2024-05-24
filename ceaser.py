# Author: Christabel Obi-Nwosu
# Date: Monday 27, 2023
# Program to create a Caesar cipher to encode and decode a message.

import math

ALPHABET = list("abcdefghijklmnopqrstuvwxyz ")

def main():
    message = input("Enter the message you want to encode: ")
    key = get_key()
    print("Encoding message", "'" + message + "'", "with key", key)
    message = message.lower()
    cipher = generate_cipher(key)
    encode_msg = encode_message(message, cipher)
    
    with open("output.txt", "w") as file:
        file.write("\nEncoded Message:\n")
        file.write(encode_msg + "\n")
        file.write(display_message(encode_msg))
        
        decoded_message = decode_message(encode_msg, cipher)
        file.write("\n\nDecoded Message:\n")
        file.write(decoded_message + "\n")
        file.write(display_message(decoded_message))
    
    print("Output has been written to output.txt")

def get_key():
    while True:
        try:
            key = int(input("Enter the key (0-26): "))
            if 0 <= key < len(ALPHABET):
                return key
            else:
                print(f"Please enter a key between 0 and {len(ALPHABET) - 1}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def generate_cipher(key):
    return ALPHABET[key:] + ALPHABET[:key]

def encode_message(message, cipher):
    encoded_message = ''
    for char in message:
        if char in ALPHABET:
            encoded_message += cipher[ALPHABET.index(char)]
    return encoded_message

def decode_message(encoded_message, cipher):
    decoded_message = ''
    for char in encoded_message:
        if char in cipher:
            decoded_message += ALPHABET[cipher.index(char)]
    return decoded_message

def display_message(message):
    radius = 10
    n = len(message)
    angle_step = 2 * math.pi / n
    center_x = 20
    center_y = 10
    grid_size = 40
    
    # Create an empty grid
    grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
    
    for i, char in enumerate(message):
        angle = i * angle_step
        x = int(center_x + radius * math.cos(angle))
        y = int(center_y + radius * math.sin(angle))
        grid[y][x] = char
    
    output = "\n".join(''.join(row) for row in grid)
    return output

if __name__ == "__main__":
    main()
