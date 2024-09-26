from PIL import Image
import numpy as np

# Function to encrypt the image
def encrypt_image(image_path, key, output_path):
    img = Image.open(image_path)
    img_array = np.array(img)

    # Apply encryption operation (add the key to each pixel value)
    encrypted_array = (img_array + key) % 256  # Ensure values are between 0 and 255
    
    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

# Function to decrypt the image
def decrypt_image(image_path, key, output_path):
    img = Image.open(image_path)
    img_array = np.array(img)

    # Apply decryption operation (subtract the key from each pixel value)
    decrypted_array = (img_array - key) % 256  # Ensure values are between 0 and 255
    
    decrypted_img = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_img.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

# Main program to take input from the user
def image_cipher():
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt an image: ").lower()
    image_path = input("Enter the image file path: ")
    key = int(input("Enter an encryption/decryption key (an integer): "))
    output_path = input("Enter the output file path (e.g., encrypted_image.png): ")

    if choice == 'encrypt':
        encrypt_image(image_path, key, output_path)
    elif choice == 'decrypt':
        decrypt_image(image_path, key, output_path)
    else:
        print("Invalid choice! Please choose either 'encrypt' or 'decrypt'.")

# Run the program
image_cipher()
