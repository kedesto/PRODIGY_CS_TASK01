def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            # Determine the appropriate case (upper or lower)
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            # Apply the shift
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result

def main():
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (positive for encryption, negative for decryption): "))
    mode = input("Enter 'encrypt' for encryption or 'decrypt' for decryption: ").lower()

    if mode == 'encrypt':
        encrypted_message = caesar_cipher(message, shift, mode)
        print("Encrypted message:", encrypted_message)
    elif mode == 'decrypt':
        decrypted_message = caesar_cipher(message, shift, mode)
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
