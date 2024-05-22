#Author: Christabel Obi-Nwosu
#Date: Monday 27, 2023
#File: ola9.py
#Prgram to create a ceaser cipher to encode
#and decode a message. 
ALPHABET=list("abcdefghijklmnopqrstuvwxyz ")
def main():
    message=input("Enter the message you want to encode: ")
    key=int(input("Enter the key: "))
    print("Encoding message","'"+message+"'","with key",key)
    message=message.lower()
    cipher=generate_cipher(key)
    encode_msg=encode_message(message,cipher)
    print("Encoded:",encode_msg)
    decode_msg=decode_message(encode_msg,cipher)
    print("Decoded:",decode_msg)

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
    
main()