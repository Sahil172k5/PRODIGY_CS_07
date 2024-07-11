def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                new_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                new_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("Caesar Cipher Algorithm")
    choice = input("Type 'encrypt' to encrypt a message or 'decrypt' to decrypt a message: ").strip().lower()
    
    if choice not in ['encrypt', 'decrypt']:
        print("Invalid choice. Please select either 'encrypt' or 'decrypt'.")
        return

    message = input("Enter your message: ").strip()
    shift = int(input("Enter the shift value: ").strip())

    if choice == 'encrypt':
        encrypted_message = caesar_encrypt(message, shift)
        print(f"Encrypted message: {encrypted_message}")
    elif choice == 'decrypt':
        decrypted_message = caesar_decrypt(message, shift)
        print(f"Decrypted message: {decrypted_message}")

main()
