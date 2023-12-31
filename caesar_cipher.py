# Bachelor of Applied IT (SLTC), CIT114 - Information Security 
# Implement the mechanism of encryption and decryption 
# in Caesar Cipher using the Python programming language

def caesar_encrypt(plain_text, shift):
    """
    Encrypts the given plain text using the Caesar Cipher with the given shift.

    args:
        plain_text: The plain text to encrypt
        shift: The shift to use in the Caesar Cipher
    """
    encrypted_text = ""
    for char in plain_text.lower():
        if char.isalpha():
            # Shift the letter by the given shift
            shifted_char = ord(char) + shift
        
            '''
            Wrap around to the beginning of the alphabet
            if the shifted character is outside of the alphabet 
            '''
            if shifted_char > ord('z'):
                shifted_char -= 26

            # Convert the shifted character back to a string
            encrypted_text += chr(shifted_char)
        else:
            # Non-alphabetic characters are left unchanged
            encrypted_text += char

    # returns the encrypted text 
    return encrypted_text


def caesar_decrypt(encrypted_text, shift):
    """
    Decrypts the given encrypted text using the Caesar Cipher with the given shift

    Args:
        encrypted_text: The encrypted text to decrypt.
        shift: The shift to use in the Caesar Cipher.
    """
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            # Shift the letter back by the given shift 
            shifted_char = ord(char) - shift

            '''
            Wrap around to the end of the alphabet 
            if the shifted character is before the beginning of the alphabet.
            '''
            if shifted_char < ord('a'):
                shifted_char += 26
            # Convert the shifted character back to a string
            decrypted_text += chr(shifted_char)
        else:
            # Non-alphabetic characters are left unchanged
            decrypted_text += char

    # returns the decrypted text
    return decrypted_text

def main():

    shift = 3
    # shift = 4
    # shift = 5

    plain_text = input("Enter your secret message: ")
    
    encrypted_text = caesar_encrypt(plain_text, shift)
    decrypted_text = caesar_decrypt(encrypted_text, shift)

    print(f'Plain text: {plain_text.upper()}')
    print(f'Encrypted text: {encrypted_text.upper()}')
    print(f'Decrypted text: {decrypted_text.upper()}')


if __name__ == "__main__":
    main()