import os

def cesar_cipher(text,shift, decrypt=False):
    if decrypt:
        shift = -shift
    
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def main():
    file_name = input("Enter the name of input text file: ")

    if not os.path.exists(file_name):
        print("Error: File not found. Please create the file and try again.")
        return

    with open(file_name, 'r') as file:
        og_message = file.read().strip()

    shift_value = 3
    encrypted_message = cesar_cipher(og_message, shift_value)
    decrypted_message = cesar_cipher(encrypted_message, shift_value, decrypt=True)

    print("\n" + (5 * "=") + "Output" + (5 * "="))
    print(f"Original Message: {og_message}")
    print(f"Technique used: Caesar Cipher (Shift={shift_value})")
    print(f"Encrypted Message: {encrypted_message}")
    print(f"Decrypted Message: {decrypted_message}")

    if decrypted_message == og_message:
        print("Status: Decryption successful")
    else:
        print("Status: Decryption failed")

if __name__ == "__main__":
    main()