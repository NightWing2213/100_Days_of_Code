alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    ealphabet = ""
    for letter in original_text:
        shift_pos = alphabet.index(letter) + shift_amount
        shift_pos %= len(alphabet) #ensure shifting stays within range
        ealphabet += alphabet[shift_pos]
    print(f"Here is your encrypted text {ealphabet}")

encrypt(text, shift)
