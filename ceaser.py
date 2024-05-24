#Author: Christabel Obi-Nwosu
#Date: Monday 27, 2023
#Prgram to create a ceaser cipher to encode
#and decode a message. 
ALPHABET=list("abcdefghijklmnopqrstuvwxyz ")
def main():
    message=input("Enter the message you want to encode: ")
    key = get_key()
    print("Encoding message","'"+message+"'","with key",key)
    message=message.lower()
    cipher=generate_cipher(key)
    encode_msg=encode_message(message,cipher)
    print("\nEncoded Message:")
    display_message(encoded_message)

    decode_msg=decode_message(encode_msg,cipher)
    print("\nDecoded Message:")
    display_message(decoded_message)

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
    cipher=ALPHABET[(len(ALPHABET)-key):]+ALPHABET[:(len(ALPHABET)-key)]
    return cipher
    
def encode_message(message,cipher):
    encode_msg=''
    for chr in message:
        if chr in ALPHABET:
            encode_msg+=cipher[ALPHABET.index(chr)]
    return encode_msg

def decode_message(encode_msg,cipher):
    decode_msg=''
    for chr in encode_msg:
        if chr in cipher:
            decode_msg+=ALPHABET[cipher.index(chr)]
    return decode_msg
    
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
    
    for row in grid:
        print(''.join(row))

if __name__ == "__main__":
    main()