# Function to encrypt the message
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

# Function to decrypt the message
def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char
    return decrypted_text

# Main program to take input from the user
def caesar_cipher():
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()
    text = input("Enter your message: ")
    shift = int(input("Enter shift value: "))
    
    if choice == 'encrypt':
        result = encrypt(text, shift)
        print(f"Encrypted message: {result}")
    elif choice == 'decrypt':
        result = decrypt(text, shift)
        print(f"Decrypted message: {result}")
    else:
        print("Invalid choice! Please choose either 'encrypt' or 'decrypt'.")

# Run the program
caesar_cipher()
